import argparse
import json
import os
from instagrapi import Client as InstaClient
from notion_client import Client
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

notion  = Client(auth=os.environ['NOTION_TOKEN'])
DB_ID   = os.environ['NOTION_DB_SAVES']
SESSION = os.environ['INSTAGRAM_SESSIONID']

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'instagram-pastas.json')
# Fingerprint de dispositivo reaproveitado entre execuções (evita logar "do zero" 2x/dia,
# o que reduz risco de a Meta marcar como comportamento suspeito). Nunca commitar — está no .gitignore.
SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.instagrapi_settings.json')

_client = None


def _get_client():
    """Cliente instagrapi autenticado, reaproveitado entre chamadas no mesmo processo."""
    global _client
    if _client is not None:
        return _client
    cl = InstaClient()
    if os.path.exists(SETTINGS_PATH):
        cl.load_settings(SETTINGS_PATH)
    cl.login_by_sessionid(SESSION)
    cl.dump_settings(SETTINGS_PATH)
    _client = cl
    return _client


def _media_to_dict(m):
    """Converte um objeto Media do instagrapi pro mesmo formato de dict que o código
    (save_to_notion, get_media_id) já espera — assim o resto do script não muda."""
    user = m.user
    return {
        'pk': str(m.pk),
        'user': {
            'username': user.username if user else '',
            'profile_pic_url': str(user.profile_pic_url) if user and user.profile_pic_url else '',
        },
        'caption': {'text': m.caption_text or ''},
        'image_versions2': {'candidates': [{'url': str(m.thumbnail_url)}]} if m.thumbnail_url else {'candidates': [{}]},
        'like_count': m.like_count or 0,
        'play_count': m.play_count or m.view_count or 0,
        'media_type': m.media_type,
    }


def load_pastas_config():
    with open(CONFIG_PATH, encoding='utf-8') as f:
        return json.load(f).get('pastas_ativas', [])


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


def list_collections():
    """Lista as coleções (pastas de salvos) da conta."""
    try:
        cols = _get_client().collections()
    except Exception as e:
        print(f'Erro ao listar coleções: {e}')
        return []
    return [{'collection_id': str(c.id), 'collection_name': c.name} for c in cols]


def _norm(nome):
    return (nome or '').strip().casefold()


def match_pastas_ativas(pastas_config, collections):
    """Casa as pastas do config pelo nome com as coleções reais da conta (sem diferenciar
    maiúsculas/minúsculas nem espaços nas pontas — o Instagram não é consistente com isso).
    Avisa (não quebra) se não achar."""
    by_name = {_norm(c.get('collection_name')): str(c.get('collection_id')) for c in collections}
    matched = []
    for p in pastas_config:
        nome = p.get('nome')
        cid = by_name.get(_norm(nome))
        if cid:
            matched.append({'nome': nome, 'angulo': p.get('angulo', ''), 'collection_id': cid})
        else:
            print(f'  ! Pasta "{nome}" configurada em instagram-pastas.json mas não encontrada nas coleções da conta — pulando.')
    return matched


def get_collection_posts(collection_id):
    # ponytail: amount=50 cobre coleções pequenas/médias sem paginação manual;
    # ampliar se uma coleção passar disso sem sincronizar tudo.
    try:
        medias = _get_client().collection_medias(str(collection_id), amount=50)
    except Exception as e:
        print(f'Erro ao buscar posts da coleção {collection_id}: {e}')
        return []
    return [_media_to_dict(m) for m in medias]


def get_media_id(post):
    media = post.get('media', post)
    return str(media.get('pk', media.get('id', '')))


def save_to_notion(post, pasta_nome):
    media = post.get('media', post)
    media_id = get_media_id(post)
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
            'pasta':       {'select': {'name': pasta_nome}},
            'status':      {'select': {'name': 'Novo'}},
            'saved':       {'date': {'start': saved_date}},
        }
    )


