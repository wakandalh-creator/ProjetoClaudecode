"""
Criativo de imagem — "leads-perdidos-custo" (reel, capa/gancho on-screen).
Evoluído de ig-saves-engine/create_image.py: paleta e tipografia trocadas
pelos tokens reais de branding/neovertix/tokens.json (módulo 16).

Peça tipográfica pura (número âncora em destaque) -> Pillow, sem IA de imagem.
Requer: pip install Pillow
"""
import os
from PIL import Image, ImageDraw, ImageFont

LARGURA, ALTURA = 1080, 1920  # 9:16 — capa de reel

# ponytail: paleta e fontes puxadas de branding/neovertix/tokens.json —
# atualizar aqui se os tokens mudarem
BG_COLOR = (10, 14, 26)        # #0A0E1A — color.bg.canvas
TX_COLOR = (245, 247, 250)     # #F5F7FA — color.text.primary
TX_MUTED = (170, 180, 194)     # #AAB4C2 — color.text.secondary
AC_COLOR = (67, 160, 71)       # #43A047 — color.accent.default

FONT_DIR = os.path.normpath(os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "..", "..",
    ".agents", "skills", "ckm-ui-styling", "canvas-fonts",
))
# ponytail: Chakra Petch / Manrope não estão instaladas no ambiente — uso as
# substitutas vendorizadas mais próximas (condensada/geométrica e humanista
# neutra). Trocar por Chakra Petch/Manrope reais se/quando instaladas.
F_DISPLAY = os.path.join(FONT_DIR, "BigShoulders-Bold.ttf")   # display (Chakra Petch)
F_BODY = os.path.join(FONT_DIR, "WorkSans-Regular.ttf")       # texto (Manrope)
F_MONO = os.path.join(FONT_DIR, "JetBrainsMono-Bold.ttf")     # mono (token real)


def _center_text(draw, text, font, y, fill, tracking=0):
    """Desenha uma linha centralizada horizontalmente; suporta letter-spacing simples."""
    if tracking:
        widths = [draw.textbbox((0, 0), ch, font=font)[2] for ch in text]
        total = sum(widths) + tracking * (len(text) - 1)
        x = (LARGURA - total) / 2
        for ch, w in zip(text, widths):
            draw.text((x, y), ch, font=font, fill=fill)
            x += w + tracking
        return
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((LARGURA - w) / 2, y), text, font=font, fill=fill)


def criar_criativo(output_path: str) -> str:
    img = Image.new("RGB", (LARGURA, ALTURA), BG_COLOR)
    draw = ImageDraw.Draw(img)

    f_overline = ImageFont.truetype(F_MONO, 34)
    f_number = ImageFont.truetype(F_DISPLAY, 168)
    f_number_small = ImageFont.truetype(F_DISPLAY, 96)
    f_body = ImageFont.truetype(F_BODY, 46)
    f_caption = ImageFont.truetype(F_MONO, 28)

    # eyebrow — contexto pra âncora não ficar solta fora do vídeo
    _center_text(draw, "10 LEADS PERDIDOS CUSTAM", f_overline, 300, AC_COLOR, tracking=6)

    # número âncora (marca.md: R$ 3.000-15.000/mês — não inventado)
    _center_text(draw, "R$ 3.000", f_number, 420, TX_COLOR)
    _center_text(draw, "A R$ 15.000", f_number, 610, TX_COLOR)
    _center_text(draw, "POR MÊS", f_number_small, 830, TX_COLOR)

    # barra de destaque — única cor de acento da peça
    bar_w, bar_h = 120, 8
    draw.rectangle(
        [(LARGURA - bar_w) / 2, 1010, (LARGURA + bar_w) / 2, 1010 + bar_h],
        fill=AC_COLOR,
    )

    # linha de apoio
    _center_text(draw, "em receita perdida por demora", f_body, 1080, TX_MUTED)
    _center_text(draw, "no atendimento", f_body, 1140, TX_MUTED)

    # assinatura discreta
    _center_text(draw, "neovertix", f_caption, ALTURA - 120, TX_MUTED, tracking=4)

    img.save(output_path, "PNG")
    return output_path


if __name__ == "__main__":
    caminho = criar_criativo(
        os.path.join(os.path.dirname(__file__), "capa-reel.png")
    )
    print(f"Criativo gerado: {caminho}")
