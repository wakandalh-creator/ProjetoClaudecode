"""
Carrossel estático — "triagem-4h-15min" (8 lâminas, módulo 15) — V2.

Iteração de design sobre gerar_carrossel.py (v1) a partir do feedback do Lucas:
"gostei, mas quero mais vivo e mais claro". Texto de cada lâmina continua
100% literal do roteiro aprovado (score_iana 7,5) — nada de copy mudou aqui,
só diagramação. Ver roteiro-laminas.md (pasta pai) para o texto de origem.

O que muda de concreto na v2 (ver detalhamento por função):
- "Mais vivo": accent.default (#43A047) passa a preencher formas (círculo,
  balão) em vez de só contornar, e ganha um glow (aproximação em Pillow do
  token shadow.glow-accent — blur gaussiano de uma camada verde translúcida)
  atrás de todo número/frase-chave.
- "Mais claro": 1 elemento dominante por lâmina, sensivelmente maior que no
  v1; texto de apoio migra pra weight mais leve (Work Sans regular, cor
  secundária) pra criar contraste de peso real com o elemento principal —
  não só contraste de cor.

Requer: pip install Pillow
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

LARGURA, ALTURA = 1080, 1350  # 4:5 — padrão de carrossel Instagram

# ponytail: paleta e fontes puxadas de branding/neovertix/tokens.json —
# atualizar aqui se os tokens mudarem
BG_COLOR = (10, 14, 26)          # #0A0E1A — color.bg.canvas
SURFACE_RAISED = (26, 36, 64)    # #1A2440 — color.surface.raised (backing sutil de ícone)
TX_COLOR = (245, 247, 250)       # #F5F7FA — color.text.primary
TX_MUTED = (170, 180, 194)       # #AAB4C2 — color.text.secondary
TX_DIM = (122, 134, 153)         # #7A8699 — color.text.muted
AC_COLOR = (67, 160, 71)         # #43A047 — color.accent.default
AC_CONTRAST = (18, 26, 46)       # #121A2E — color.accent.contrast (texto sobre fill de accent)
BORDER_SUBTLE = (24, 33, 58)     # #18213A — color.border.subtle

FONT_DIR = os.path.normpath(os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "..", "..", "..",
    ".agents", "skills", "ckm-ui-styling", "canvas-fonts",
))
# ponytail: Chakra Petch / Manrope não instaladas no ambiente — mesmos
# substitutos vendorizados já usados no v1 (mesma decisão registrada lá).
F_DISPLAY = os.path.join(FONT_DIR, "BigShoulders-Bold.ttf")   # display (Chakra Petch)
F_BODY = os.path.join(FONT_DIR, "WorkSans-Regular.ttf")       # texto (Manrope)
F_MONO = os.path.join(FONT_DIR, "JetBrainsMono-Bold.ttf")     # mono (token real)

MARGIN_X = 100


def _wrap(draw, text, font, max_width):
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
    for line in lines:
        if align_center:
            _draw_centered(draw, line, font, y, fill)
        else:
            draw.text((MARGIN_X, y), line, font=font, fill=fill)
        y += line_height
    return y


def _block_width(draw, lines, font):
    return max((draw.textlength(line, font=font) for line in lines), default=0)


def _page_counter(draw, idx, total, f_mono):
    label = f"{idx:02d} / {total:02d}"
    draw.text((MARGIN_X, ALTURA - 90), label, font=f_mono, fill=TX_DIM)
    bar_w = LARGURA - 2 * MARGIN_X
    draw.rectangle([MARGIN_X, ALTURA - 40, MARGIN_X + bar_w, ALTURA - 36], fill=BORDER_SUBTLE)
    filled = bar_w * idx / total
    draw.rectangle([MARGIN_X, ALTURA - 40, MARGIN_X + filled, ALTURA - 36], fill=AC_COLOR)


def _glow(img, cx, cy, w, h, blur=55, alpha=140):
    """Aproximação em Pillow do token shadow.glow-accent (blur gaussiano de
    uma camada verde translúcida atrás do elemento principal). Muta `img`
    in-place — pode ser chamada antes de continuar desenhando com o mesmo
    objeto ImageDraw."""
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(overlay).ellipse(
        [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2],
        fill=AC_COLOR + (alpha,),
    )
    overlay = overlay.filter(ImageFilter.GaussianBlur(blur))
    img.paste(overlay, (0, 0), overlay)


def _clock_parado(draw, cx, cy, r):
    """Ícone geométrico: relógio com ponteiros parados (estado 'antes').
    v2: disco de apoio em surface.raised atrás do contorno (mais presença
    sem introduzir uma segunda cor de destaque) + traço mais grosso."""
    draw.ellipse([cx - r - 24, cy - r - 24, cx + r + 24, cy + r + 24], fill=SURFACE_RAISED)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=TX_MUTED, width=9)
    draw.line([cx, cy, cx, cy - r * 0.6], fill=TX_MUTED, width=9)
    draw.line([cx, cy, cx + r * 0.35, cy - r * 0.5], fill=TX_MUTED, width=9)
    draw.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=TX_MUTED)


def _fila_parada(draw, cx, cy, r, n=5):
    """Ícone geométrico: fila de pontos parada (estado 'antes'). v2: disco
    de apoio em surface.raised atrás da fila + traço mais grosso."""
    spacing = r * 3
    start_x = cx - spacing * (n - 1) / 2
    draw.rounded_rectangle(
        [start_x - r - 24, cy - r - 24, start_x + spacing * (n - 1) + r + 24, cy + r + 24],
        radius=r + 24, fill=SURFACE_RAISED,
    )
    for i in range(n):
        x = start_x + i * spacing
        draw.ellipse([x - r, cy - r, x + r, cy + r], outline=TX_MUTED, width=8)


def _fluxo_numerado(draw, cx, cy, r, numero, f_display):
    """Ícone geométrico: círculo numerado + seta (estado 'depois'). v2:
    círculo maior — já era fill sólido de accent, o glow (aplicado por fora,
    antes de chamar esta função) que faltava pra dar presença real."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=AC_COLOR)
    num_font = ImageFont.truetype(f_display, int(r * 1.1))
    tb = draw.textbbox((0, 0), numero, font=num_font)
    nw, nh = tb[2] - tb[0], tb[3] - tb[1]
    draw.text((cx - nw / 2 - tb[0], cy - nh / 2 - tb[1]), numero, font=num_font, fill=BG_COLOR)
    ax = cx + r + 36
    draw.line([ax, cy, ax + 110, cy], fill=AC_COLOR, width=8)
    draw.polygon([(ax + 110, cy - 18), (ax + 110, cy + 18), (ax + 142, cy)], fill=AC_COLOR)


