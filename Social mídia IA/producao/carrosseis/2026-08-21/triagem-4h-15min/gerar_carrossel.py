"""
Carrossel estático — "triagem-4h-15min" (8 lâminas, módulo 15).
Evoluído de ig-saves-engine/create_image.py + o padrão já usado no módulo 16
(producao/criativos/2026-08-21/leads-perdidos-custo/gerar_criativo.py):
paleta e tipografia = branding/neovertix/tokens.json, Pillow-first, zero IA de imagem.

Texto de cada lâmina é literal do roteiro aprovado (score_iana 7,5) — ver
roteiro-laminas.md. Requer: pip install Pillow
"""
import os
from PIL import Image, ImageDraw, ImageFont

LARGURA, ALTURA = 1080, 1350  # 4:5 — padrão de carrossel Instagram

# ponytail: paleta e fontes puxadas de branding/neovertix/tokens.json —
# atualizar aqui se os tokens mudarem
BG_COLOR = (10, 14, 26)        # #0A0E1A — color.bg.canvas
TX_COLOR = (245, 247, 250)     # #F5F7FA — color.text.primary
TX_MUTED = (170, 180, 194)     # #AAB4C2 — color.text.secondary
TX_DIM = (122, 134, 153)       # #7A8699 — color.text.muted
AC_COLOR = (67, 160, 71)       # #43A047 — color.accent.default
BORDER_SUBTLE = (24, 33, 58)   # #18213A — color.border.subtle

FONT_DIR = os.path.normpath(os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "..", "..",
    ".agents", "skills", "ckm-ui-styling", "canvas-fonts",
))
# ponytail: Chakra Petch / Manrope não instaladas no ambiente — mesmos
# substitutos vendorizados já usados no criativo do módulo 16 (mesma paleta,
# mesma decisão registrada lá). Trocar por Chakra Petch/Manrope reais se/quando
# disponíveis.
F_DISPLAY = os.path.join(FONT_DIR, "BigShoulders-Bold.ttf")   # display (Chakra Petch)
F_BODY = os.path.join(FONT_DIR, "WorkSans-Regular.ttf")       # texto (Manrope)
F_MONO = os.path.join(FONT_DIR, "JetBrainsMono-Bold.ttf")     # mono (token real)

MARGIN_X = 100


def _wrap(draw, text, font, max_width):
    """Quebra texto em linhas que cabem em max_width, medindo pixel real."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def _draw_centered(draw, text, font, y, fill, tracking=0):
    if tracking:
        widths = [draw.textlength(ch, font=font) for ch in text]
        total = sum(widths) + tracking * (len(text) - 1)
        x = (LARGURA - total) / 2
        for ch, w in zip(text, widths):
            draw.text((x, y), ch, font=font, fill=fill)
            x += w + tracking
        return y
    w = draw.textlength(text, font=font)
    draw.text(((LARGURA - w) / 2, y), text, font=font, fill=fill)
    return y


def _draw_block(draw, lines, font, y, fill, line_height, align_center=True):
    """Desenha um bloco de linhas já quebradas, retorna o y final."""
    for line in lines:
        if align_center:
            _draw_centered(draw, line, font, y, fill)
        else:
            draw.text((MARGIN_X, y), line, font=font, fill=fill)
        y += line_height
    return y


def _page_counter(draw, idx, total, f_mono):
    label = f"{idx:02d} / {total:02d}"
    draw.text((MARGIN_X, ALTURA - 90), label, font=f_mono, fill=TX_DIM)
    # barra de progresso mínima (mesma linguagem visual em todas as lâminas)
    bar_w = LARGURA - 2 * MARGIN_X
    draw.rectangle([MARGIN_X, ALTURA - 40, MARGIN_X + bar_w, ALTURA - 36], fill=BORDER_SUBTLE)
    filled = bar_w * idx / total
    draw.rectangle([MARGIN_X, ALTURA - 40, MARGIN_X + filled, ALTURA - 36], fill=AC_COLOR)


def _clock_parado(draw, cx, cy, r):
    """Ícone geométrico simples: relógio com ponteiros parados (estado 'antes')."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=TX_MUTED, width=6)
    draw.line([cx, cy, cx, cy - r * 0.6], fill=TX_MUTED, width=6)
    draw.line([cx, cy, cx + r * 0.35, cy - r * 0.5], fill=TX_MUTED, width=6)
    draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=TX_MUTED)


def _fila_parada(draw, cx, cy, r, n=5):
    """Ícone geométrico simples: fila de pontos parada (estado 'antes')."""
    spacing = r * 3
    start_x = cx - spacing * (n - 1) / 2
    for i in range(n):
        x = start_x + i * spacing
        color = TX_MUTED if i > 0 else AC_COLOR if False else TX_MUTED
        draw.ellipse([x - r, cy - r, x + r, cy + r], outline=color, width=5)


