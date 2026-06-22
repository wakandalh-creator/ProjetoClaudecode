import os
import sys
import anthropic

sys.stdout.reconfigure(encoding='utf-8')
from notion_client import Client
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

notion   = Client(auth=os.environ['NOTION_TOKEN'])
DB_SAVES = os.environ['NOTION_DB_SAVES']
DB_IDEAS = os.environ['NOTION_DB_IDEAS']
client   = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])

PROMPT_TEMPLATE = """\
Você é um especialista em criação de conteúdo sobre IA para criadores brasileiros.

Post de @{author} no Instagram:
{caption}

Baseado neste post, crie uma ideia de Reel para criadores brasileiros que querem usar IA no dia a dia.
Responda sempre em português do Brasil, mesmo que o post original esteja em outro idioma (traduza qualquer trecho relevante).
Responda EXATAMENTE neste formato (sem texto extra antes ou depois):

TITULO: [título curto e chamativo, máximo 60 caracteres]
FORMATO: [Reel, Carrossel ou Post]
GANCHO: [primeira frase do vídeo, máximo 10 palavras]
ROTEIRO: [roteiro em 4-5 passos numerados]
"""

def get_new_saves():
    res = notion.databases.query(
        database_id=DB_SAVES,
        filter={'property': 'status', 'select': {'equals': 'Novo'}}
    )
    return res['results'][:10]

def generate_idea(caption, author):
    msg = client.messages.create(
        model='claude-sonnet-4-6',
        max_tokens=800,
        messages=[{
            'role': 'user',
            'content': PROMPT_TEMPLATE.format(author=author, caption=caption)
        }]
    )
    return msg.content[0].text

def parse_idea(text):
    titulo  = 'Ideia gerada'
    formato = 'Reel'
    gancho  = ''
    roteiro = text

    for line in text.split('\n'):
        stripped = line.strip()
        if stripped.startswith('TITULO:'):
            titulo = stripped.replace('TITULO:', '').strip()
        elif stripped.startswith('FORMATO:'):
            raw = stripped.replace('FORMATO:', '').strip()
            formato = raw if raw in ('Reel', 'Carrossel', 'Post') else 'Reel'
        elif stripped.startswith('GANCHO:'):
            gancho = stripped.replace('GANCHO:', '').strip()
        elif stripped.startswith('ROTEIRO:'):
            idx = text.find('ROTEIRO:')
            roteiro = text[idx:].replace('ROTEIRO:', '').strip()

    return titulo, formato, gancho, roteiro

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

if __name__ == '__main__':
    print(f'[{datetime.now().strftime("%H:%M:%S")}] Gerando ideias com Claude...')
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

            auth_list = props.get('author', {}).get('rich_text', [])
            author    = auth_list[0]['text']['content'] if auth_list else 'desconhecido'
            media_url = props.get('media_url', {}).get('url', '')

            print(f'  Gerando ideia para post de @{author}...')
            idea_text = generate_idea(caption, author)
            titulo, formato, gancho, roteiro = parse_idea(idea_text)
            save_idea(titulo, formato, gancho, roteiro, media_url)
            mark_as_processed(s['id'])
            print(f'  + Salvo: {titulo}')

        except Exception as e:
            print(f'  ! Erro: {e}')

    print('Concluído!')
