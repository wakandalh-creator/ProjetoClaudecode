import json
import os
import re
import sys
from google import genai
from google.genai import types as genai_types

sys.stdout.reconfigure(encoding='utf-8')
from notion_client import Client
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

notion   = Client(auth=os.environ['NOTION_TOKEN'])
DB_SAVES = os.environ['NOTION_DB_SAVES']
DB_IDEAS = os.environ['NOTION_DB_IDEAS']
# ponytail: Gemini em vez de Anthropic — ANTHROPIC_API_KEY está sem créditos (ver comentário no .env).
# Trocar de volta é só reverter este bloco + generate_idea() se/quando a conta Anthropic for reativada.
client   = genai.Client(api_key=os.environ['GOOGLE_API_KEY'])
GEMINI_MODEL = 'gemini-3.5-flash'

BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
PASTAS_PATH  = os.path.join(BASE_DIR, '..', 'config', 'instagram-pastas.json')
TEMPLATE_PATH = os.path.join(BASE_DIR, '..', 'Social mídia IA', '_templates', 'roteiro.md')

# ponytail: resumo estático destilado de Social mídia IA/_context/marca.md e tom-de-voz.md
# (snapshot 2026-08-06). Esses arquivos evoluem devagar (base de tom só muda por decisão
# explícita do Lucas); se marca.md/tom-de-voz.md mudarem de forma relevante, atualizar este
# bloco à mão em vez de parsear markdown em runtime pra um resumo de poucas linhas.
BRAND_CONTEXT = """\
MARCA: Neovertix — agência de operações com IA (nunca "marketing digital"). Promessa: "Colocamos IA \
para atender e vender por você — rápido, sem parecer robô." Diferencial: sistema rodando antes de \
fechar contrato; o fundador escreve o código, sem departamento comercial no meio.
PÚBLICO: dono de PME BR (5-50 func. — serviços, e-commerce, clínica, imobiliária, educação) perdendo \
lead por demora no WhatsApp/Instagram. Objeções comuns: "IA soa robótica", "agência nova sem case", \
"quanto tempo leva", "se quebrar, quem conserta".
NÚMEROS ÂNCORA (usar estes, nunca inventar outros): SDR CLT júnior custa ~R$3.800-4.200/mês; 10 leads \
perdidos por demora = R$3.000-15.000/mês em receita não realizada; de 4h de triagem manual pra 15 \
minutos; resposta em segundos, lead às 23h atendido na hora; garantia de 30% de melhora ou o piloto sai \
de graça.
TOM: direto, técnico sem jargão, honesto, sóbrio, orientado a número. Linha 1 sempre gancho puro (nunca \
"Olá" ou apresentação). Número concreto vale mais que adjetivo. Emoji só pontual, nunca 🚀/🔥 em \
sequência, nunca CAPS LOCK. CTA sóbrio e específico ("comenta X que eu te mando"), nunca "CORRE pro \
link!!!". Toda alegação forte precisa de prova nomeável (demo, número, walkthrough).
BANIDAS: revolucionar, turbinar, o futuro chegou, funcionário digital que não dorme, disruptivo, \
sinergia, potencializar, ecossistema, game changer, "vale por N humanos".
"""


def load_angulos():
    try:
        with open(PASTAS_PATH, encoding='utf-8') as f:
            pastas = json.load(f).get('pastas_ativas', [])
        return {p['nome']: p.get('angulo', '') for p in pastas}
    except FileNotFoundError:
        return {}


def load_roteiro_template():
    try:
        with open(TEMPLATE_PATH, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ''


ANGULOS         = load_angulos()
ROTEIRO_TEMPLATE = load_roteiro_template()


def get_new_saves():
    res = notion.databases.query(
        database_id=DB_SAVES,
        filter={'property': 'status', 'select': {'equals': 'Novo'}}
    )
    return res['results'][:10]


def build_prompt(caption, author, angulo):
    direcionamento = f'\nÂngulo desta pasta de origem: {angulo}.\n' if angulo else ''
    return f"""\
{BRAND_CONTEXT}
Você escreve roteiros de conteúdo para a Neovertix seguindo a marca e o tom de voz acima.

Post salvo de @{author} no Instagram (use como inspiração/gancho; se estiver em outro idioma, traduza \
para português do Brasil):
{caption}
{direcionamento}
Gere UM roteiro completo no formato EXATO do template abaixo. Preencha todos os campos entre chaves, \
mantenha os marcadores [GANCHO][EMOÇÃO][VIRADA][PROVA][CTA] literalmente no texto, responda sempre em \
português do Brasil e não escreva nada antes ou depois do bloco:

{ROTEIRO_TEMPLATE}
"""


def generate_idea(caption, author, angulo):
    # ponytail: max_output_tokens alto porque o gemini-3.5-flash gasta parte do orçamento
    # em raciocínio interno antes da resposta final (thinking_budget baixo pra não gastar à toa
    # numa tarefa de copywriting simples, mas sem zerar — zerar piorou a qualidade no teste).
    res = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=build_prompt(caption, author, angulo),
        config=genai_types.GenerateContentConfig(
            max_output_tokens=4000,
            thinking_config=genai_types.ThinkingConfig(thinking_budget=512),
        ),
    )
    return res.text


