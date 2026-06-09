"""
Gera uma imagem simples com o Hook da ideia para postar no Instagram.
Requer: pip install Pillow
"""
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

LARGURA  = 1080
ALTURA   = 1080
BG_COLOR = (15, 15, 15)       # fundo preto
TX_COLOR = (255, 255, 255)    # texto branco
AC_COLOR = (99, 102, 241)     # roxo (destaque)

def criar_imagem(hook: str, titulo: str, output_path: str = "post.jpg") -> str:
    img  = Image.new("RGB", (LARGURA, ALTURA), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # barra lateral colorida
    draw.rectangle([0, 0, 12, ALTURA], fill=AC_COLOR)

    # tenta carregar fonte; usa padrão se não encontrar
    try:
        fonte_titulo = ImageFont.truetype("arial.ttf", 52)
        fonte_hook   = ImageFont.truetype("arialbd.ttf", 72)
        fonte_rodape = ImageFont.truetype("arial.ttf", 36)
    except Exception:
        fonte_titulo = ImageFont.load_default()
        fonte_hook   = fonte_titulo
        fonte_rodape = fonte_titulo

    # título pequeno no topo
    draw.text((80, 120), titulo[:60], font=fonte_titulo, fill=AC_COLOR)

    # hook centralizado (quebra em linhas)
    linhas = textwrap.wrap(hook, width=22)
    y = 340
    for linha in linhas:
        draw.text((80, y), linha, font=fonte_hook, fill=TX_COLOR)
        y += 100

    # rodapé
    draw.text((80, 920), "@lukashonorato09", font=fonte_rodape, fill=(150, 150, 150))

    img.save(output_path, "JPEG", quality=95)
    return output_path


if __name__ == "__main__":
    caminho = criar_imagem(
        hook="IA que cria Reels sozinha enquanto você dorme",
        titulo="Teste de imagem",
        output_path="test_post.jpg"
    )
    print(f"Imagem gerada: {caminho}")
