# Konzeptprojekte — Scroll-Animation & Echte Webdesign-Screenshots

**Datum:** 2026-05-26  
**Datei:** `NetlifyPage/index.html`

---

## Ziel

Den Konzeptprojekte-Abschnitt von einem horizontal scrollenden Karussell (100vw pro Panel) auf eine vertikale Pin-Animation umstellen: alle drei Geräte sind gleichzeitig sichtbar, und beim Scrollen rückt jedes Gerät der Reihe nach in den Mittelpunkt und vergrößert sich, während darin ein echtes Webdesign-Screenshot langsam nach unten scrollt.

---

## Bilder

Drei webp-Dateien werden von Downloads nach `NetlifyPage/assets/projects/` kopiert:

| Gerät | Dateiname | Inhalt |
|---|---|---|
| Tablet — Handwerk | `handwerk.webp` | Dachdecker-Meisterbetrieb, grün/weiß |
| Laptop — Zahnarzt | `dental.webp` | Dental Health, hellblau/weiß |
| Phone — Restaurant | `restaurant.webp` | Sushi-Restaurant, dunkel/gold |

Einbindung als `<img>` (kein CSS-Background), damit der Browser lazy-laden kann.

---

## HTML-Struktur

Die bestehenden `.showcase-track`, `.showcase-panel` (3× `min-width: 100vw`) und alle CSS-Platzhalter-Inhalte (`.fsite-craft`, `.fsite-dental`, `.fsite-resto` mit ihren Kind-Elementen) werden komplett ersetzt durch:

```html
<section class="showcase" id="projects">
  <div class="container showcase-header"> … </div>

  <div class="devices-row" id="devicesRow">

    <div class="dev-item" id="devItem0">
      <div class="dev-shell dev-shell--tablet" id="devShell0">
        <div class="dev-screen">
          <img src="assets/projects/handwerk.webp" alt="Handwerk Konzept" id="devImg0">
        </div>
      </div>
      <div class="device-label">
        <div class="device-industry" id="panel0Industry"></div>
        <div class="device-type" id="panel0Type"></div>
      </div>
    </div>

    <div class="dev-item" id="devItem1">
      <div class="dev-shell dev-shell--laptop" id="devShell1">
        <div class="dev-laptop-wrap">
          <div class="dev-laptop-body">
            <div class="dev-screen">
              <img src="assets/projects/dental.webp" alt="Zahnarzt Konzept" id="devImg1">
            </div>
          </div>
          <div class="dev-laptop-chin"></div>
          <div class="dev-laptop-foot"></div>
        </div>
      </div>
      <div class="device-label">
        <div class="device-industry" id="panel1Industry"></div>
        <div class="device-type" id="panel1Type"></div>
      </div>
    </div>

    <div class="dev-item" id="devItem2">
      <div class="dev-shell dev-shell--phone" id="devShell2">
        <div class="dev-phone-notch"></div>
        <div class="dev-screen">
          <img src="assets/projects/restaurant.webp" alt="Restaurant Konzept" id="devImg2">
        </div>
      </div>
      <div class="device-label">
        <div class="device-industry" id="panel2Industry"></div>
        <div class="device-type" id="panel2Type"></div>
      </div>
    </div>

  </div>
</section>
```

---

## CSS

Alle bestehenden Showcase-Styles (`.showcase-track`, `.showcase-panel`, `.fsite-*`, `.fc-*`, `.fd-*`, `.fr-*`) werden entfernt und durch folgende Regeln ersetzt:

```css
.showcase { position: relative; }
.showcase-header { padding: clamp(60px,8vw,100px) 0 48px; }

.devices-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: clamp(24px, 4vw, 60px);
  padding: 48px 0 80px;
  position: relative;
}

.dev-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  transform-origin: center center;
  will-change: transform, opacity;
}

/* Device shells — Basis-Größen (klein, Overview-Zustand) */
.dev-shell--tablet {
  width: 180px; height: 240px;
  background: #0d0d10;
  border-radius: 14px;
  border: 2px solid #2a2a30;
  box-shadow: 0 24px 60px rgba(0,0,0,0.55);
  overflow: hidden;
  position: relative;
}
.dev-shell--laptop {
  /* Laptop hat Wrap für Chin + Foot */
}
.dev-laptop-wrap { display: flex; flex-direction: column; align-items: center; }
.dev-laptop-body {
  width: 300px; height: 188px;
  background: #141414;
  border-radius: 8px 8px 0 0;
  border: 2px solid #2a2a2a;
  border-bottom: none;
  overflow: hidden;
  position: relative;
}
.dev-laptop-chin { width: 100%; height: 10px; background: #1a1a1a; border: 2px solid #222; border-top: none; border-radius: 0 0 3px 3px; }
.dev-laptop-foot { width: 75%; height: 6px; background: #131313; border-radius: 0 0 6px 6px; border: 1px solid #1e1e1e; border-top: none; }
.dev-shell--phone {
  width: 110px; height: 222px;
  background: #0d0d10;
  border-radius: 22px;
  border: 2px solid #2a2a30;
  box-shadow: 0 24px 60px rgba(0,0,0,0.55);
  overflow: hidden;
  position: relative;
}
.dev-phone-notch {
  position: absolute; top: 8px; left: 50%; transform: translateX(-50%);
  width: 32px; height: 5px; background: #111; border-radius: 3px; z-index: 3;
}

/* Screen + scrollendes Bild */
.dev-screen {
  position: absolute; inset: 6px;
  overflow: hidden;
  border-radius: inherit;
}
.dev-laptop-body .dev-screen { inset: 5px; border-radius: 3px; }
.dev-screen img {
  width: 100%;
  height: auto;        /* lässt Bild länger als Container sein */
  display: block;
  transform: translateY(0);
  will-change: transform;
}

/* Labels */
.device-label { text-align: center; opacity: 0; transition: opacity 0.3s; }
.device-label.visible { opacity: 1; }
.device-industry { font-size: 1rem; font-weight: 800; letter-spacing: -0.02em; color: var(--text); }
.device-type { font-size: 11px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); margin-top: 4px; }

/* Mobile */
@media (max-width: 767px) {
  .devices-row { flex-direction: column; gap: 40px; padding: 32px 0 48px; }
  .device-label { opacity: 1; }
}
```