def _balao_comentario(draw, cx, cy, w, h, texto, f_display):
    """Balão de comentário. v2: preenchido sólido em accent (token
    accent.contrast pro texto dentro, exatamente o par pra que o token
    existe) em vez de só contorno — o CTA vira o elemento mais 'vivo' da
    lâmina."""
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    draw.rounded_rectangle([x0, y0, x1, y1], radius=32, fill=AC_COLOR)
    draw.polygon([(cx - 34, y1 - 2), (cx + 12, y1 - 2), (cx - 14, y1 + 46)], fill=AC_COLOR)
    font = ImageFont.truetype(f_display, 92)
    tb = draw.textbbox((0, 0), texto, font=font)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    draw.text((cx - tw / 2 - tb[0], cy - th / 2 - tb[1]), texto, font=font, fill=AC_CONTRAST)


def _canvas():
    img = Image.new("RGB", (LARGURA, ALTURA), BG_COLOR)
    return img, ImageDraw.Draw(img)


def lamina_1_capa(f):
    img, draw = _canvas()
    f_lead = ImageFont.truetype(F_BODY, 46)       # texto de apoio: leve, secundário
    f_hero = ImageFont.truetype(F_DISPLAY, 176)   # "4 HORAS": elemento dominante da lâmina
    f_sub = ImageFont.truetype(F_BODY, 42)
    f_sec_accent = ImageFont.truetype(F_DISPLAY, 96)  # "EM SEGUNDOS": accent, mas claramente 2º

    hero_lines = ["4 HORAS"]
    hero_w = _block_width(draw, hero_lines, f_hero)
    _glow(img, LARGURA / 2, 470, hero_w + 140, 280, blur=60, alpha=130)
    draw = ImageDraw.Draw(img)  # reataca o mesmo buffer após o paste do glow

    y = 190
    y = _draw_block(draw, ["Sua equipe leva"], f_lead, y, TX_MUTED, 64)
    y += 20
    y = _draw_block(draw, hero_lines, f_hero, y, AC_COLOR, 188)
    y += 30
    y = _draw_block(draw, _wrap(draw, "pra responder um lead.", f_lead, LARGURA - 2 * MARGIN_X),
                     f_lead, y, TX_MUTED, 64)
    y += 70
    y = _draw_block(draw, _wrap(draw, "O concorrente respondeu", f_sub, LARGURA - 2 * MARGIN_X),
                     f_sub, y, TX_DIM, 58)
    y += 10
    _draw_block(draw, ["EM SEGUNDOS."], f_sec_accent, y, AC_COLOR, 104)
    _page_counter(draw, 1, 8, ImageFont.truetype(F_MONO, 26))
    img.save(f)