def parse_roteiro(text):
    """Extrai frontmatter + campos de um roteiro no formato de Social mídia IA/_templates/roteiro.md."""
    text = text.strip()
    text = re.sub(r'^```(?:markdown)?\n|\n```$', '', text)

    frontmatter = {}
    body = text
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', text, re.DOTALL)
    if m:
        fm_text, body = m.group(1), m.group(2)
        for line in fm_text.split('\n'):
            if ':' in line:
                key, _, val = line.partition(':')
                frontmatter[key.strip()] = val.strip()

    titulo = frontmatter.get('titulo') or 'Ideia gerada'
    formato_raw = (frontmatter.get('formato') or 'reel').lower()
    formato = {'reel': 'Reel', 'carrossel': 'Carrossel', 'post': 'Post'}.get(formato_raw, 'Reel')

    gancho_match = re.search(r'\[GANCHO\]\s*(.+)', body)
    gancho = gancho_match.group(1).strip() if gancho_match else ''

    return titulo, formato, gancho, body.strip()


def save_idea(titulo, formato, gancho, roteiro, media_url):
    notion.pages.create(
        parent={'database_id': DB_IDEAS},
        properties={
            'titulo':       {'title':     [{'text': {'content': titulo[:200]}}]},
            'formato':      {'select':    {'name': formato}},
            'Hook':         {'rich_text': [{'text': {'content': gancho[:200]}}]},
            'roteiro':      {'rich_text': [{'text': {'content': roteiro[:1990]}}]},
            'fonte':        {'url': media_url or 'https://instagram.com'},
            'data_geracao': {'date': {'start': datetime.now().strftime('%Y-%m-%d')}},
            'status':       {'select': {'name': 'gravar'}},
        }
    )


def mark_as_processed(page_id):
    notion.pages.update(
        page_id=page_id,
        properties={'status': {'select': {'name': 'Processado'}}}
    )


def _selftest():
    sample = """```markdown
---
titulo: Teste de roteiro
formato: reel
pilar: rapido-de-verdade
---

## Mensagem central
{frase}

## Roteiro

[GANCHO] Seu comercial responde em 30 segundos.
[EMOÇÃO] Lead esfriando de madrugada.
[VIRADA] O agente lê, consulta o CRM e responde.
[PROVA] De 4h de triagem pra 15 minutos.
[CTA] Comenta DEMO que eu te mando.
```"""
    titulo, formato, gancho, roteiro = parse_roteiro(sample)
    assert titulo == 'Teste de roteiro'
    assert formato == 'Reel'
    assert gancho == 'Seu comercial responde em 30 segundos.'
    assert '[PROVA]' in roteiro
    print('OK — selftest passou.')


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        _selftest()
        exit(0)

    print(f'[{datetime.now().strftime("%H:%M:%S")}] Gerando ideias com Gemini...')
    saves = get_new_saves()
    print(f'Posts para processar: {len(saves)}')

    if not saves:
        print('Nenhum post novo. Rode instagram_saves_sync.py primeiro.')
        exit(0)

    for s in saves:
        try:
            props     = s['properties']
            cap_list  = props['caption']['rich_text']
            caption   = cap_list[0]['text']['content'] if cap_list else ''

            if not caption.strip():
                print(f'  - Pulando post sem legenda')
                mark_as_processed(s['id'])
                continue

            auth_list  = props.get('author', {}).get('rich_text', [])
            author     = auth_list[0]['text']['content'] if auth_list else 'desconhecido'
            media_url  = props.get('media_url', {}).get('url', '')
            pasta_nome = (props.get('pasta', {}) or {}).get('select', {}).get('name') if props.get('pasta') else None
            angulo     = ANGULOS.get(pasta_nome, '') if pasta_nome else ''

            print(f'  Gerando ideia para post de @{author} (pasta: {pasta_nome or "?"})...')
            idea_text = generate_idea(caption, author, angulo)
            titulo, formato, gancho, roteiro = parse_roteiro(idea_text)
            save_idea(titulo, formato, gancho, roteiro, media_url)
            mark_as_processed(s['id'])
            print(f'  + Salvo: {titulo}')

        except Exception as e:
            print(f'  ! Erro: {e}')

    print('Concluído!')