def _fluxo_numerado(draw, cx, cy, r, numero, f_display):
    """Ícone geométrico simples: círculo numerado + seta (estado 'depois')."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=AC_COLOR)
    num_font = ImageFont.truetype(f_display, int(r * 1.1))
    tb = draw.textbbox((0, 0), numero, font=num_font)
    nw, nh = tb[2] - tb[0], tb[3] - tb[1]
    draw.text((cx - nw / 2 - tb[0], cy - nh / 2 - tb[1]), numero, font=num_font, fill=BG_COLOR)
    # seta pra direita, indicando continuidade do fluxo
    ax = cx + r + 30
    draw.line([ax, cy, ax + 90, cy], fill=AC_COLOR, width=6)
    draw.polygon([(ax + 90, cy - 14), (ax + 90, cy + 14), (ax + 116, cy)], fill=AC_COLOR)


def _balao_comentario(draw, cx, cy, w, h, texto, f_display):
    """Balão de comentário geométrico (não é ícone de robô) com a palavra CTA dentro."""
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    draw.rounded_rectangle([x0, y0, x1, y1], radius=28, outline=AC_COLOR, width=6)
    draw.polygon([(cx - 30, y1), (cx + 10, y1), (cx - 10, y1 + 40)], fill=BG_COLOR, outline=AC_COLOR, width=6)
    draw.polygon([(cx - 28, y1 - 2), (cx + 8, y1 - 2), (cx - 12, y1 + 34)], fill=AC_COLOR)
    font = ImageFont.truetype(f_display, 74)
    tb = draw.textbbox((0, 0), texto, font=font)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    draw.text((cx - tw / 2 - tb[0], cy - th / 2 - tb[1]), texto, font=font, fill=AC_COLOR)


def _canvas():
    img = Image.new("RGB", (LARGURA, ALTURA), BG_COLOR)
    return img, ImageDraw.Draw(img)


def lamina_1_capa(f):
    img, draw = _canvas()
    f_display = ImageFont.truetype(F_DISPLAY, 88)
    f_accent = ImageFont.truetype(F_DISPLAY, 100)
    y = 420
    y = _draw_block(draw, ["Sua equipe leva"], f_display, y, TX_COLOR, 100)
    y = _draw_block(draw, ["4 HORAS"], f_accent, y, AC_COLOR, 112)
    y = _draw_block(draw, ["pra responder", "um lead."], f_display, y, TX_COLOR, 100)
    y += 40
    f_display_sm = ImageFont.truetype(F_DISPLAY, 64)
    y = _draw_block(draw, ["O concorrente", "respondeu"], f_display_sm, y, TX_MUTED, 76)
    _draw_block(draw, ["EM SEGUNDOS."], ImageFont.truetype(F_DISPLAY, 78), y, AC_COLOR, 88)
    _page_counter(draw, 1, 8, ImageFont.truetype(F_MONO, 26))
    img.save(f)


def lamina_2_emocao(f):
    img, draw = _canvas()
    f_body = ImageFont.truetype(F_BODY, 54)
    f_overline = ImageFont.truetype(F_MONO, 30)
    f_number = ImageFont.truetype(F_DISPLAY, 92)
    f_caption = ImageFont.truetype(F_BODY, 38)

    lines = _wrap(draw, "Ele não espera a fila andar — testa quem responder primeiro.",
                  f_body, LARGURA - 2 * MARGIN_X)
    y = 220
    y = _draw_block(draw, lines, f_body, y, TX_COLOR, 70)
    y += 90
    _draw_centered(draw, "CUSTO DA DEMORA / MÊS", f_overline, y, AC_COLOR, tracking=4)
    y += 90
    y = _draw_block(draw, ["R$ 3.000"], f_number, y, TX_COLOR, 100)
    y = _draw_block(draw, ["A R$ 15.000"], f_number, y, TX_COLOR, 100)
    y += 30
    _draw_block(draw, ["10 leads perdidos por demora"], f_caption, y, TX_MUTED, 46)
    _page_counter(draw, 2, 8, ImageFont.truetype(F_MONO, 26))
    img.save(f)


def lamina_antes(f, idx, texto, icone):
    img, draw = _canvas()
    f_overline = ImageFont.truetype(F_MONO, 32)
    f_body = ImageFont.truetype(F_BODY, 58)
    _draw_centered(draw, "ANTES", f_overline, 180, TX_MUTED, tracking=8)
    icone(draw, LARGURA / 2, 420, 70)
    lines = _wrap(draw, texto, f_body, LARGURA - 2 * MARGIN_X)
    y = 640
    _draw_block(draw, lines, f_body, y, TX_COLOR, 78)
    _page_counter(draw, idx, 8, ImageFont.truetype(F_MONO, 26))
    img.save(f)


def lamina_depois(f, idx, numero, texto, payoff=None):
    img, draw = _canvas()
    f_overline = ImageFont.truetype(F_MONO, 32)
    f_body = ImageFont.truetype(F_BODY, 58)
    f_payoff = ImageFont.truetype(F_DISPLAY, 72)
    _draw_centered(draw, f"DEPOIS · {numero}", f_overline, 180, AC_COLOR, tracking=8)
    _fluxo_numerado(draw, LARGURA / 2 - 60, 420, 64, numero, F_DISPLAY)
    lines = _wrap(draw, texto, f_body, LARGURA - 2 * MARGIN_X)
    y = 640
    y = _draw_block(draw, lines, f_body, y, TX_COLOR, 78)
    if payoff:
        y += 50
        payoff_lines = _wrap(draw, payoff, f_payoff, LARGURA - 2 * MARGIN_X)
        _draw_block(draw, payoff_lines, f_payoff, y, AC_COLOR, 84)
    _page_counter(draw, idx, 8, ImageFont.truetype(F_MONO, 26))
    img.save(f)


def lamina_7_prova(f):
    img, draw = _canvas()
    f_overline = ImageFont.truetype(F_MONO, 32)
    f_body = ImageFont.truetype(F_BODY, 56)
    f_accent = ImageFont.truetype(F_DISPLAY, 64)
    _draw_centered(draw, "PILOTO VÉRTICE", f_overline, 220, AC_COLOR, tracking=6)
    y = 340
    y = _draw_block(draw, _wrap(draw, "2 a 4 semanas", f_accent, LARGURA - 2 * MARGIN_X),
                     f_accent, y, AC_COLOR, 84)
    y += 40
    resto = ("rodando com os dados da sua operação, com a métrica de tempo de "
             "resposta combinada antes de começar — semanas, não trimestre.")
    lines = _wrap(draw, resto, f_body, LARGURA - 2 * MARGIN_X)
    _draw_block(draw, lines, f_body, y, TX_COLOR, 74)
    _page_counter(draw, 7, 8, ImageFont.truetype(F_MONO, 26))
    img.save(f)


def lamina_8_cta(f):
    img, draw = _canvas()
    f_overline = ImageFont.truetype(F_MONO, 30)
    f_body = ImageFont.truetype(F_BODY, 54)
    _draw_centered(draw, "COMENTA AQUI EMBAIXO", f_overline, 170, TX_MUTED, tracking=6)
    _balao_comentario(draw, LARGURA / 2, 460, 720, 260, "TRIAGEM", F_DISPLAY)
    resto = "Te chamo no direct e monto esse fluxo com os números da sua operação, ao vivo."
    lines = _wrap(draw, resto, f_body, LARGURA - 2 * MARGIN_X)
    _draw_block(draw, lines, f_body, 720, TX_COLOR, 74)
    _page_counter(draw, 8, 8, ImageFont.truetype(F_MONO, 26))
    img.save(f)


def gerar_carrossel(output_dir: str) -> list:
    os.makedirs(output_dir, exist_ok=True)
    caminhos = []

    def path(n):
        p = os.path.join(output_dir, f"lamina-{n}.png")
        caminhos.append(p)
        return p

    lamina_1_capa(path(1))
    lamina_2_emocao(path(2))
    lamina_antes(path(3), 3,
                 "A mensagem chega e fica parada até alguém sair de outra ligação.",
                 _clock_parado)
    lamina_antes(path(4), 4,
                 "Quando alguém finalmente abre o CRM, já se passaram 4 horas — e "
                 "o lead quente esfriou junto com o resto da fila.",
                 _fila_parada)
    lamina_depois(path(5), "1",
                  "O agente lê a mensagem no segundo em que ela chega e consulta "
                  "o CRM sozinho — histórico, se já é cliente, o que já foi combinado.")
    lamina_depois(path(6), "2",
                  "Responde com esse histórico na mão e sobe pro topo da fila "
                  "quem já pediu orçamento.",
                  payoff="4 horas de triagem viram 15 minutos.")
    lamina_7_prova(path(7))
    lamina_8_cta(path(8))
    return caminhos


if __name__ == "__main__":
    caminhos = gerar_carrossel(os.path.dirname(__file__))
    for c in caminhos:
        print(f"Lâmina gerada: {c}")
