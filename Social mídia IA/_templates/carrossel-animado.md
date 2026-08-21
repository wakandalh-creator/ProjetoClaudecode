# Template — Carrossel Animado (2 slides, corte contínuo)

> Formaliza a técnica de carrossel que parece **uma imagem única cortada ao meio**: os dois slides são metades de uma mesma composição, com um elemento visual temático (o "fluxo de sinal" Neovertix — ver abaixo) atravessando o centro dos dois. No feed, o efeito de scroll entre slide 1 e 2 dá a sensação de continuidade; o elemento em movimento reforça isso.

## Elemento temático — "Fluxo de sinal" Neovertix

Adaptação do briefing original (lá era um elemento genérico tipo água-viva atravessando o corte) pro universo visual da marca: um **traço luminoso verde** (cor de destaque `accent.default #43A047`, esmaecendo pra `accent.light #8BC34A`) que atravessa o quadro como um sinal/corrente de dados fluindo — não é um objeto literal, é luz/energia em movimento, ecoando a seta ascendente do logo. Nunca usar outro elemento temático sem aprovação do Lucas (mantém consistência entre carrosséis animados diferentes).

## Regra de dimensão

Gerar **uma imagem única de 2160×1350px** (o dobro da largura de um slide 4:5) e cortar exatamente ao meio:
- Slide 1 = pixels 0–1080
- Slide 2 = pixels 1080–2160

Isso garante que o elemento cruzando o centro fique perfeitamente contínuo entre os dois slides publicados.

## Fluxo (3 passos)

### Passo 1 — Nano Banana gera a composição base (sem texto)

Gera a imagem 2160×1350 com a pessoa/composição da foto de referência **intacta** + o fluxo de sinal adicionado atravessando o centro. **Sem texto** — texto é adicionado no Passo 2 via Pillow (evita o problema conhecido de IA de imagem errar texto longo).

**Prompt-modelo (Nano Banana):**
```
A single continuous image, 2160x1350px, designed to be split down the exact
center into two carousel slides. [SUBJECT_DESCRIPTION] stays exactly as in
the reference photo — do not change pose, framing, outfit, face or
background composition. Add one continuous luminous signal trail that
flows horizontally across the full width of the image, passing directly
through the center split line — Neovertix brand green (#43A047 fading to
#8BC34A), glowing, like a current of data or energy, echoing the ascending
arrow in the Neovertix logo. Not a literal object, no logo, no text.
Background: [BACKGROUND_NOTE, default: "the navy-black Neovertix
background, #0A0E1A"]. Photographic, clean, no added text, no watermark.

Fidelity lock: preserve the subject exactly as shown in the reference
image — pose, framing, proportions, face, outfit and background
composition unchanged. Only add the described light element. Do not
invent logos, icons or text.
```

Variáveis: `[SUBJECT_DESCRIPTION]` (descrição da pessoa/composição da foto de referência), `[BACKGROUND_NOTE]` (default acima, trocar só se o roteiro pedir outro fundo).

### Passo 2 — Pillow sobrepõe o texto fixo de cada slide

Com a imagem base pronta, cortar em 2 (1080×1350 cada) e sobrepor o texto de cada slide (vem do roteiro — ver módulo 15) usando os tokens de tipografia da marca (`font.display` pros títulos/gancho, `font.text` pro corpo). Isso produz a composição final estática que vai pro KlingAI — texto já é pixel fixo na imagem, então "trava" junto com o resto da cena no passo 3.

### Passo 3 — KlingAI anima só o elemento visual (manual, sem API)

**Etapa manual** — KlingAI não tem integração via API neste projeto. O Lucas sobe a imagem final (com texto já sobreposto) direto na interface web do KlingAI e cola o prompt abaixo.

**Prompt-modelo (KlingAI):**
```
Locked static camera, no camera movement, no zoom, no pan. The entire
scene is frozen except for one element: the glowing green signal trail
crossing the frame — animate ONLY this element, as if energy/data is
flowing continuously along its path (subtle pulse, particle motion,
gentle glow travel), looping smoothly. The person, all text, and the
background are a locked static layer — zero movement, zero deformation,
zero change in expression or position. Duration: [DURATION]s, seamless
loop. Subtle motion only — no dramatic or fast movement.
```

Variável: `[DURATION]` (default 5s).

O resultado é 2 vídeos curtos (slide 1 e slide 2) que, publicados como carrossel, dão a sensação de uma cena contínua com só o fluxo de sinal se movendo.

## Checklist antes de apresentar ao Lucas

- [ ] Pessoa/composição idênticas entre os 2 slides (nenhuma variação além do corte)
- [ ] Fluxo de sinal contínuo através do corte central (sem quebra visual)
- [ ] Texto fixo, legível, no tom de voz e sem palavras banidas
- [ ] Paleta = tokens da marca (nunca preto puro, nunca roxo/gradiente genérico)
- [ ] Etapa KlingAI sinalizada como manual — Lucas precisa colar o prompt ele mesmo
