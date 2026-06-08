import os
import requests
from notion_client import Client
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

notion  = Client(auth=os.environ['NOTION_TOKEN'])
DB_ID   = os.environ['NOTION_DB_SAVES']
SESSION = os.environ['INSTAGRAM_SESSIONID']
CSRF    = os.environ['INSTAGRAM_CSRFTOKEN']
DS      = os.environ['INSTAGRAM_DS_USER_ID']

HEADERS = {
    'Cookie': f'sessionid={SESSION}; csrftoken={CSRF}; ds_user_id={DS}',
    'X-CSRFToken': CSRF,
    'User-Agent': 'Instagram 219.0.0.12.117 Android',
    'X-IG-App-ID': '936619743392459',
    'Accept': 'application/json',
}

def get_existing_ids():
    ids = set()
    cursor = None
    while True:
        params = {'start_cursor': cursor} if cursor else {}
        res = notion.databases.query(database_id=DB_ID, **params)
        for r in res['results']:
            try:
                ids.add(r['properties']['post_id']['title'][0]['text']['content'])
            except Exception:
                pass
        if not res.get('has_more'):
            break
        cursor = res.get('next_cursor')
    return ids

def get_saved_posts():
    url = 'https://www.instagram.com/api/v1/feed/saved/posts/'
    res = requests.get(url, headers=HEADERS, timeout=15)
    if res.status_code != 200:
        print(f'Erro ao buscar posts: HTTP {res.status_code}')
        return []
    return res.json().get('items', [])

def save_to_notion(post):
    media = post.get('media', post)
    media_id = str(media.get('pk', media.get('id', '')))
    user = media.get('user', {})
    author = user.get('username', '')
    profile_pic = user.get('profile_pic_url', '') or 'https://instagram.com'
    caption = media.get('caption', {})
    caption_text = caption.get('text', '') if caption else ''
    thumbnail = (
        media.get('image_versions2', {}).get('candidates', [{}])[0].get('url', '')
        or 'https://instagram.com'
    )
    likes = media.get('like_count', 0) or 0
    views = media.get('play_count', media.get('view_count', 0)) or 0
    media_type = media.get('media_type', 1)
    tipo = 'Reel' if media_type == 2 else 'Post'
    saved_date = datetime.now().strftime('%Y-%m-%d')

    notion.pages.create(
        parent={'database_id': DB_ID},
        properties={
            'post_id':     {'title':     [{'text': {'content': media_id}}]},
            'caption':     {'rich_text': [{'text': {'content': caption_text[:1990]}}]},
            'media_url':   {'url': thumbnail},
            'author':      {'rich_text': [{'text': {'content': author}}]},
            'profile_pic': {'url': profile_pic},
            'likes':       {'number': likes},
            'views':       {'number': views},
            'tipo':        {'select': {'name': tipo}},
            'status':      {'select': {'name': 'Novo'}},
            'saved':       {'date': {'start': saved_date}},
        }
    )

if __name__ == '__main__':
    print(f'[{datetime.now().strftime("%H:%M:%S")}] Iniciando sincronização...')
    existing = get_existing_ids()
    print(f'Posts já no Notion: {len(existing)}')
    posts = get_saved_posts()
    print(f'Posts salvos no Instagram: {len(posts)}')
    total = 0
    for post in posts:
        media = post.get('media', post)
        media_id = str(media.get('pk', media.get('id', '')))
        if media_id in existing:
            continue
        try:
            save_to_notion(post)
            existing.add(media_id)
            total += 1
            print(f'  + Adicionado: {media_id}')
        except Exception as e:
            print(f'  ! Erro no post {media_id}: {e}')
    print(f'Concluído! {total} novos posts adicionados.')