def run_sync():
    print(f'[{datetime.now().strftime("%H:%M:%S")}] Iniciando sincronização...')
    existing = get_existing_ids()
    print(f'Posts já no Notion: {len(existing)}')

    pastas = match_pastas_ativas(load_pastas_config(), list_collections())
    if not pastas:
        print('Nenhuma pasta configurada foi encontrada nas coleções da conta. Nada a sincronizar.')
        return

    total = 0
    for pasta in pastas:
        print(f'Coleção "{pasta["nome"]}"...')
        posts = get_collection_posts(pasta['collection_id'])
        print(f'  Posts na coleção: {len(posts)}')
        for post in posts:
            media_id = get_media_id(post)
            if not media_id or media_id in existing:
                continue
            try:
                save_to_notion(post, pasta['nome'])
                existing.add(media_id)
                total += 1
                print(f'  + Adicionado: {media_id} [{pasta["nome"]}]')
            except Exception as e:
                print(f'  ! Erro no post {media_id}: {e}')
    print(f'Concluído! {total} novos posts adicionados.')


def get_posts_missing_pasta():
    """Posts no Notion cujo campo 'pasta' ainda está vazio: [(page_id, post_id), ...]."""
    results = []
    cursor = None
    while True:
        params = {'start_cursor': cursor} if cursor else {}
        res = notion.databases.query(
            database_id=DB_ID,
            filter={'property': 'pasta', 'select': {'is_empty': True}},
            **params
        )
        for r in res['results']:
            try:
                post_id = r['properties']['post_id']['title'][0]['text']['content']
                results.append((r['id'], post_id))
            except Exception:
                pass
        if not res.get('has_more'):
            break
        cursor = res.get('next_cursor')
    return results


def run_backfill():
    """Para posts já existentes no Notion sem 'pasta', tenta casar o post_id contra
    as coleções ativas e atualiza o campo (em vez de processar posts novos)."""
    print(f'[{datetime.now().strftime("%H:%M:%S")}] Backfill do campo "pasta"...')
    pastas = match_pastas_ativas(load_pastas_config(), list_collections())
    if not pastas:
        print('Nenhuma pasta configurada foi encontrada nas coleções da conta. Backfill abortado.')
        return

    post_to_pasta = {}
    for pasta in pastas:
        for post in get_collection_posts(pasta['collection_id']):
            media_id = get_media_id(post)
            if media_id and media_id not in post_to_pasta:
                post_to_pasta[media_id] = pasta['nome']

    pendentes = get_posts_missing_pasta()
    print(f'Posts sem "pasta" no Notion: {len(pendentes)}')
    total = 0
    for page_id, post_id in pendentes:
        nome = post_to_pasta.get(post_id)
        if not nome:
            print(f'  - {post_id}: não encontrado em nenhuma coleção ativa, pulando.')
            continue
        try:
            notion.pages.update(page_id=page_id, properties={'pasta': {'select': {'name': nome}}})
            total += 1
            print(f'  + {post_id} -> {nome}')
        except Exception as e:
            print(f'  ! Erro ao atualizar {post_id}: {e}')
    print(f'Concluído! {total} posts atualizados.')


def _selftest():
    assert get_media_id({'media': {'pk': 123}}) == '123'
    assert get_media_id({'pk': 456}) == '456'
    assert get_media_id({}) == ''

    matched = match_pastas_ativas(
        [{'nome': 'Claude', 'angulo': 'x'}, {'nome': 'Nao Existe', 'angulo': 'y'}],
        [{'collection_id': 111, 'collection_name': 'Claude'}]
    )
    assert len(matched) == 1 and matched[0]['collection_id'] == '111' and matched[0]['angulo'] == 'x'
    print('OK — selftest passou.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sincroniza posts salvos do Instagram (por coleção) com o Notion.')
    parser.add_argument('--backfill', action='store_true',
                         help='Preenche o campo "pasta" de posts já existentes no Notion que ainda não têm esse campo.')
    parser.add_argument('--selftest', action='store_true', help='Roda checagens offline (sem chamar Instagram/Notion) e sai.')
    args = parser.parse_args()

    if args.selftest:
        _selftest()
    elif args.backfill:
        run_backfill()
    else:
        run_sync()
