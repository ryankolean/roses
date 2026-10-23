/* Roses - motion layer (brand-guidelines.md, Motion).
   The idea: the site draws itself by hand, like the printed menu. Strokes ink
   in, photos come up like a lamp, the week's produce is laid on the table.
   Nothing moves the menu text itself.

   Progressive: every element is in the HTML and visible without this file.
   Hidden states are set here, by GSAP, only when the visitor has not asked for
   reduced motion. GSAP writes styles through the CSSOM, which the content
   security policy allows. */
(function () {
  'use strict';

  var gsap = window.gsap;
  var ScrollTrigger = window.ScrollTrigger;
  if (!gsap || !ScrollTrigger) return;
  gsap.registerPlugin(ScrollTrigger);
  ScrollTrigger.config({ ignoreMobileResize: true });

  var SVG_NS = 'http://www.w3.org/2000/svg';
  var ENTER = 'top 88%';
  var INK = 'power2.inOut';
  var SETTLE = 'power3.out';

  // Hide a stroke and return the tween that draws it. The gap is longer than
  // the path so a round line cap cannot leave a dot behind.
  function drawFrom(path) {
    var length = path.getTotalLength();
    gsap.set(path, { strokeDasharray: length + ' ' + (length + 2), strokeDashoffset: length + 1 });
    return { strokeDashoffset: 0 };
  }

  // <use> renders the motif in a closed shadow tree, so its strokes cannot be
  // animated. Swap in a copy of the symbol's own shapes; the picture is the same.
  function inlineMotif(svg, symbols) {
    var use = svg.querySelector('use');
    var id = use && (use.getAttribute('href') || '').split('#')[1];
    var symbol = id && symbols[id];
    if (!symbol) return false;
    svg.setAttribute('viewBox', symbol.getAttribute('viewBox'));
    var ratio = symbol.getAttribute('preserveAspectRatio');
    if (ratio) svg.setAttribute('preserveAspectRatio', ratio);
    svg.removeChild(use);
    Array.prototype.forEach.call(symbol.childNodes, function (node) {
      svg.appendChild(document.importNode(node, true));
    });
    return true;
  }

  function loadMotifs() {
    return fetch('assets/img/motifs.svg')
      .then(function (response) { return response.ok ? response.text() : ''; })
      .then(function (text) {
        var doc = new DOMParser().parseFromString(text, 'image/svg+xml');
        var symbols = {};
        Array.prototype.forEach.call(doc.querySelectorAll('symbol[id]'), function (s) {
          symbols[s.id] = s;
        });
        return symbols;
      });
  }

  // Wheat grows: each stalk's stem rises, then its leaves, one stalk after another.
  function growWheat(svg) {
    var stems = [], leaves = [];
    Array.prototype.forEach.call(svg.querySelectorAll('path'), function (path, i) {
      (i % 2 ? leaves : stems).push(path);
    });
    var tl = gsap.timeline({ scrollTrigger: { trigger: svg, start: ENTER, once: true } });
    stems.forEach(function (path, i) {
      tl.to(path, Object.assign(drawFrom(path), { duration: 0.45, ease: INK }), i * 0.14);
    });
    leaves.forEach(function (path, i) {
      tl.to(path, Object.assign(drawFrom(path), { duration: 0.5, ease: 'power1.out' }), 0.22 + i * 0.14);
    });
  }

  // A wave rule is ruled left to right: two waves a beat apart, then the bar.
  function ruleWave(svg) {
    var waves = svg.querySelectorAll('path');
    var bar = svg.querySelector('rect');
    var tl = gsap.timeline({ scrollTrigger: { trigger: svg, start: ENTER, once: true } });
    Array.prototype.forEach.call(waves, function (path, i) {
      tl.to(path, Object.assign(drawFrom(path), { duration: 1.3, ease: INK }), i * 0.18);
    });
    if (bar) tl.from(bar, { scaleX: 0, transformOrigin: '0% 50%', duration: 1.1, ease: INK }, 0.3);
  }

  // The homepage greeting gets an ember flourish, drawn once on arrival.
  function flourish(heading) {
    var anchor = document.createElement('span');
    anchor.className = 'flourish-anchor';
    while (heading.firstChild) anchor.appendChild(heading.firstChild);
    heading.appendChild(anchor);

    var svg = document.createElementNS(SVG_NS, 'svg');
    svg.setAttribute('class', 'flourish');
    svg.setAttribute('aria-hidden', 'true');
    svg.setAttribute('focusable', 'false');
    svg.setAttribute('viewBox', '0 0 200 12');
    svg.setAttribute('preserveAspectRatio', 'none');
    var path = document.createElementNS(SVG_NS, 'path');
    path.setAttribute('d', 'M2 6q11-6 22 0t22 0 22 0 22 0 22 0 22 0 22 0 22 0 22 0');
    path.setAttribute('fill', 'none');
    path.setAttribute('stroke', 'currentColor');
    path.setAttribute('stroke-width', '2.4');
    path.setAttribute('stroke-linecap', 'round');
    svg.appendChild(path);
    anchor.appendChild(svg);

    gsap.to(path, Object.assign(drawFrom(path), { duration: 1.4, ease: INK, delay: 0.35 }));

    return function () {
      while (anchor.firstChild && anchor.firstChild !== svg) heading.insertBefore(anchor.firstChild, anchor);
      heading.removeChild(anchor);
    };
  }

  // Photos come up like a lamp being turned on. The end value is explicit:
  // tweening toward the computed "none" interpolates through brightness(0).
  function lampUp(img, trigger) {
    var vars = { filter: 'brightness(1)', duration: 1.4, ease: 'power2.out', clearProps: 'filter' };
    if (trigger) vars.scrollTrigger = { trigger: trigger, start: ENTER, once: true };
    gsap.fromTo(img, { filter: 'brightness(0.8)' }, vars);
  }

  gsap.matchMedia().add('(prefers-reduced-motion: no-preference)', function (context) {
    var root = document.documentElement;
    var undo = [];
    root.classList.add('motion');

    var greeting = document.querySelector('.summit-hero__title, main h1.display');
    if (greeting) undo.push(flourish(greeting));

    var hero = document.querySelector('.summit-hero__media, .hero__img img');
    if (hero) lampUp(hero, null);

    gsap.utils.toArray('main .photo img').forEach(function (img) {
      if (img !== hero) lampUp(img, img);
    });

    gsap.utils.toArray('.awards').forEach(function (list) {
      var items = list.querySelectorAll('li');
      var tl = gsap.timeline({ scrollTrigger: { trigger: list, start: ENTER, once: true } });
      tl.fromTo(items, { '--rule': 0 }, { '--rule': 1, duration: 0.9, ease: INK, stagger: 0.12 }, 0)
        .from(list.querySelectorAll('.outlet, .what'), { y: 8, autoAlpha: 0, duration: 0.7, ease: SETTLE, stagger: 0.06 }, 0.2);
    });

    // The week's produce is laid on the table: each photo lands at a slight angle and squares up.
    ScrollTrigger.batch('.gallery > *', {
      start: ENTER,
      once: true,
      onEnter: function (batch) {
        gsap.from(batch, {
          y: 28, autoAlpha: 0, duration: 0.9, ease: SETTLE, stagger: 0.1,
          rotation: function (i) { return i % 2 ? 2.4 : -2.4; }
        });
      }
    });

    ScrollTrigger.batch('main .card, main .quote', {
      start: ENTER,
      once: true,
      onEnter: function (batch) {
        gsap.from(batch, { y: 16, autoAlpha: 0, duration: 0.7, ease: SETTLE, stagger: 0.08 });
      }
    });

    var motifs = document.querySelectorAll('svg.wheat, svg.rule');
    if (motifs.length) {
      // A named context method keeps these late tweens in the matchMedia
      // context, so they revert with everything else if reduced motion is
      // switched on.
      context.add('drawMotifs', function (symbols) {
        Array.prototype.forEach.call(motifs, function (svg) {
          if (!inlineMotif(svg, symbols)) return;
          if (svg.classList.contains('wheat')) growWheat(svg);
          else ruleWave(svg);
        });
        ScrollTrigger.refresh();
      });
      loadMotifs().then(function (symbols) { context.drawMotifs(symbols); })
        .catch(function () { /* the static motifs stay as they are */ });
    }

    return function () {
      root.classList.remove('motion');
      undo.forEach(function (fn) { fn(); });
    };
  });
})();