def lamina_2_emocao(f):
    img, draw = _canvas()
    f_body = ImageFont.truetype(F_BODY, 44)
    f_overline = ImageFont.truetype(F_MONO, 32)
    f_number = ImageFont.truetype(F_DISPLAY, 158)  # dado que dói: elemento dominante
    f_caption = ImageFont.truetype(F_BODY, 42)

    lines = _wrap(draw, "Ele não espera a fila andar — testa quem responder primeiro.",
                  f_body, LARGURA - 2 * MARGIN_X)
    y = 190
    y = _draw_block(draw, lines, f_body, y, TX_MUTED, 62)
    y += 80
    _draw_centered(draw, "CUSTO DA DEMORA / MÊS", f_overline, y, AC_COLOR, tracking=4)
    y += 100

    num_lines = ["R$ 3.000", "A R$ 15.000"]
    num_w = _block_width(draw, num_lines, f_number)
    _glow(img, LARGURA / 2, y + 340, num_w + 160, 480, blur=70, alpha=120)
    draw = ImageDraw.Draw(img)

    y = _draw_block(draw, num_lines, f_number, y, AC_COLOR, 176)
    y += 40
    _draw_block(draw, ["10 leads perdidos por demora"], f_caption, y, TX_MUTED, 46)
    _page_counter(draw, 2, 8, ImageFont.truetype(F_MONO, 26))
    img.save(f)


def lamina_antes(f, idx, texto, icone):
    img, draw = _canvas()
    f_overline = ImageFont.truetype(F_MONO, 32)
    f_body = ImageFont.truetype(F_BODY, 62)
    _draw_centered(draw, "ANTES", f_overline, 180, TX_MUTED, tracking=8)
    icone(draw, LARGURA / 2, 470, 118)
    lines = _wrap(draw, texto, f_body, LARGURA - 2 * MARGIN_X)
    y = 720
    _draw_block(draw, lines, f_body, y, TX_COLOR, 84)
    _page_counter(draw, idx, 8, ImageFont.truetype(F_MONO, 26))
    img.save(f)


