"""
Script de postagem no Instagram.
Lê ideias com status 'aprovado' no Notion, gera imagem e posta.

COMO ATIVAR:
1. Mude o status de uma ideia no Notion de 'gravar' → 'aprovado'
2. Rode: python post_to_instagram.py
3. Para automação diária: descomente o passo no workflow ig-automation.yml
"""
import os
import time
import requests
from notion_client import Client
from dotenv import load_dotenv
from create_image import criar_imagem

load_dotenv()

notion   = Client(auth=os.environ['NOTION_TOKEN'])
DB_IDEAS = os.environ['NOTION_DB_IDEAS']
SESSION  = os.environ['INSTAGRAM_SESSIONID']
CSRF     = os.environ['INSTAGRAM_CSRFTOKEN']
DS       = os.environ['INSTAGRAM_DS_USER_ID']

HEADERS = {
    'Cookie': f'sessionid={SESSION}; csrftoken={CSRF}; ds_user_id={DS}',
    'X-CSRFToken': CSRF,
    'User-Agent': 'Instagram 219.0.0.12.117 Android',
    'X-IG-App-ID': '936619743392459',
    'Accept': 'application/json',
}

def get_ideias_aprovadas():
    res = notion.databases.query(
        database_id=DB_IDEAS,
        filter={'property': 'status', 'select': {'equals': 'aprovado'}}
    )
    return res['results'][:3]

def upload_foto(imagem_path: str) -> str:
    """Faz upload da imagem e retorna o upload_id."""
    with open(imagem_path, 'rb') as f:
        dados = f.read()

    upload_id = str(int(time.time() * 1000))
    headers = {
        **HEADERS,
        'X-Entity-Type': 'image/jpeg',
        'Offset': '0',
        'X-Entity-Name': f'fb_uploader_{upload_id}',
        'X-Instagram-Rupload-Params': f'{{"upload_id":"{upload_id}","media_type":1,"upload_media_height":1080,"upload_media_width":1080}}',
        'X-Entity-Length': str(len(dados)),
        'Content-Type': 'application/octet-stream',
    }
    url = f'https://i.instagram.com/rupload_igphoto/fb_uploader_{upload_id}'
    res = requests.post(url, data=dados, headers=headers, timeout=30)
    res.raise_for_status()
    return upload_id

def publicar_post(upload_id: str, caption: str) -> dict:
    """Publica o post no Instagram."""
    url = 'https://i.instagram.com/api/v1/media/configure/'
    payload = {
        'upload_id': upload_id,
        'caption': caption,
        'source_type': '4',
        'timezone_offset': '-10800',  # BRT UTC-3
    }
    res = requests.post(url, data=payload, headers=HEADERS, timeout=30)
    res.raise_for_status()
    return res.json()

def marcar_como_publicado(page_id: str):
    notion.pages.update(
        page_id=page_id,
        properties={'status': {'select': {'name': 'publicado'}}}
    )

def montar_caption(props: dict) -> str:
    hook_list   = props.get('Hook', {}).get('rich_text', [])
    roteiro_list= props.get('roteiro', {}).get('rich_text', [])
    hook    = hook_list[0]['text']['content']    if hook_list    else ''
    roteiro = roteiro_list[0]['text']['content'] if roteiro_list else ''
    return f"{hook}\n\n{roteiro}\n\n#IA #InteligenciaArtificial #CriadorDeConteudo #Reels"

if __name__ == '__main__':
    print('Buscando ideias aprovadas...')
    ideias = get_ideias_aprovadas()

    if not ideias:
        print('Nenhuma ideia com status "aprovado". Mude o status no Notion e tente novamente.')
        exit(0)

    print(f'{len(ideias)} ideia(s) para postar.')

    for ideia in ideias:
        try:
            props   = ideia['properties']
            titulo_list = props['titulo']['title']
            titulo  = titulo_list[0]['text']['content'] if titulo_list else 'Post'
            hook_list   = props.get('Hook', {}).get('rich_text', [])
            hook    = hook_list[0]['text']['content'] if hook_list else titulo
            caption = montar_caption(props)

            print(f'  Gerando imagem para: {titulo}')
            imagem = criar_imagem(hook=hook, titulo=titulo, output_path='post_temp.jpg')

            print(f'  Fazendo upload...')
            upload_id = upload_foto(imagem)

            print(f'  Publicando...')
            publicar_post(upload_id, caption)
            marcar_como_publicado(ideia['id'])

            print(f'  + Postado: {titulo}')
            time.sleep(30)  # aguarda entre posts para não acionar limites

        except Exception as e:
            print(f'  ! Erro: {e}')

    print('Concluido!')