---

## JavaScript — GSAP ScrollTrigger

Das bestehende Showcase-IIFE (horizontale Track-Translation) wird vollständig ersetzt:

```js
(function() {
  var isMobile = window.innerWidth < 768;
  if (isMobile) { /* einfache fade-in Animationen, wie bisher */ return; }

  var section = document.getElementById('projects');
  var items   = ['#devItem0','#devItem1','#devItem2'];
  var imgs    = ['#devImg0','#devImg1','#devImg2'];
  var labels  = ['.device-label in item0', …];

  // Fokus-Werte
  var SCALE_FOCUS = 2.2;
  var SCALE_REST  = 1.0;
  var OPACITY_DIM = 0.25;

  // X-Offset zum Zentrum: berechnet beim Init aus getBoundingClientRect
  // Gerät 0 (links)  → positiver x-Wert (nach rechts)
  // Gerät 1 (mitte)  → x = 0
  // Gerät 2 (rechts) → negativer x-Wert (nach links)
  function getCenterOffset(el) {
    var rowCenter = document.getElementById('devicesRow').getBoundingClientRect();
    var elRect    = el.getBoundingClientRect();
    var elCenter  = elRect.left + elRect.width / 2;
    var rowMid    = rowCenter.left + rowCenter.width / 2;
    return rowMid - elCenter;
  }

  var tl = gsap.timeline({
    scrollTrigger: {
      trigger: section,
      pin: true,
      scrub: 1,
      end: '+=300vh',
      onRefresh: function() { tl.invalidate(); } // recalc bei Resize
    }
  });

  // Phase 0–20%: Eingang (alle erscheinen)
  tl.from(items, { opacity: 0, y: 40, stagger: 0.1, duration: 0.2 });

  // Phase 20–40%: Gerät 0 Fokus — skaliert + rückt in Mitte
  tl.to('#devItem0', { scale: SCALE_FOCUS, x: () => getCenterOffset(document.getElementById('devItem0')), duration: 0.2 }, 0.2)
    .to(['#devItem1','#devItem2'], { opacity: OPACITY_DIM, duration: 0.15 }, 0.2)
    .to('#devImg0', { y: '-45%', ease: 'none', duration: 0.2 }, 0.2)
    .to('#devItem0', { scale: SCALE_REST, x: 0, duration: 0.15 }, 0.38)
    .to(['#devItem1','#devItem2'], { opacity: 1, duration: 0.1 }, 0.38);

  // Phase 40–60%: Gerät 1 Fokus — bereits mittig, nur skalieren
  tl.to('#devItem1', { scale: SCALE_FOCUS, duration: 0.2 }, 0.4)
    .to(['#devItem0','#devItem2'], { opacity: OPACITY_DIM, duration: 0.15 }, 0.4)
    .to('#devImg1', { y: '-45%', ease: 'none', duration: 0.2 }, 0.4)
    .to('#devItem1', { scale: SCALE_REST, duration: 0.15 }, 0.58)
    .to(['#devItem0','#devItem2'], { opacity: 1, duration: 0.1 }, 0.58);

  // Phase 60–80%: Gerät 2 Fokus — skaliert + rückt in Mitte
  tl.to('#devItem2', { scale: SCALE_FOCUS, x: () => getCenterOffset(document.getElementById('devItem2')), duration: 0.2 }, 0.6)
    .to(['#devItem0','#devItem1'], { opacity: OPACITY_DIM, duration: 0.15 }, 0.6)
    .to('#devImg2', { y: '-45%', ease: 'none', duration: 0.2 }, 0.6)
    .to('#devItem2', { scale: SCALE_REST, x: 0, duration: 0.15 }, 0.78)
    .to(['#devItem0','#devItem1'], { opacity: 1, duration: 0.1 }, 0.78);

  // Phase 80–100%: Ausgang
  tl.to(items, { opacity: 0, duration: 0.2 }, 0.85);
}());
```

**Hinweis:** Die genauen `y`-Werte für den Bild-Scroll hängen von der tatsächlichen Bildhöhe relativ zum Device-Frame ab — wird beim Testen feingesteuert (–30% bis –55% je nach Bild).

---

## Scope — was sich NICHT ändert

- i18n-Texte (`panel0Industry`, `panel0Type` etc.) bleiben unverändert
- `.showcase-header` mit Label, Headline, Note bleibt unverändert
- `.showcase-progress` Dots werden entfernt (nicht mehr relevant)
- Alle anderen Sektionen (Hero, Process, Contact) bleiben unberührt

---

## Dateien die sich ändern

1. `NetlifyPage/index.html` — HTML, CSS-Block, JS-IIFE
2. `NetlifyPage/assets/projects/handwerk.webp` — neu (kopiert)
3. `NetlifyPage/assets/projects/dental.webp` — neu (kopiert)
4. `NetlifyPage/assets/projects/restaurant.webp` — neu (kopiert)