def lamina_depois(f, idx, numero, texto, payoff=None):
    img, draw = _canvas()
    f_overline = ImageFont.truetype(F_MONO, 32)
    f_body = ImageFont.truetype(F_BODY, 50)
    f_payoff = ImageFont.truetype(F_DISPLAY, 104)  # payoff é o dado dominante quando existe

    _draw_centered(draw, f"DEPOIS · {numero}", f_overline, 180, AC_COLOR, tracking=8)

    cx, cy, r = LARGURA / 2 - 90, 470, 108
    _glow(img, cx, cy, r * 2.8, r * 2.8, blur=55, alpha=130)
    draw = ImageDraw.Draw(img)
    _fluxo_numerado(draw, cx, cy, r, numero, F_DISPLAY)

    lines = _wrap(draw, texto, f_body, LARGURA - 2 * MARGIN_X)
    y = 700
    y = _draw_block(draw, lines, f_body, y, TX_COLOR, 68)
    if payoff:
        y += 60
        payoff_lines = _wrap(draw, payoff, f_payoff, LARGURA - 2 * MARGIN_X)
        payoff_w = _block_width(draw, payoff_lines, f_payoff)
        _glow(img, LARGURA / 2, y + len(payoff_lines) * 58, payoff_w + 140,
              len(payoff_lines) * 130 + 100, blur=60, alpha=120)
        draw = ImageDraw.Draw(img)
        _draw_block(draw, payoff_lines, f_payoff, y, AC_COLOR, 116)
    _page_counter(draw, idx, 8, ImageFont.truetype(F_MONO, 26))
    img.save(f)


def lamina_7_prova(f):
    img, draw = _canvas()
    f_overline = ImageFont.truetype(F_MONO, 32)
    f_body = ImageFont.truetype(F_BODY, 46)
    f_accent = ImageFont.truetype(F_DISPLAY, 128)  # elemento dominante da lâmina

    _draw_centered(draw, "PILOTO VÉRTICE", f_overline, 220, AC_COLOR, tracking=6)
    y = 320
    accent_lines = _wrap(draw, "2 a 4 semanas", f_accent, LARGURA - 2 * MARGIN_X)
    accent_w = _block_width(draw, accent_lines, f_accent)
    _glow(img, LARGURA / 2, y + len(accent_lines) * 65, accent_w + 140,
          len(accent_lines) * 140 + 80, blur=60, alpha=125)
    draw = ImageDraw.Draw(img)
    y = _draw_block(draw, accent_lines, f_accent, y, AC_COLOR, 138)
    y += 70
    resto = ("rodando com os dados da sua operação, com a métrica de tempo de "
             "resposta combinada antes de começar — semanas, não trimestre.")
    lines = _wrap(draw, resto, f_body, LARGURA - 2 * MARGIN_X)
    _draw_block(draw, lines, f_body, y, TX_MUTED, 62)
    _page_counter(draw, 7, 8, ImageFont.truetype(F_MONO, 26))
    img.save(f)


def lamina_8_cta(f):
    img, draw = _canvas()
    f_overline = ImageFont.truetype(F_MONO, 30)
    f_body = ImageFont.truetype(F_BODY, 46)

    _draw_centered(draw, "COMENTA AQUI EMBAIXO", f_overline, 170, TX_MUTED, tracking=6)

    bw, bh = 800, 300
    bcx, bcy = LARGURA / 2, 490
    _glow(img, bcx, bcy, bw + 160, bh + 160, blur=65, alpha=110)
    draw = ImageDraw.Draw(img)
    _balao_comentario(draw, bcx, bcy, bw, bh, "TRIAGEM", F_DISPLAY)

    resto = "Te chamo no direct e monto esse fluxo com os números da sua operação, ao vivo."
    lines = _wrap(draw, resto, f_body, LARGURA - 2 * MARGIN_X)
    _draw_block(draw, lines, f_body, 780, TX_MUTED, 64)
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
    lamina_depois(path(5), 5, "1",
                  "O agente lê a mensagem no segundo em que ela chega e consulta "
                  "o CRM sozinho — histórico, se já é cliente, o que já foi combinado.")
    lamina_depois(path(6), 6, "2",
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
