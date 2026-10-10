/**
 * Piloto Vértice — motor de movimento (GSAP + ScrollTrigger + Lenis via CDN).
 *
 * Progressive enhancement, fallback-first:
 * - Todo o conteúdo já está visível em CSS puro (ver styles.css). Este script
 *   só adiciona movimento DEPOIS de confirmar que as 3 libs carregaram —
 *   nunca esconde conteúdo que já foi pintado.
 * - Se qualquer lib falhar (CDN fora, ad-blocker, etc.), o script sai cedo
 *   e a página continua 100% funcional e legível sem nenhuma animação.
 */
(function () {
  "use strict";

  if (typeof gsap === "undefined" || typeof ScrollTrigger === "undefined" || typeof Lenis === "undefined") {
    // ponytail: bail simples — fallback CSS já garante página legível.
    return;
  }

  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  gsap.registerPlugin(ScrollTrigger);

  /* ----------------------------------------------------------------------
     Lenis — smooth scroll da página inteira (Strong, 2026-10-09).
     Integração oficial recomendada: Lenis no ticker do GSAP, não em listener
     de scroll próprio — mantém INP sob controle (passivo, só transform).
     Desligado inteiramente em reduced-motion: scroll nativo é mais previsível
     pra quem é sensível a movimento.
     ---------------------------------------------------------------------- */
  if (!prefersReducedMotion) {
    var lenis = new Lenis();
    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add(function (time) {
      lenis.raf(time * 1000);
    });
    gsap.ticker.lagSmoothing(0);
  }

  if (prefersReducedMotion) {
    // Conteúdo já visível via CSS fallback — nada a fazer. Não liga
    // .motion-ready, não aplica parallax. O usuário entende 100% do
    // conteúdo com o movimento inteiro desligado (regra não-negociável).
    return;
  }

  /* ----------------------------------------------------------------------
     Entrada do Hero — eyebrow → H1 → subhead → CTA, stagger.
     set() + to() no mesmo tick: GSAP agenda o primeiro frame renderizado
     já em progresso de tween (via seu próprio rAF), então não existe um
     frame pintado "100% oculto" isolado antes da entrada começar — o H1
     nunca fica invisível esperando a rede, porque o CSS já o mostrava.
     ---------------------------------------------------------------------- */
  var heroEls = gsap.utils.toArray("[data-hero-reveal]");
  if (heroEls.length) {
    gsap.set(heroEls, { opacity: 0, y: 16 });
    gsap.to(heroEls, {
      opacity: 1,
      y: 0,
      duration: 0.6,
      ease: "power2.out",
      stagger: 0.12,
    });
  }

  /* ----------------------------------------------------------------------
     Scroll-reveal (Medium) — as 8 seções, via [data-reveal].
     .motion-ready só é ligado aqui, depois de tudo confirmado — é o que
     ativa a regra CSS que oculta [data-reveal] antes do reveal via scroll.
     ---------------------------------------------------------------------- */
  document.documentElement.classList.add("motion-ready");

  // Objeções ganha stagger entre os 4 itens (~60ms) — pacing de leitura.
  var objecoesList = document.querySelector(".objecoes__list");
  if (objecoesList) {
    var objecoesItems = gsap.utils.toArray(".objecoes__item");
    gsap.set(objecoesItems, { opacity: 0, y: 24 });
    ScrollTrigger.create({
      trigger: objecoesList,
      start: "top 82%",
      once: true,
      onEnter: function () {
        gsap.to(objecoesItems, {
          opacity: 1,
          y: 0,
          duration: 0.5,
          ease: "power2.out",
          stagger: 0.06,
        });
      },
    });
  }

  // Demais [data-reveal] (exceto os itens de Objeções, já tratados acima):
  // fade + slide curto, 1 reveal por elemento, dispara uma vez.
  var genericReveals = gsap.utils.toArray("[data-reveal]").filter(function (el) {
    return !el.closest(".objecoes__list");
  });
  genericReveals.forEach(function (el) {
    gsap.set(el, { opacity: 0, y: 24 });
    ScrollTrigger.create({
      trigger: el,
      start: "top 85%",
      once: true,
      onEnter: function () {
        gsap.to(el, { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" });
      },
    });
  });

  /* ----------------------------------------------------------------------
     Parallax 1 (Strong) — glow Hero → Problema. Só transform, scrub.
     Função: continuidade espacial entre as seções, não decoração solta.
     ---------------------------------------------------------------------- */
  var heroGlow = document.querySelector(".hero__glow");
  if (heroGlow) {
    gsap.to(heroGlow, {
      yPercent: 40,
      ease: "none",
      scrollTrigger: {
        trigger: "#hero",
        start: "top top",
        end: "bottom top",
        scrub: true,
      },
    });
  }

  /* ----------------------------------------------------------------------
     Parallax 2 (Strong) — trilha de "Como funciona", scrub síncrono.
     A trilha "cresce" (scaleY) acompanhando a leitura dos 3 passos —
     reforça visualmente que é sequência, não 3 cards soltos.
     Só ativa em telas >=768px, onde a trilha é visível (ver styles.css).
     ---------------------------------------------------------------------- */
  var trail = document.querySelector(".mecanismo__trail");
  if (trail && window.matchMedia("(min-width: 768px)").matches) {
    gsap.set(trail, { scaleY: 0 });
    gsap.to(trail, {
      scaleY: 1,
      ease: "none",
      scrollTrigger: {
        trigger: "#como-funciona",
        start: "top 70%",
        end: "bottom 60%",
        scrub: true,
      },
    });
  }
})();
