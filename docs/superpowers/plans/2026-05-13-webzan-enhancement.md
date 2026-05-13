# WebZan.de Enhancement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 8 Features auf webzan.de umsetzen — DSGVO-Fix, Dark/Light Logo, Floating Constellations, erweitertes Kontaktformular, 4 Service-Detailseiten, Cookie-Banner, Device Showcase mit Horizontal Pin Scroll.

**Architecture:** Alles reines HTML/CSS/JS in `NetlifyPage/`. Kein Framework, kein Build-Step. Alle Änderungen gehen in `index.html` (umbenannte `mockup-orbit.html`) und neue Dateien unter `services/` und `legal/`. GSAP 3.12 + ScrollTrigger + Lenis bleiben per CDN.

**Tech Stack:** Vanilla JS · GSAP 3.12 (CDN) · ScrollTrigger (CDN) · Lenis (CDN) · Netlify Forms · Inter (self-hosted woff2)

---

## Dateiübersicht

| Aktion | Pfad | Verantwortlich für |
|--------|------|--------------------|
| Umbenennen | `NetlifyPage/mockup-orbit.html` → `index.html` | Hauptseite |
| Erstellen | `NetlifyPage/assets/fonts/inter-400.woff2` | Self-hosted Font |
| Erstellen | `NetlifyPage/assets/fonts/inter-600.woff2` | Self-hosted Font |
| Erstellen | `NetlifyPage/assets/fonts/inter-700.woff2` | Self-hosted Font |
| Erstellen | `NetlifyPage/assets/fonts/inter-900.woff2` | Self-hosted Font |
| Kopieren | `Logo/webzan-logo-amber-light-1024.png` → `NetlifyPage/assets/logo/` | Light-Mode Logo |
| Modifizieren | `NetlifyPage/index.html` | Alle Features 1–8 |
| Erstellen | `NetlifyPage/services/wordpress.html` | Service-Detail |
| Erstellen | `NetlifyPage/services/motion.html` | Service-Detail |
| Erstellen | `NetlifyPage/services/landing-page.html` | Service-Detail |
| Erstellen | `NetlifyPage/services/ui-ux.html` | Service-Detail |
| Erstellen | `NetlifyPage/legal/impressum.html` | Impressum deployed |
| Erstellen | `NetlifyPage/legal/datenschutz.html` | Datenschutz deployed |

---

## Task 1: Datei-Setup — umbenennen, Fonts laden, Logo kopieren

**Files:**
- Rename: `NetlifyPage/mockup-orbit.html` → `NetlifyPage/index.html`
- Create: `NetlifyPage/assets/fonts/` (Verzeichnis)
- Copy: `Logo/webzan-logo-amber-light-1024.png` → `NetlifyPage/assets/logo/`

- [ ] **Schritt 1.1: mockup-orbit.html umbenennen**

```powershell
Rename-Item "C:\Projekte\webzan\NetlifyPage\mockup-orbit.html" "index.html"
```

Erwartung: Datei heißt jetzt `C:\Projekte\webzan\NetlifyPage\index.html`.

- [ ] **Schritt 1.2: fonts-Verzeichnis anlegen**

```powershell
New-Item -ItemType Directory -Force "C:\Projekte\webzan\NetlifyPage\assets\fonts"
New-Item -ItemType Directory -Force "C:\Projekte\webzan\NetlifyPage\services"
New-Item -ItemType Directory -Force "C:\Projekte\webzan\NetlifyPage\legal"
```

- [ ] **Schritt 1.3: Amber-Light Logo kopieren**

```powershell
Copy-Item "C:\Projekte\webzan\Logo\webzan-logo-amber-light-1024.png" `
          "C:\Projekte\webzan\NetlifyPage\assets\logo\webzan-logo-amber-light-1024.png"
```

- [ ] **Schritt 1.4: Inter-Fonts herunterladen**

Öffne im Browser: https://gwfh.mranftl.com/fonts/inter?subsets=latin

Wähle: Weights `400, 600, 700, 900` · Format `woff2` · Subset `latin` · Klick „Download files".

Entpacke das ZIP und kopiere diese 4 Dateien nach `NetlifyPage/assets/fonts/`:
- `inter-v13-latin-regular.woff2` → umbenennen zu `inter-400.woff2`
- `inter-v13-latin-600.woff2` → umbenennen zu `inter-600.woff2`
- `inter-v13-latin-700.woff2` → umbenennen zu `inter-700.woff2`
- `inter-v13-latin-900.woff2` → umbenennen zu `inter-900.woff2`

Prüfen:
```powershell
Get-ChildItem "C:\Projekte\webzan\NetlifyPage\assets\fonts\"
```
Erwartung: 4 `.woff2`-Dateien aufgelistet.

- [ ] **Schritt 1.5: Commit**

```powershell
cd C:\Projekte\webzan
git init  # falls noch kein git-Repo
git add NetlifyPage/index.html NetlifyPage/assets/fonts/ NetlifyPage/assets/logo/webzan-logo-amber-light-1024.png NetlifyPage/services/ NetlifyPage/legal/
git commit -m "chore: setup — rename to index.html, add fonts dir, copy amber-light logo"
```

---

## Task 2: DSGVO Fix — Google Fonts durch self-hosted Inter ersetzen

**Files:**
- Modify: `NetlifyPage/index.html` Zeilen 8–10 (Google Fonts `<link>`-Tags)
- Modify: `NetlifyPage/index.html` Zeile ~19 (`:root` CSS Block — `@font-face` einfügen)

- [ ] **Schritt 2.1: Google Fonts Links entfernen**

In `NetlifyPage/index.html`, ersetze die 3 Zeilen:
```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&display=swap" rel="stylesheet">
```
mit:
```html
  <!-- Inter self-hosted — DSGVO-konform -->
```

- [ ] **Schritt 2.2: @font-face direkt vor `:root {` einfügen**

Direkt vor der Zeile `/* ============================================` im `<style>`-Block einfügen:

```css
    /* Self-hosted Inter — replaces Google Fonts CDN */
    @font-face {
      font-family: 'Inter';
      src: url('assets/fonts/inter-400.woff2') format('woff2');
      font-weight: 400;
      font-style: normal;
      font-display: swap;
    }
    @font-face {
      font-family: 'Inter';
      src: url('assets/fonts/inter-600.woff2') format('woff2');
      font-weight: 600;
      font-style: normal;
      font-display: swap;
    }
    @font-face {
      font-family: 'Inter';
      src: url('assets/fonts/inter-700.woff2') format('woff2');
      font-weight: 700;
      font-style: normal;
      font-display: swap;
    }
    @font-face {
      font-family: 'Inter';
      src: url('assets/fonts/inter-900.woff2') format('woff2');
      font-weight: 900;
      font-style: normal;
      font-display: swap;
    }

```

- [ ] **Schritt 2.3: Visuell prüfen**

`index.html` im Browser öffnen. DevTools → Network-Tab → Filter `fonts.goog` eingeben.  
Erwartung: **Keine Requests** an `fonts.googleapis.com` oder `fonts.gstatic.com`.  
Text auf der Seite muss weiterhin in Inter erscheinen (Seitenüberschrift, Nav-Links, usw.).

- [ ] **Schritt 2.4: Commit**

```powershell
git add NetlifyPage/index.html
git commit -m "fix(dsgvo): self-host Inter font, remove Google Fonts CDN"
```

---

## Task 3: Logo-Fix Light Mode + Legal Pages

**Files:**
- Modify: `NetlifyPage/index.html` — `setTheme()`-Funktion (~Zeile 1456)
- Create: `NetlifyPage/legal/impressum.html`
- Create: `NetlifyPage/legal/datenschutz.html`

- [ ] **Schritt 3.1: Logo-Swap im setTheme()-Fix**

Finde in `index.html` die Zeile:
```js
          ? 'assets/logo/webzan-logo-amber-dark-1024.png'
          : 'assets/logo/webzan-logo-transparent-1024.png';
```
Ersetze sie mit:
```js
          ? 'assets/logo/webzan-logo-amber-dark-1024.png'
          : 'assets/logo/webzan-logo-amber-light-1024.png';
```

- [ ] **Schritt 3.2: Light Mode prüfen**

Browser öffnen → ☀-Button klicken → Logo muss auf das Amber-Light-Logo wechseln (warmes Gold auf hellem Hintergrund), nicht mehr transparent/unsichtbar.

- [ ] **Schritt 3.3: Impressum erstellen**

Erstelle `NetlifyPage/legal/impressum.html`:

```html
<!DOCTYPE html>
<html lang="de" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Impressum — WebZan</title>
  <link rel="icon" type="image/png" href="../assets/logo/favicon-32.png">
  <style>
    @font-face { font-family:'Inter'; src:url('../assets/fonts/inter-400.woff2') format('woff2'); font-weight:400; font-display:swap; }
    @font-face { font-family:'Inter'; src:url('../assets/fonts/inter-700.woff2') format('woff2'); font-weight:700; font-display:swap; }
    *, *::before, *::after { box-sizing:border-box; margin:0; padding:0; }
    :root { --accent:#E8B84B; }
    [data-theme="dark"] { --bg:#1A1510; --text:#F5F0E8; --muted:#8A8070; --border:rgba(232,184,75,0.15); }
    [data-theme="light"] { --bg:#FAFAF8; --text:#1A1510; --muted:#6A6050; --border:rgba(232,184,75,0.3); }
    body { font-family:'Inter',sans-serif; background:var(--bg); color:var(--text); line-height:1.8; padding:80px clamp(24px,5vw,80px) 120px; max-width:720px; margin:0 auto; transition:background 0.3s,color 0.3s; }
    h1 { font-size:clamp(2rem,6vw,3.5rem); font-weight:900; letter-spacing:-0.03em; margin-bottom:48px; color:var(--accent); }
    h2 { font-size:1.1rem; font-weight:700; margin:36px 0 8px; }
    p, address { font-size:0.95rem; color:var(--muted); font-style:normal; }
    a { color:var(--accent); text-decoration:none; }
    a:hover { text-decoration:underline; }
    .back { display:inline-flex; align-items:center; gap:8px; font-size:13px; font-weight:600; color:var(--muted); margin-bottom:48px; transition:color 0.2s; }
    .back:hover { color:var(--accent); }
    .theme-btn { position:fixed; top:24px; right:24px; padding:6px 14px; border-radius:100px; border:1px solid var(--border); background:transparent; color:var(--muted); font-size:12px; font-weight:600; cursor:pointer; font-family:'Inter',sans-serif; transition:all 0.2s; }
    .theme-btn:hover { border-color:var(--accent); color:var(--accent); }
  </style>
</head>
<body>
  <button class="theme-btn" id="themeBtn">☀</button>
  <a href="../index.html" class="back">← WebZan.de</a>
  <h1>Impressum</h1>

  <h2>Angaben gemäß §5 TMG</h2>
  <address>
    Hendrik Zanzig<br>
    [Straße und Hausnummer]<br>
    [PLZ] Berlin<br>
    Deutschland
  </address>

  <h2>Kontakt</h2>
  <p>E-Mail: <a href="mailto:tri.henne@gmail.com">tri.henne@gmail.com</a></p>

  <h2>Umsatzsteuer-ID</h2>
  <p>USt-IdNr. gemäß §27a UStG: [USt-ID eintragen]</p>

  <h2>Streitschlichtung</h2>
  <p>Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit: <a href="https://ec.europa.eu/consumers/odr/" target="_blank" rel="noopener">ec.europa.eu/consumers/odr</a>. Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>

  <script>
    var html = document.documentElement;
    var btn = document.getElementById('themeBtn');
    var t = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light');
    html.setAttribute('data-theme', t);
    btn.textContent = t === 'dark' ? '☀' : '🌙';
    btn.addEventListener('click', function() {
      t = html.dataset.theme === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', t);
      btn.textContent = t === 'dark' ? '☀' : '🌙';
      localStorage.setItem('theme', t);
    });
  </script>
</body>
</html>
```

- [ ] **Schritt 3.4: Datenschutzerklärung erstellen**

Erstelle `NetlifyPage/legal/datenschutz.html`:

```html
<!DOCTYPE html>
<html lang="de" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Datenschutz — WebZan</title>
  <link rel="icon" type="image/png" href="../assets/logo/favicon-32.png">
  <style>
    @font-face { font-family:'Inter'; src:url('../assets/fonts/inter-400.woff2') format('woff2'); font-weight:400; font-display:swap; }
    @font-face { font-family:'Inter'; src:url('../assets/fonts/inter-700.woff2') format('woff2'); font-weight:700; font-display:swap; }
    *, *::before, *::after { box-sizing:border-box; margin:0; padding:0; }
    :root { --accent:#E8B84B; }
    [data-theme="dark"] { --bg:#1A1510; --text:#F5F0E8; --muted:#8A8070; --border:rgba(232,184,75,0.15); }
    [data-theme="light"] { --bg:#FAFAF8; --text:#1A1510; --muted:#6A6050; --border:rgba(232,184,75,0.3); }
    body { font-family:'Inter',sans-serif; background:var(--bg); color:var(--text); line-height:1.8; padding:80px clamp(24px,5vw,80px) 120px; max-width:720px; margin:0 auto; transition:background 0.3s,color 0.3s; }
    h1 { font-size:clamp(2rem,6vw,3.5rem); font-weight:900; letter-spacing:-0.03em; margin-bottom:48px; color:var(--accent); }
    h2 { font-size:1.1rem; font-weight:700; margin:36px 0 8px; }
    p { font-size:0.95rem; color:var(--muted); margin-bottom:12px; }
    a { color:var(--accent); text-decoration:none; }
    .back { display:inline-flex; align-items:center; gap:8px; font-size:13px; font-weight:600; color:var(--muted); margin-bottom:48px; transition:color 0.2s; }
    .back:hover { color:var(--accent); }
    .theme-btn { position:fixed; top:24px; right:24px; padding:6px 14px; border-radius:100px; border:1px solid var(--border); background:transparent; color:var(--muted); font-size:12px; font-weight:600; cursor:pointer; font-family:'Inter',sans-serif; transition:all 0.2s; }
  </style>
</head>
<body>
  <button class="theme-btn" id="themeBtn">☀</button>
  <a href="../index.html" class="back">← WebZan.de</a>
  <h1>Datenschutz&shy;erklärung</h1>

  <h2>1. Verantwortlicher</h2>
  <p>Hendrik Zanzig, [Adresse], tri.henne@gmail.com</p>

  <h2>2. Hosting</h2>
  <p>Diese Website wird bei Netlify Inc., 512 2nd Street, San Francisco, CA 94107, USA gehostet. Netlify verarbeitet beim Seitenaufruf technisch notwendige Verbindungsdaten (IP-Adresse, Zeitstempel, aufgerufene URL). Grundlage: Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse am Betrieb der Website). Weitere Informationen: <a href="https://www.netlify.com/privacy/" target="_blank" rel="noopener">netlify.com/privacy</a>.</p>

  <h2>3. Kontaktformular</h2>
  <p>Wenn Sie das Kontaktformular nutzen, werden Ihre Angaben (Name, E-Mail-Adresse, Nachricht und optionale Projektangaben) über Netlify Forms übertragen und dort gespeichert. Netlify fungiert dabei als Auftragsverarbeiter. Ihre Daten werden ausschließlich zur Bearbeitung Ihrer Anfrage verwendet und danach gelöscht, sobald sie nicht mehr benötigt werden. Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO.</p>

  <h2>4. Schriften</h2>
  <p>Diese Website verwendet die Schriftart „Inter", die lokal auf dem Server gespeichert ist. Es werden keine Schriftdaten an Dritte (z. B. Google) übertragen.</p>

  <h2>5. Externe Skripte (GSAP, Lenis)</h2>
  <p>Für Animationen werden JavaScript-Bibliotheken (GSAP von cdnjs.cloudflare.com, Lenis von cdn.jsdelivr.net) von externen CDN-Servern geladen. Dabei können technische Daten (IP-Adresse) an die CDN-Anbieter übertragen werden. Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO.</p>

  <h2>6. Lokaler Speicher (localStorage)</h2>
  <p>Diese Website speichert Ihre Theme- und Sprachpräferenz im localStorage Ihres Browsers. Dies dient ausschließlich technischen Zwecken und erfordert keine Einwilligung (§ 25 Abs. 2 Nr. 2 TTDSG). Es werden keine personenbezogenen Daten gespeichert.</p>

  <h2>7. Ihre Rechte</h2>
  <p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit sowie Widerspruch. Beschwerden richten Sie an die zuständige Datenschutzaufsichtsbehörde.</p>

  <script>
    var html = document.documentElement;
    var btn = document.getElementById('themeBtn');
    var t = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light');
    html.setAttribute('data-theme', t);
    btn.textContent = t === 'dark' ? '☀' : '🌙';
    btn.addEventListener('click', function() {
      t = html.dataset.theme === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', t);
      btn.textContent = t === 'dark' ? '☀' : '🌙';
      localStorage.setItem('theme', t);
    });
  </script>
</body>
</html>
```

- [ ] **Schritt 3.5: Footer-Link in index.html aktualisieren**

Im Footer von `index.html` den Impressum-Link finden (suche nach `id="footerImprint"`) und das `href`-Attribut im `renderContent`-Bereich anpassen. Finde die Zeile:
```html
        <a href="#" class="footer-link" id="footerImprint"></a>
```
Ersetze mit:
```html
        <a href="legal/impressum.html" class="footer-link" id="footerImprint"></a>
```

- [ ] **Schritt 3.6: Commit**

```powershell
git add NetlifyPage/index.html NetlifyPage/legal/
git commit -m "fix: light-mode logo swap, add legal pages (impressum + datenschutz)"
```

---

## Task 4: Cookie Consent Banner

**Files:**
- Modify: `NetlifyPage/index.html` — CSS-Block (Banner-Styles), HTML vor `</body>`, JS-Block (Banner-Logik)

- [ ] **Schritt 4.1: CSS für Banner ans Ende des `<style>`-Blocks einfügen**

Direkt vor `</style>` (vor `</head>`) einfügen:

```css
    /* ============================================
       COOKIE CONSENT BANNER
    ============================================ */
    .consent-banner {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      z-index: 9999;
      padding: 14px clamp(24px, 5vw, 80px);
      background: var(--bg2);
      border-top: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      transform: translateY(100%);
      opacity: 0;
      transition: background 0.4s ease, border-color 0.4s ease;
    }
    .consent-banner.is-visible {
      transform: translateY(0);
      opacity: 1;
    }
    .consent-text {
      font-size: 12.5px;
      color: var(--muted);
      line-height: 1.6;
      flex: 1;
      min-width: 200px;
    }
    .consent-text a {
      color: var(--accent);
      text-decoration: underline;
      text-underline-offset: 2px;
    }
    .consent-ok {
      padding: 8px 20px;
      border-radius: 100px;
      background: var(--accent);
      color: #1A1510;
      border: none;
      font-size: 12px;
      font-weight: 700;
      font-family: 'Inter', sans-serif;
      cursor: pointer;
      flex-shrink: 0;
      transition: opacity 0.2s;
    }
    .consent-ok:hover { opacity: 0.85; }
```

- [ ] **Schritt 4.2: Banner-HTML direkt vor `</body>` einfügen**

```html
  <!-- ============================================
       COOKIE CONSENT BANNER
  ============================================ -->
  <div class="consent-banner" id="consentBanner" role="region" aria-label="Cookie-Hinweis">
    <p class="consent-text" id="consentText"></p>
    <button class="consent-ok" id="consentOk"></button>
  </div>
```

- [ ] **Schritt 4.3: Banner-JS am Ende des `<script>`-Blocks einfügen (vor dem letzten `}());`)**

Direkt vor `}());` einfügen:

```js
    /* ==========================================
       COOKIE CONSENT BANNER
    ========================================== */
    (function() {
      var banner = document.getElementById('consentBanner');
      var textEl = document.getElementById('consentText');
      var okBtn  = document.getElementById('consentOk');
      if (!banner || localStorage.getItem('consent') === '1') return;

      var texts = {
        de: {
          msg: 'Wir verwenden keine Tracking-Cookies. Formulardaten werden von <a href="legal/datenschutz.html">Netlify verarbeitet</a>.',
          ok: 'Verstanden'
        },
        en: {
          msg: 'We use no tracking cookies. Form data is <a href="legal/datenschutz.html">processed by Netlify</a>.',
          ok: 'Got it'
        }
      };

      function updateBannerLang(l) {
        var t = texts[l] || texts.de;
        textEl.innerHTML = t.msg;
        okBtn.textContent = t.ok;
      }

      var currentLang = localStorage.getItem('lang') || 'de';
      updateBannerLang(currentLang);

      // Sync banner language when user switches language
      var origRender = render;
      render = function(l) {
        origRender(l);
        updateBannerLang(l);
      };

      // Show banner with GSAP slide-up
      gsap.to(banner, {
        y: 0,
        opacity: 1,
        duration: 0.5,
        ease: 'power3.out',
        delay: 1.2,
        onStart: function() { banner.classList.add('is-visible'); }
      });

      okBtn.addEventListener('click', function() {
        localStorage.setItem('consent', '1');
        gsap.to(banner, {
          y: '100%',
          opacity: 0,
          duration: 0.35,
          ease: 'power2.in',
          onComplete: function() { banner.remove(); }
        });
      });
    }());
```

- [ ] **Schritt 4.4: Prüfen**

`localStorage` leeren (DevTools → Application → Local Storage → alles löschen), Seite neu laden.  
Erwartung: Banner erscheint nach ~1.2s von unten. Klick auf "Verstanden" → Banner gleitet weg. Seite neu laden → Banner erscheint nicht mehr.

- [ ] **Schritt 4.5: Commit**

```powershell
git add NetlifyPage/index.html
git commit -m "feat: cookie consent banner with GSAP slide-up, i18n"
```

---

## Task 5: Floating Constellations Canvas

**Files:**
- Modify: `NetlifyPage/index.html` — CSS (Canvas-Positionierung), HTML (Canvas-Element in Hero), JS (Animation-Logik)

- [ ] **Schritt 5.1: Canvas-CSS einfügen**

Im `<style>`-Block direkt nach dem `.hero::before`-Block (suche `pointer-events: none;` im Hero-Bereich) einfügen:

```css
    .hero-canvas {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
    }
    .hero-inner {
      position: relative;
      z-index: 1;
    }
```

Hinweis: Wenn `.hero-inner` bereits `position: relative` hat, nur den Canvas-Block einfügen.

- [ ] **Schritt 5.2: Canvas-Element im Hero-HTML einfügen**

Finde in `index.html`:
```html
  <section class="hero" id="hero">
    <div class="container">
      <div class="hero-inner">
```
Ersetze mit:
```html
  <section class="hero" id="hero">
    <canvas class="hero-canvas" id="constellationCanvas" aria-hidden="true"></canvas>
    <div class="container">
      <div class="hero-inner">
```

- [ ] **Schritt 5.3: Canvas-Animations-JS einfügen**

Direkt nach `gsap.registerPlugin(ScrollTrigger);` im JS-Block einfügen:

```js
    /* ==========================================
       FLOATING CONSTELLATIONS CANVAS
    ========================================== */
    (function() {
      var canvas = document.getElementById('constellationCanvas');
      if (!canvas) return;
      var ctx = canvas.getContext('2d');
      var nodes = [];
      var NODE_COUNT = 35;
      var MAX_DIST = 80;
      var animId;

      function resize() {
        canvas.width  = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
      }
      resize();
      window.addEventListener('resize', resize, { passive: true });

      for (var i = 0; i < NODE_COUNT; i++) {
        nodes.push({
          x:  Math.random() * canvas.width,
          y:  Math.random() * canvas.height,
          vx: (Math.random() - 0.5) * 0.4,
          vy: (Math.random() - 0.5) * 0.4,
          r:  Math.random() * 1.6 + 0.7
        });
      }

      function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        nodes.forEach(function(n) {
          n.x += n.vx;
          n.y += n.vy;
          if (n.x < 0 || n.x > canvas.width)  n.vx *= -1;
          if (n.y < 0 || n.y > canvas.height) n.vy *= -1;
        });

        for (var i = 0; i < nodes.length; i++) {
          for (var j = i + 1; j < nodes.length; j++) {
            var dx = nodes[i].x - nodes[j].x;
            var dy = nodes[i].y - nodes[j].y;
            var d  = Math.sqrt(dx * dx + dy * dy);
            if (d < MAX_DIST) {
              ctx.beginPath();
              ctx.moveTo(nodes[i].x, nodes[i].y);
              ctx.lineTo(nodes[j].x, nodes[j].y);
              ctx.strokeStyle = 'rgba(232,184,75,' + ((1 - d / MAX_DIST) * 0.18) + ')';
              ctx.lineWidth = 0.6;
              ctx.stroke();
            }
          }
        }

        nodes.forEach(function(n) {
          ctx.beginPath();
          ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
          ctx.fillStyle = 'rgba(232,184,75,0.5)';
          ctx.fill();
        });

        animId = requestAnimationFrame(draw);
      }

      // Respect prefers-reduced-motion
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      draw();
    }());
```

- [ ] **Schritt 5.4: Prüfen**

Seite im Browser laden. Im Hero-Bereich müssen sich kleine Amber-Punkte bewegen und Linien ziehen wenn sie nah beieinander sind. Keine Maus-Reaktion. Beim Resize des Fensters passt sich die Canvas an.

- [ ] **Schritt 5.5: Commit**

```powershell
git add NetlifyPage/index.html
git commit -m "feat: floating constellations canvas animation in hero"
```

---

## Task 6: Erweitertes Kontaktformular — HTML + CSS

**Files:**
- Modify: `NetlifyPage/index.html` — HTML (Formular-Felder), CSS (neue Formular-Styles)

- [ ] **Schritt 6.1: Neue Formular-CSS einfügen**

Im `<style>`-Block, nach dem bestehenden `.form-submit`-CSS-Block einfügen:

```css
    /* Extended contact form */
    .form-section-label {
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--accent);
      margin: 28px 0 16px;
      opacity: 0.8;
    }
    .form-field select {
      width: 100%;
      padding: 14px 16px;
      background: var(--bg2);
      border: 1px solid var(--border-sub);
      border-radius: 8px;
      color: var(--text);
      font-family: 'Inter', sans-serif;
      font-size: 0.95rem;
      cursor: pointer;
      transition: border-color var(--transition);
      appearance: none;
      -webkit-appearance: none;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%238A8070' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
      background-repeat: no-repeat;
      background-position: right 14px center;
      padding-right: 40px;
    }
    .form-field select:focus {
      outline: none;
      border-color: var(--accent);
    }
    .form-field select option {
      background: var(--bg2);
      color: var(--text);
    }
    .form-radio-group {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }
    .form-radio-label {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.9rem;
      color: var(--muted);
      cursor: pointer;
      padding: 10px 16px;
      border: 1px solid var(--border-sub);
      border-radius: 8px;
      transition: all var(--transition);
    }
    .form-radio-label:hover { border-color: var(--accent); color: var(--text); }
    .form-radio-label input[type="radio"] { display: none; }
    .form-radio-label.checked {
      border-color: var(--accent);
      color: var(--accent);
      background: var(--accent-dim);
    }
    .form-url-wrap {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.4s ease;
      margin-top: 0;
    }
    .form-url-wrap.visible {
      max-height: 80px;
      margin-top: 12px;
    }
    .form-url-wrap input {
      width: 100%;
      padding: 14px 16px;
      background: var(--bg2);
      border: 1px solid var(--border-sub);
      border-radius: 8px;
      color: var(--text);
      font-family: 'Inter', sans-serif;
      font-size: 0.95rem;
      transition: border-color var(--transition);
    }
    .form-url-wrap input:focus { outline: none; border-color: var(--accent); }
```

- [ ] **Schritt 6.2: Neue Formular-Felder im HTML einfügen**

Finde in `index.html`:
```html
          <div class="form-field">
            <label for="contactMessage" id="contactMessageLabel"></label>
            <textarea id="contactMessage" name="message" required></textarea>
          </div>
          <button type="submit" class="form-submit" id="contactSubmit"></button>
```
Ersetze mit:
```html
          <div class="form-field">
            <label for="contactMessage" id="contactMessageLabel"></label>
            <textarea id="contactMessage" name="message" required></textarea>
          </div>

          <!-- Block 1: Dein Projekt -->
          <p class="form-section-label" id="formBlock1Label"></p>

          <div class="form-field">
            <label id="formHasWebsiteLabel"></label>
            <div class="form-radio-group" id="formHasWebsiteGroup">
              <label class="form-radio-label" id="radioYesLabel">
                <input type="radio" name="has_website" value="yes" id="radioYes">
                <span id="radioYesText"></span>
              </label>
              <label class="form-radio-label" id="radioNoLabel">
                <input type="radio" name="has_website" value="no" id="radioNo">
                <span id="radioNoText"></span>
              </label>
            </div>
            <div class="form-url-wrap" id="formUrlWrap">
              <input type="url" name="existing_url" id="formExistingUrl" placeholder="https://">
            </div>
          </div>

          <div class="form-row">
            <div class="form-field">
              <label for="formScope" id="formScopeLabel"></label>
              <select id="formScope" name="scope">
                <option value="" id="formScopeDefault"></option>
                <option value="new" id="formScopeNew"></option>
                <option value="redesign" id="formScopeRedesign"></option>
                <option value="landing" id="formScopeLanding"></option>
                <option value="uiux" id="formScopeUiux"></option>
                <option value="unclear" id="formScopeUnclear"></option>
              </select>
            </div>
            <div class="form-field">
              <label for="formIndustry" id="formIndustryLabel"></label>
              <select id="formIndustry" name="industry">
                <option value="" id="formIndustryDefault"></option>
                <option value="restaurant" id="formInd1"></option>
                <option value="dental" id="formInd2"></option>
                <option value="craft" id="formInd3"></option>
                <option value="retail" id="formInd4"></option>
                <option value="service" id="formInd5"></option>
                <option value="startup" id="formInd6"></option>
                <option value="other" id="formInd7"></option>
              </select>
            </div>
          </div>

          <div class="form-row">
            <div class="form-field">
              <label for="formTimeline" id="formTimelineLabel"></label>
              <select id="formTimeline" name="timeline">
                <option value="" id="formTimelineDefault"></option>
                <option value="asap" id="formTL1"></option>
                <option value="1-3m" id="formTL2"></option>
                <option value="3-6m" id="formTL3"></option>
                <option value="flex" id="formTL4"></option>
              </select>
            </div>
            <div class="form-field">
              <label for="formGoal" id="formGoalLabel"></label>
              <select id="formGoal" name="goal">
                <option value="" id="formGoalDefault"></option>
                <option value="leads" id="formGoal1"></option>
                <option value="booking" id="formGoal2"></option>
                <option value="shop" id="formGoal3"></option>
                <option value="brand" id="formGoal4"></option>
                <option value="update" id="formGoal5"></option>
                <option value="unclear" id="formGoal6"></option>
              </select>
            </div>
          </div>

          <!-- Block 2: Noch etwas -->
          <p class="form-section-label" id="formBlock2Label"></p>

          <div class="form-field">
            <label for="formInspo" id="formInspoLabel"></label>
            <textarea id="formInspo" name="inspiration" rows="2" id="formInspo"></textarea>
          </div>

          <div class="form-field">
            <label for="formSource" id="formSourceLabel"></label>
            <select id="formSource" name="source">
              <option value="" id="formSourceDefault"></option>
              <option value="google" id="formSrc1"></option>
              <option value="referral" id="formSrc2"></option>
              <option value="social" id="formSrc3"></option>
              <option value="other" id="formSrc4"></option>
            </select>
          </div>

          <button type="submit" class="form-submit" id="contactSubmit"></button>
```

- [ ] **Schritt 6.3: Commit**

```powershell
git add NetlifyPage/index.html
git commit -m "feat: extended contact form HTML + CSS (8 optional fields)"
```

---

## Task 7: Kontaktformular — i18n + konditionelle Logik

**Files:**
- Modify: `NetlifyPage/index.html` — `content`-Objekt (de + en Keys), `render()`-Funktion, Radio-JS

- [ ] **Schritt 7.1: i18n-Content für Formular-Felder in `content.de` einfügen**

Im `content`-Objekt, im `de.contact`-Block, nach `send: 'Anfrage senden'` einfügen:

```js
        block1: 'Dein Projekt',
        block2: 'Noch etwas',
        hasWebsite: 'Existiert bereits eine Website?',
        radioYes: 'Ja',
        radioNo: 'Nein',
        existingUrl: 'URL der bestehenden Website',
        scope: 'Projektumfang',
        scopeDefault: '— Bitte wählen —',
        scopeNew: 'Neue Website',
        scopeRedesign: 'Redesign / Relaunch',
        scopeLanding: 'Landing Page',
        scopeUiux: 'UI/UX Beratung',
        scopeUnclear: 'Noch unklar',
        industry: 'Branche',
        industryDefault: '— Bitte wählen —',
        ind1: 'Restaurant / Gastronomie',
        ind2: 'Zahnarzt / Medizin',
        ind3: 'Handwerk / Bau',
        ind4: 'Einzelhandel',
        ind5: 'Dienstleistung',
        ind6: 'Startup / Tech',
        ind7: 'Andere',
        timeline: 'Wunsch-Zeitrahmen',
        timelineDefault: '— Bitte wählen —',
        tl1: 'So bald wie möglich',
        tl2: '1 – 3 Monate',
        tl3: '3 – 6 Monate',
        tl4: 'Noch flexibel',
        goal: 'Hauptziel der Website',
        goalDefault: '— Bitte wählen —',
        goal1: 'Anfragen / Leads generieren',
        goal2: 'Online-Termine buchen',
        goal3: 'Produkte verkaufen (Shop)',
        goal4: 'Marke / Portfolio aufbauen',
        goal5: 'Bestehende Seite aktualisieren',
        goal6: 'Noch unklar',
        inspo: 'Inspirations-URLs',
        inspoPlaceholder: 'z. B. apple.com, studio.com — Seiten die dir gefallen',
        sourceLabel: 'Wie bist du auf mich gestoßen?',
        sourceDefault: '— Bitte wählen —',
        src1: 'Google',
        src2: 'Empfehlung',
        src3: 'Instagram / LinkedIn',
        src4: 'Anderes',
```

- [ ] **Schritt 7.2: i18n-Content für Formular-Felder in `content.en` einfügen**

Im `content.en.contact`-Block analog einfügen:

```js
        block1: 'Your Project',
        block2: 'One more thing',
        hasWebsite: 'Do you have an existing website?',
        radioYes: 'Yes',
        radioNo: 'No',
        existingUrl: 'URL of existing website',
        scope: 'Project scope',
        scopeDefault: '— Please select —',
        scopeNew: 'New website',
        scopeRedesign: 'Redesign / Relaunch',
        scopeLanding: 'Landing page',
        scopeUiux: 'UI/UX consulting',
        scopeUnclear: 'Not sure yet',
        industry: 'Industry',
        industryDefault: '— Please select —',
        ind1: 'Restaurant / Food',
        ind2: 'Dental / Medical',
        ind3: 'Trades / Construction',
        ind4: 'Retail',
        ind5: 'Services',
        ind6: 'Startup / Tech',
        ind7: 'Other',
        timeline: 'Desired timeline',
        timelineDefault: '— Please select —',
        tl1: 'As soon as possible',
        tl2: '1 – 3 months',
        tl3: '3 – 6 months',
        tl4: 'Flexible',
        goal: 'Primary website goal',
        goalDefault: '— Please select —',
        goal1: 'Generate leads / inquiries',
        goal2: 'Book appointments online',
        goal3: 'Sell products (shop)',
        goal4: 'Build brand / portfolio',
        goal5: 'Update existing site',
        goal6: 'Not sure yet',
        inspo: 'Inspiration URLs',
        inspoPlaceholder: 'e. g. apple.com, studio.com — sites you like',
        sourceLabel: 'How did you find me?',
        sourceDefault: '— Please select —',
        src1: 'Google',
        src2: 'Referral',
        src3: 'Instagram / LinkedIn',
        src4: 'Other',
```

- [ ] **Schritt 7.3: render()-Funktion erweitern**

Am Ende des `// Contact`-Blocks in der `render()`-Funktion (nach `contactSubmit.textContent`) einfügen:

```js
      // Extended form fields
      var f = c.contact;
      function setText(id, val) { var el = document.getElementById(id); if (el) el.textContent = val; }
      function setPlaceholder(id, val) { var el = document.getElementById(id); if (el) el.placeholder = val; }

      setText('formBlock1Label', f.block1);
      setText('formBlock2Label', f.block2);
      setText('formHasWebsiteLabel', f.hasWebsite);
      setText('radioYesText', f.radioYes);
      setText('radioNoText', f.radioNo);
      setPlaceholder('formExistingUrl', f.existingUrl);
      setText('formScopeLabel', f.scope);
      setText('formScopeDefault', f.scopeDefault);
      setText('formScopeNew', f.scopeNew);
      setText('formScopeRedesign', f.scopeRedesign);
      setText('formScopeLanding', f.scopeLanding);
      setText('formScopeUiux', f.scopeUiux);
      setText('formScopeUnclear', f.scopeUnclear);
      setText('formIndustryLabel', f.industry);
      setText('formIndustryDefault', f.industryDefault);
      setText('formInd1', f.ind1);
      setText('formInd2', f.ind2);
      setText('formInd3', f.ind3);
      setText('formInd4', f.ind4);
      setText('formInd5', f.ind5);
      setText('formInd6', f.ind6);
      setText('formInd7', f.ind7);
      setText('formTimelineLabel', f.timeline);
      setText('formTimelineDefault', f.timelineDefault);
      setText('formTL1', f.tl1);
      setText('formTL2', f.tl2);
      setText('formTL3', f.tl3);
      setText('formTL4', f.tl4);
      setText('formGoalLabel', f.goal);
      setText('formGoalDefault', f.goalDefault);
      setText('formGoal1', f.goal1);
      setText('formGoal2', f.goal2);
      setText('formGoal3', f.goal3);
      setText('formGoal4', f.goal4);
      setText('formGoal5', f.goal5);
      setText('formGoal6', f.goal6);
      setText('formInspoLabel', f.inspo);
      setPlaceholder('formInspo', f.inspoPlaceholder);
      setText('formSourceLabel', f.sourceLabel);
      setText('formSourceDefault', f.sourceDefault);
      setText('formSrc1', f.src1);
      setText('formSrc2', f.src2);
      setText('formSrc3', f.src3);
      setText('formSrc4', f.src4);
```

- [ ] **Schritt 7.4: Radio-JS für konditionelles URL-Feld einfügen**

Nach dem `render(lang);`-Aufruf (Initial render) einfügen:

```js
    /* ==========================================
       CONTACT FORM — CONDITIONAL URL FIELD
    ========================================== */
    (function() {
      var urlWrap = document.getElementById('formUrlWrap');
      var radios = document.querySelectorAll('input[name="has_website"]');
      var labels = document.querySelectorAll('.form-radio-label');

      radios.forEach(function(radio) {
        radio.addEventListener('change', function() {
          labels.forEach(function(l) { l.classList.remove('checked'); });
          this.parentElement.classList.add('checked');
          if (this.value === 'yes') {
            urlWrap.classList.add('visible');
          } else {
            urlWrap.classList.remove('visible');
            document.getElementById('formExistingUrl').value = '';
          }
        });
      });
    }());
```

- [ ] **Schritt 7.5: Prüfen**

Kontaktformular in Browser öffnen (Scroll nach unten). Prüfen:
- Alle Felder erscheinen mit deutschen Labels
- Sprache auf EN wechseln → alle Labels wechseln sofort
- Radio "Ja" klicken → URL-Feld gleitet mit CSS-Transition auf
- Radio "Nein" klicken → URL-Feld verschwindet wieder

- [ ] **Schritt 7.6: Commit**

```powershell
git add NetlifyPage/index.html
git commit -m "feat: contact form i18n + conditional URL field"
```

---

## Task 8: Service-Detailseiten (alle 4)

**Files:**
- Create: `NetlifyPage/services/wordpress.html`
- Create: `NetlifyPage/services/motion.html`
- Create: `NetlifyPage/services/landing-page.html`
- Create: `NetlifyPage/services/ui-ux.html`

- [ ] **Schritt 8.1: `services/motion.html` erstellen (Motion Websites)**

```html
<!DOCTYPE html>
<html lang="de" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Motion Websites — WebZan</title>
  <link rel="icon" type="image/png" href="../assets/logo/favicon-32.png">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
  <style>
    @font-face { font-family:'Inter'; src:url('../assets/fonts/inter-400.woff2') format('woff2'); font-weight:400; font-display:swap; }
    @font-face { font-family:'Inter'; src:url('../assets/fonts/inter-600.woff2') format('woff2'); font-weight:600; font-display:swap; }
    @font-face { font-family:'Inter'; src:url('../assets/fonts/inter-700.woff2') format('woff2'); font-weight:700; font-display:swap; }
    @font-face { font-family:'Inter'; src:url('../assets/fonts/inter-900.woff2') format('woff2'); font-weight:900; font-display:swap; }

    *, *::before, *::after { box-sizing:border-box; margin:0; padding:0; }
    :root { --accent:#E8B84B; --accent-dim:rgba(232,184,75,0.12); --transition:0.3s cubic-bezier(0.4,0,0.2,1); }
    [data-theme="dark"] { --bg:#1A1510; --bg2:#221B12; --text:#F5F0E8; --muted:#8A8070; --border:rgba(232,184,75,0.15); --border-sub:rgba(245,240,232,0.08); }
    [data-theme="light"] { --bg:#FAFAF8; --bg2:#F0EDE6; --text:#1A1510; --muted:#6A6050; --border:rgba(232,184,75,0.3); --border-sub:rgba(26,21,16,0.1); }

    body { font-family:'Inter',sans-serif; background:var(--bg); color:var(--text); line-height:1.6; overflow-x:hidden; transition:background 0.4s,color 0.4s; }
    a { color:inherit; text-decoration:none; }
    .container { width:100%; max-width:1280px; margin:0 auto; padding:0 clamp(24px,5vw,80px); }

    /* NAV */
    .nav { position:fixed; top:0; left:0; right:0; z-index:900; padding:20px 0; transition:background 0.4s,padding 0.3s; border-bottom:1px solid transparent; }
    .nav.scrolled { background:rgba(26,21,16,0.88); backdrop-filter:blur(16px); border-bottom-color:var(--border); padding:14px 0; }
    [data-theme="light"] .nav.scrolled { background:rgba(250,250,248,0.88); }
    .nav-inner { display:flex; align-items:center; justify-content:space-between; }
    .nav-logo-img { height:28px; width:auto; }
    .back-link { display:flex; align-items:center; gap:8px; font-size:13px; font-weight:600; color:var(--muted); transition:color var(--transition); }
    .back-link:hover { color:var(--accent); }
    .nav-controls { display:flex; gap:10px; }
    .pill-btn { padding:6px 14px; border-radius:100px; border:1px solid var(--border-sub); background:transparent; color:var(--muted); font-size:12px; font-weight:600; font-family:'Inter',sans-serif; cursor:pointer; transition:all var(--transition); }
    .pill-btn:hover { border-color:var(--accent); color:var(--accent); }

    /* HERO */
    .service-hero { min-height:60svh; display:flex; align-items:flex-end; padding:140px 0 clamp(48px,6vw,80px); position:relative; overflow:hidden; }
    .service-hero::before { content:''; position:absolute; top:-20%; right:-10%; width:50vw; height:50vw; background:radial-gradient(circle,rgba(232,184,75,0.07) 0%,transparent 70%); pointer-events:none; }
    .service-eyebrow { font-size:11px; font-weight:600; letter-spacing:0.18em; text-transform:uppercase; color:var(--accent); margin-bottom:20px; display:flex; align-items:center; gap:12px; opacity:0; }
    .service-eyebrow::before { content:''; display:block; width:32px; height:1px; background:var(--accent); }
    .service-headline { font-size:clamp(3rem,8vw,7rem); font-weight:900; line-height:0.95; letter-spacing:-0.03em; margin-bottom:24px; overflow:hidden; }
    .headline-line { display:block; clip-path:inset(0 0 100% 0); }
    .headline-line.accent { color:var(--accent); }
    .service-tagline { font-size:clamp(1rem,2vw,1.25rem); color:var(--muted); max-width:560px; opacity:0; transform:translateY(20px); }

    /* CANVAS */
    .hero-canvas { position:absolute; inset:0; width:100%; height:100%; pointer-events:none; z-index:0; }
    .service-hero .container { position:relative; z-index:1; }

    /* SECTIONS */
    .service-section { padding:clamp(60px,8vw,100px) 0; }
    .service-section + .service-section { border-top:1px solid var(--border-sub); }
    .section-label { font-size:11px; font-weight:600; letter-spacing:0.15em; text-transform:uppercase; color:var(--accent); margin-bottom:24px; opacity:0; transform:translateY(20px); }
    .section-headline { font-size:clamp(1.8rem,4vw,3rem); font-weight:900; letter-spacing:-0.03em; margin-bottom:24px; opacity:0; transform:translateY(20px); }
    .section-text { font-size:0.95rem; color:var(--muted); max-width:640px; line-height:1.8; margin-bottom:16px; opacity:0; transform:translateY(20px); }

    /* FOR WHOM */
    .bullet-list { list-style:none; display:flex; flex-direction:column; gap:16px; margin-top:8px; }
    .bullet-item { display:flex; align-items:flex-start; gap:16px; opacity:0; transform:translateX(-20px); }
    .bullet-icon { width:40px; height:40px; background:var(--accent-dim); border:1px solid var(--border); border-radius:10px; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
    .bullet-text { font-size:0.95rem; color:var(--muted); padding-top:10px; }

    /* PROCESS */
    .process-list { list-style:none; display:flex; flex-direction:column; gap:0; }
    .process-item { display:flex; gap:24px; padding:24px 0; border-bottom:1px solid var(--border-sub); opacity:0; transform:translateX(-20px); }
    .process-num { font-size:11px; font-weight:700; color:var(--accent); letter-spacing:0.08em; padding-top:4px; min-width:32px; }
    .process-title { font-size:1rem; font-weight:700; margin-bottom:4px; }
    .process-desc { font-size:0.9rem; color:var(--muted); line-height:1.7; }

    /* CTA */
    .service-cta { display:flex; gap:16px; align-items:center; flex-wrap:wrap; padding:clamp(60px,8vw,100px) 0; }
    .btn-primary { display:inline-flex; align-items:center; gap:10px; padding:14px 28px; background:var(--accent); color:#1A1510; border-radius:6px; font-weight:700; font-size:0.95rem; transition:opacity var(--transition); }
    .btn-primary:hover { opacity:0.85; }
    .btn-ghost { font-size:0.9rem; color:var(--muted); transition:color var(--transition); }
    .btn-ghost:hover { color:var(--accent); }

    /* FOOTER */
    .footer { padding:32px 0; border-top:1px solid var(--border-sub); }
    .footer-inner { display:flex; justify-content:space-between; align-items:center; gap:16px; flex-wrap:wrap; }
    .footer-copy { font-size:12px; color:var(--muted); }
  </style>
</head>
<body>

  <canvas class="hero-canvas" id="svcCanvas" aria-hidden="true"></canvas>

  <nav class="nav" id="svcNav">
    <div class="container">
      <div class="nav-inner">
        <a href="../index.html" class="back-link" id="backLink">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M13 8H3M7 4l-4 4 4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <span id="backText">WebZan</span>
        </a>
        <img class="nav-logo-img" id="navLogo" src="../assets/logo/webzan-logo-amber-dark-1024.png" alt="WebZan" width="128" height="32">
        <div class="nav-controls">
          <button class="pill-btn" id="langBtn">EN</button>
          <button class="pill-btn" id="themeBtn">&#9788;</button>
        </div>
      </div>
    </div>
  </nav>

  <section class="service-hero">
    <div class="container">
      <p class="service-eyebrow" id="svcEyebrow"></p>
      <h1 class="service-headline">
        <span class="headline-line" id="svcLine1"></span>
        <span class="headline-line accent" id="svcLine2"></span>
      </h1>
      <p class="service-tagline" id="svcTagline"></p>
    </div>
  </section>

  <section class="service-section">
    <div class="container">
      <p class="section-label" id="whatLabel"></p>
      <h2 class="section-headline" id="whatHeadline"></h2>
      <p class="section-text" id="whatText1"></p>
      <p class="section-text" id="whatText2"></p>
    </div>
  </section>

  <section class="service-section">
    <div class="container">
      <p class="section-label" id="forWhomLabel"></p>
      <h2 class="section-headline" id="forWhomHeadline"></h2>
      <ul class="bullet-list" id="bulletList">
        <li class="bullet-item">
          <div class="bullet-icon"><svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M3 9l4 4 8-8" stroke="#E8B84B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
          <p class="bullet-text" id="bullet1"></p>
        </li>
        <li class="bullet-item">
          <div class="bullet-icon"><svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M3 9l4 4 8-8" stroke="#E8B84B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
          <p class="bullet-text" id="bullet2"></p>
        </li>
        <li class="bullet-item">
          <div class="bullet-icon"><svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M3 9l4 4 8-8" stroke="#E8B84B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
          <p class="bullet-text" id="bullet3"></p>
        </li>
      </ul>
    </div>
  </section>

  <section class="service-section">
    <div class="container">
      <p class="section-label" id="processLabel"></p>
      <h2 class="section-headline" id="processHeadline"></h2>
      <ul class="process-list" id="processList"></ul>
    </div>
  </section>

  <div class="service-cta">
    <div class="container" style="display:flex;gap:16px;align-items:center;flex-wrap:wrap;">
      <a href="../index.html#contact" class="btn-primary" id="ctaBtn">
        <span id="ctaBtnText"></span>
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <a href="../index.html" class="btn-ghost" id="backBtn"></a>
    </div>
  </div>

  <footer class="footer">
    <div class="container">
      <div class="footer-inner">
        <p class="footer-copy">&#169; 2026 WebZan</p>
        <a href="impressum.html" style="font-size:12px;color:var(--muted)" id="imprintLink"></a>
      </div>
    </div>
  </footer>

  <script>
  (function() {
    'use strict';
    gsap.registerPlugin(ScrollTrigger);

    var content = {
      de: {
        back: '← WebZan',
        eyebrow: '02 — Motion Websites',
        line1: 'Design',
        line2: 'in Bewegung.',
        tagline: 'GSAP-animierte Websites, die Besucher in Kunden verwandeln — für Brands, die mehr als eine Visitenkarte wollen.',
        whatLabel: '— Was ist das',
        whatHeadline: 'Mehr als eine Website.',
        whatText1: 'Motion Websites sind digitale Erlebnisse: jede Scroll-Bewegung löst eine Animation aus, jede Sektion erzählt eine Geschichte. Das Ergebnis ist ein professioneller erster Eindruck, der im Kopf bleibt.',
        whatText2: 'Technisch basiert das auf GSAP (GreenSock Animation Platform) — der Standard-Library für Web-Animationen bei Top-Agenturen weltweit. Ich kombiniere das mit modernem Design und klarer Nutzerführung.',
        forWhomLabel: '— Für wen',
        forWhomHeadline: 'Dein Brand verdient Bewegung.',
        bullet1: 'Restaurants, Galerien und Kreative, die mit dem ersten Eindruck überzeugen wollen',
        bullet2: 'Unternehmen, die sich von Standard-WordPress-Seiten abheben möchten',
        bullet3: 'Startups und Produkte, die ihren Launch unvergesslich machen wollen',
        processLabel: '— Mein Prozess',
        processHeadline: 'Wie wir vorgehen.',
        steps: [
          { num: '01 —', title: 'Briefing & Moodboard', desc: 'Wir definieren Ton, Farben, Animationssprache und Feeling der Seite.' },
          { num: '02 —', title: 'Design & Prototyp', desc: 'Screendesign in Figma, interaktiver Prototyp zum Anfassen.' },
          { num: '03 —', title: 'GSAP-Entwicklung', desc: 'Sauber codierte Motion Website — mobile-first, performance-optimiert.' },
          { num: '04 —', title: 'Launch & Übergabe', desc: 'Live-Schaltung, Hosting-Setup, kurze Einweisung.' }
        ],
        cta: 'Motion Website anfragen',
        backBtn: '← Zurück zur Übersicht',
        imprint: 'Impressum'
      },
      en: {
        back: '← WebZan',
        eyebrow: '02 — Motion Websites',
        line1: 'Design',
        line2: 'in Motion.',
        tagline: 'GSAP-animated websites that turn visitors into clients — for brands that want more than a business card.',
        whatLabel: '— What is this',
        whatHeadline: 'More than a website.',
        whatText1: 'Motion websites are digital experiences: every scroll triggers an animation, every section tells a story. The result is a professional first impression that stays in people\'s minds.',
        whatText2: 'Technically built on GSAP (GreenSock Animation Platform) — the industry-standard animation library used by top agencies worldwide. Combined with modern design and clear user journeys.',
        forWhomLabel: '— For whom',
        forWhomHeadline: 'Your brand deserves motion.',
        bullet1: 'Restaurants, galleries and creatives who want to impress from the first scroll',
        bullet2: 'Businesses that want to stand out from standard WordPress sites',
        bullet3: 'Startups and products that want an unforgettable launch',
        processLabel: '— My Process',
        processHeadline: 'How we work.',
        steps: [
          { num: '01 —', title: 'Briefing & Moodboard', desc: 'We define tone, colors, animation language and the overall feel.' },
          { num: '02 —', title: 'Design & Prototype', desc: 'Screendesign in Figma, interactive prototype to review.' },
          { num: '03 —', title: 'GSAP Development', desc: 'Clean-coded motion website — mobile-first, performance-optimized.' },
          { num: '04 —', title: 'Launch & Handover', desc: 'Go-live, hosting setup, short walkthrough.' }
        ],
        cta: 'Request motion website',
        backBtn: '← Back to overview',
        imprint: 'Imprint'
      }
    };

    var lang = localStorage.getItem('lang') || 'de';
    var html = document.documentElement;
    var logoEl = document.getElementById('navLogo');
    var themeBtn = document.getElementById('themeBtn');
    var langBtn = document.getElementById('langBtn');

    function setTheme(t) {
      html.setAttribute('data-theme', t);
      logoEl.src = t === 'dark' ? '../assets/logo/webzan-logo-amber-dark-1024.png' : '../assets/logo/webzan-logo-amber-light-1024.png';
      themeBtn.textContent = t === 'dark' ? '☀' : '🌙';
      localStorage.setItem('theme', t);
    }
    var savedTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light');
    setTheme(savedTheme);
    themeBtn.addEventListener('click', function() { setTheme(html.dataset.theme === 'dark' ? 'light' : 'dark'); });

    function render(l) {
      lang = l;
      html.lang = l;
      var c = content[l];
      document.getElementById('backText').textContent = c.back;
      document.getElementById('svcEyebrow').textContent = c.eyebrow;
      document.getElementById('svcLine1').textContent = c.line1;
      document.getElementById('svcLine2').textContent = c.line2;
      document.getElementById('svcTagline').textContent = c.tagline;
      document.getElementById('whatLabel').textContent = c.whatLabel;
      document.getElementById('whatHeadline').textContent = c.whatHeadline;
      document.getElementById('whatText1').textContent = c.whatText1;
      document.getElementById('whatText2').textContent = c.whatText2;
      document.getElementById('forWhomLabel').textContent = c.forWhomLabel;
      document.getElementById('forWhomHeadline').textContent = c.forWhomHeadline;
      document.getElementById('bullet1').textContent = c.bullet1;
      document.getElementById('bullet2').textContent = c.bullet2;
      document.getElementById('bullet3').textContent = c.bullet3;
      document.getElementById('processLabel').textContent = c.processLabel;
      document.getElementById('processHeadline').textContent = c.processHeadline;
      var list = document.getElementById('processList');
      list.innerHTML = '';
      c.steps.forEach(function(s) {
        var li = document.createElement('li');
        li.className = 'process-item';
        li.innerHTML = '<span class="process-num">' + s.num + '</span><div><h3 class="process-title">' + s.title + '</h3><p class="process-desc">' + s.desc + '</p></div>';
        list.appendChild(li);
      });
      document.getElementById('ctaBtnText').textContent = c.cta;
      document.getElementById('backBtn').textContent = c.backBtn;
      document.getElementById('imprintLink').textContent = c.imprint;
      langBtn.textContent = l === 'de' ? 'EN' : 'DE';
      localStorage.setItem('lang', l);
    }
    langBtn.addEventListener('click', function() { render(lang === 'de' ? 'en' : 'de'); });
    render(lang);

    // Nav scroll
    ScrollTrigger.create({ start: 60, onToggle: function(s) { document.getElementById('svcNav').classList.toggle('scrolled', s.isActive); } });

    // Entrance animations
    window.addEventListener('load', function() {
      var tl = gsap.timeline({ delay: 0.1 });
      tl.to('#svcEyebrow', { opacity: 1, duration: 0.5, ease: 'power3.out' });
      tl.to(['#svcLine1', '#svcLine2'], { clipPath: 'inset(0 0 0% 0)', duration: 0.9, ease: 'power4.out', stagger: 0.1 }, '-=0.2');
      tl.to('#svcTagline', { opacity: 1, y: 0, duration: 0.6, ease: 'power3.out' }, '-=0.3');
    });
    gsap.set(['#svcLine1', '#svcLine2'], { clipPath: 'inset(0 0 100% 0)' });

    // Scroll reveals
    document.querySelectorAll('.section-label, .section-headline, .section-text').forEach(function(el) {
      gsap.to(el, { scrollTrigger: { trigger: el, start: 'top 82%' }, opacity: 1, y: 0, duration: 0.7, ease: 'power3.out' });
    });
    ScrollTrigger.create({ trigger: '#bulletList', start: 'top 80%', onEnter: function() {
      gsap.to('.bullet-item', { opacity: 1, x: 0, duration: 0.6, ease: 'power3.out', stagger: 0.1 });
    }});
    ScrollTrigger.create({ trigger: '#processList', start: 'top 80%', onEnter: function() {
      gsap.to('.process-item', { opacity: 1, x: 0, duration: 0.5, ease: 'power3.out', stagger: 0.08 });
    }});

    // Canvas
    (function() {
      var canvas = document.getElementById('svcCanvas');
      if (!canvas || window.matchMedia('(prefers-reduced-motion:reduce)').matches) return;
      var ctx = canvas.getContext('2d');
      var nodes = [];
      function resize() { canvas.width = canvas.offsetWidth; canvas.height = canvas.offsetHeight; }
      resize();
      window.addEventListener('resize', resize, { passive: true });
      for (var i = 0; i < 20; i++) {
        nodes.push({ x: Math.random() * canvas.width, y: Math.random() * canvas.height, vx: (Math.random() - 0.5) * 0.35, vy: (Math.random() - 0.5) * 0.35, r: Math.random() * 1.4 + 0.6 });
      }
      function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        nodes.forEach(function(n) {
          n.x += n.vx; n.y += n.vy;
          if (n.x < 0 || n.x > canvas.width) n.vx *= -1;
          if (n.y < 0 || n.y > canvas.height) n.vy *= -1;
        });
        for (var i = 0; i < nodes.length; i++) {
          for (var j = i + 1; j < nodes.length; j++) {
            var dx = nodes[i].x - nodes[j].x, dy = nodes[i].y - nodes[j].y;
            var d = Math.sqrt(dx*dx + dy*dy);
            if (d < 80) {
              ctx.beginPath(); ctx.moveTo(nodes[i].x, nodes[i].y); ctx.lineTo(nodes[j].x, nodes[j].y);
              ctx.strokeStyle = 'rgba(232,184,75,' + ((1 - d/80) * 0.11) + ')'; ctx.lineWidth = 0.6; ctx.stroke();
            }
          }
        }
        nodes.forEach(function(n) { ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, Math.PI*2); ctx.fillStyle = 'rgba(232,184,75,0.3)'; ctx.fill(); });
        requestAnimationFrame(draw);
      }
      draw();
    }());
  }());
  </script>
</body>
</html>
```

- [ ] **Schritt 8.2: `services/wordpress.html` erstellen**

Kopiere `services/motion.html` als Basis. Ändere im `content`-Objekt:
- `eyebrow`: `'01 — WordPress Websites'`
- `line1`: `'WordPress,'` / `line2`: `'die funktionieren.'`
- `tagline`: `'Professionelle CMS-Lösungen, die du selbst pflegen kannst. Schnell, sicher, auf dein Business zugeschnitten.'`
- `whatText1`: `'WordPress ist das meistgenutzte CMS der Welt — ich setze es so um, dass du vollständige Kontrolle hast ohne technisches Know-how zu brauchen. Keine Page-Builder-Abhängigkeiten, kein überbordender Plugin-Dschungel.'`
- `whatText2`: `'Jede Seite wird maßgeschneidert: eigenes Design, eigene Struktur, eigene Inhalte. SEO-Grundlagen sind inklusive. Du bekommst eine Einweisung und kannst danach selbst Texte und Bilder aktualisieren.'`
- `bullet1`: `'Dienstleister, Praxen und Handwerksbetriebe, die eine professionelle Online-Präsenz brauchen'`
- `bullet2`: `'Unternehmen, die ihre Website selbst pflegen wollen ohne Entwickler anzufragen'`
- `bullet3`: `'KMUs, die in Google gefunden werden möchten'`
- Steps: Briefing → Konzept & Design → WordPress-Entwicklung → Launch & Einweisung
- `cta`: `'WordPress Website anfragen'`

Für `content.en` entsprechend übersetzen.

- [ ] **Schritt 8.3: `services/landing-page.html` erstellen**

Kopiere `services/motion.html` als Basis. Ändere im `content`-Objekt:
- `eyebrow`: `'03 — Landing Pages'`
- `line1`: `'Pages that'` / `line2`: `'convert.'`
- `tagline`: `'Conversion-optimierte Einzelseiten für Kampagnen, Produktlaunches und Service-Angebote.'`
- `whatText1`: `'Eine Landing Page hat genau ein Ziel: den Besucher zur Handlung zu bewegen. Kein Ablenkungsmenü, keine langen Texte — klarer Aufbau, starke Headline, eindeutiger Call-to-Action.'`
- `whatText2`: `'Ich designe und entwickle Landing Pages, die mit A/B-Testing-Best-Practices aufgebaut sind. Scroll-Animationen führen den Blick und bauen Vertrauen auf.'`
- `bullet1`: `'Kampagnen mit klarem Ziel: Anfragen, Anmeldungen, Downloads'`
- `bullet2`: `'Produktlaunches, die einen starken ersten Eindruck hinterlassen sollen'`
- `bullet3`: `'Service-Angebote, die klar positioniert und schnell verstanden werden müssen'`
- Steps: Briefing → Copywriting-Struktur → Design & Entwicklung → Launch
- `cta`: `'Landing Page anfragen'`

- [ ] **Schritt 8.4: `services/ui-ux.html` erstellen**

Kopiere `services/motion.html` als Basis. Ändere im `content`-Objekt:
- `eyebrow`: `'04 — UI/UX & Branding'`
- `line1`: `'Design, das'` / `line2`: `'überzeugt.'`
- `tagline`: `'Von der visuellen Identität bis zum fertigen Interface — systematisches Design, das zu deinem Business passt.'`
- `whatText1`: `'Gutes UI/UX ist nicht sichtbar — es macht die Nutzung einfach und angenehm. Ich analysiere User-Flows, definiere Hierarchien und designe Interfaces, die ohne Erklärung funktionieren.'`
- `whatText2`: `'Branding-Projekte beginnen mit der Frage: Was soll dein Business ausstrahlen? Das Ergebnis ist ein kohärentes System aus Farben, Typografie und Formen — für Website, Print und Social Media.'`
- `bullet1`: `'Startups, die eine visuelle Identität von Grund auf aufbauen wollen'`
- `bullet2`: `'Unternehmen, deren Website veraltet ist und einen frischen Look braucht'`
- `bullet3`: `'Produkte, die sich trotz guter Funktion nicht gut anfühlen'`
- Steps: Discovery → Moodboard & System → Interface-Design → Übergabe & Assets
- `cta`: `'UI/UX Projekt anfragen'`

- [ ] **Schritt 8.5: Service-Cards in index.html verlinken**

In der `renderServices()`-Funktion in `index.html`, ersetze die Card-Erstellung:

```js
    var serviceLinks = ['services/wordpress.html', 'services/motion.html', 'services/landing-page.html', 'services/ui-ux.html'];

    function renderServices(l) {
      var grid = document.getElementById('servicesGrid');
      var items = content[l].services.items;
      grid.innerHTML = '';
      items.forEach(function (item, i) {
        var card = document.createElement('a');
        card.className = 'service-card';
        card.setAttribute('href', serviceLinks[i]);
        card.setAttribute('aria-label', item.title);
        card.style.cursor = 'pointer';
        card.innerHTML =
          '<span class="service-num">' + item.num + '</span>' +
          '<h3 class="service-title">' + item.title + '</h3>' +
          '<p class="service-desc">' + item.desc + '</p>' +
          '<span class="service-arrow">&#8594;</span>';
        grid.appendChild(card);
      });
    }
```

Außerdem `.service-card`-CSS um Hover-Effekt erweitern (in `<style>`):
```css
    .service-card { display: block; text-decoration: none; transition: border-color var(--transition), transform var(--transition); }
    .service-card:hover { border-color: var(--accent); transform: translateY(-2px); }
    .service-arrow { font-size: 14px; color: var(--accent); display: block; margin-top: 12px; opacity: 0; transition: opacity var(--transition), transform var(--transition); transform: translateX(-4px); }
    .service-card:hover .service-arrow { opacity: 1; transform: translateX(0); }
```

- [ ] **Schritt 8.6: Prüfen**

Alle 4 Service-Seiten im Browser öffnen. Checkliste:
- Logo erscheint korrekt (dark: amber-dark, light: amber-light)
- Headline animiert mit Clip-Path beim Laden
- Sprache wechselt korrekt zwischen DE/EN
- Zurück-Link führt zu `index.html`
- Floating Constellations sichtbar im Hintergrund
- In `index.html`: Service-Cards sind klickbar, Pfeil erscheint beim Hover

- [ ] **Schritt 8.7: Commit**

```powershell
git add NetlifyPage/services/ NetlifyPage/index.html
git commit -m "feat: 4 service detail pages + clickable service cards"
```

---

## Task 9: Device Showcase — HTML + CSS

**Files:**
- Modify: `NetlifyPage/index.html` — `projects`-Section durch `showcase`-Section ersetzen, neue CSS-Regeln

- [ ] **Schritt 9.1: Showcase-CSS einfügen**

Im `<style>`-Block, am Ende vor `</style>`, einfügen:

```css
    /* ============================================
       DEVICE SHOWCASE — HORIZONTAL PIN SCROLL
    ============================================ */
    .showcase {
      position: relative;
      overflow: hidden;
    }
    .showcase-header {
      padding: clamp(60px,8vw,100px) 0 48px;
    }
    .showcase-track-outer {
      overflow: hidden;
      position: relative;
    }
    .showcase-track {
      display: flex;
      will-change: transform;
    }
    .showcase-panel {
      min-width: 100vw;
      height: 70vh;
      min-height: 480px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      flex-direction: column;
      gap: 20px;
    }
    .showcase-panel::before {
      content: '';
      position: absolute;
      inset: 0;
      pointer-events: none;
    }
    .panel-craft::before { background: radial-gradient(ellipse at 50% 50%, rgba(30,90,150,0.1) 0%, transparent 65%); }
    .panel-dental::before { background: radial-gradient(ellipse at 50% 50%, rgba(44,74,110,0.08) 0%, transparent 65%); }
    .panel-resto::before { background: radial-gradient(ellipse at 50% 50%, rgba(232,184,75,0.06) 0%, transparent 65%); }

    /* Progress dots */
    .showcase-progress {
      display: flex;
      gap: 8px;
      margin-top: 12px;
    }
    .sp-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--border-sub);
      transition: background 0.3s, transform 0.3s;
    }
    .sp-dot.active {
      background: var(--accent);
      transform: scale(1.3);
    }

    /* Device labels */
    .device-label {
      text-align: center;
      position: relative;
      z-index: 2;
    }
    .device-industry {
      font-size: 1.1rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--text);
    }
    .device-type {
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--muted);
      margin-top: 4px;
    }

    /* ---- DEVICE FRAMES ---- */
    .device-wrap {
      position: relative;
      z-index: 2;
    }

    /* Tablet */
    .dev-tablet {
      width: 220px;
      height: 290px;
      background: #0d0d10;
      border-radius: 18px;
      border: 2px solid #2a2a30;
      box-shadow: 0 32px 80px rgba(0,0,0,0.55), inset 0 1px 0 rgba(255,255,255,0.05);
      overflow: hidden;
      position: relative;
    }
    .dev-tablet-screen {
      position: absolute;
      inset: 8px;
      border-radius: 10px;
      overflow: hidden;
    }

    /* Laptop */
    .dev-laptop-wrap { display: flex; flex-direction: column; align-items: center; }
    .dev-laptop {
      width: 380px;
      height: 230px;
      background: #141414;
      border-radius: 10px 10px 0 0;
      border: 2px solid #2a2a2a;
      border-bottom: none;
      box-shadow: 0 -8px 40px rgba(0,0,0,0.4);
      position: relative;
      overflow: hidden;
    }
    .dev-laptop-bezel {
      position: absolute;
      inset: 6px;
      border-radius: 5px;
      overflow: hidden;
    }
    .dev-laptop-chin {
      width: 100%;
      height: 10px;
      background: #1a1a1a;
      border: 2px solid #222;
      border-top: none;
      border-radius: 0 0 3px 3px;
    }
    .dev-laptop-foot {
      width: 80%;
      height: 6px;
      background: #131313;
      border-radius: 0 0 6px 6px;
      border: 1px solid #1e1e1e;
      border-top: none;
    }

    /* Phone */
    .dev-phone {
      width: 130px;
      height: 260px;
      background: #0d0d10;
      border-radius: 26px;
      border: 2px solid #2a2a30;
      box-shadow: 0 32px 80px rgba(0,0,0,0.55), inset 0 1px 0 rgba(255,255,255,0.05);
      position: relative;
      overflow: hidden;
    }
    .dev-phone-notch {
      position: absolute;
      top: 10px;
      left: 50%;
      transform: translateX(-50%);
      width: 40px;
      height: 6px;
      background: #1a1a1a;
      border-radius: 3px;
      z-index: 3;
    }
    .dev-phone-screen {
      position: absolute;
      inset: 6px;
      border-radius: 20px;
      overflow: hidden;
    }

    /* ---- FAKE SITES ---- */
    /* Craft (Handwerk) — dark blue */
    .fsite-craft { position:absolute; inset:0; background:linear-gradient(160deg,#0e1825,#152235); display:flex; flex-direction:column; }
    .fc-hero { height:40%; background:#1e3a5a; flex-shrink:0; position:relative; overflow:hidden; display:flex; align-items:flex-end; padding:8px; }
    .fc-hero::after { content:''; position:absolute; bottom:0; left:0; right:0; height:2px; background:linear-gradient(90deg,transparent,rgba(30,90,200,0.5),transparent); }
    .fc-hero-text { display:flex; flex-direction:column; gap:3px; }
    .fc-line { height:3px; border-radius:1.5px; background:rgba(255,255,255,0.6); }
    .fc-body { padding:8px; display:flex; flex-direction:column; gap:4px; }
    .fc-bline { height:2.5px; border-radius:1.5px; background:rgba(30,90,150,0.3); }
    .fc-grid { display:grid; grid-template-columns:1fr 1fr; gap:4px; margin-top:4px; }
    .fc-card { height:28px; border-radius:4px; background:rgba(30,90,150,0.12); border:1px solid rgba(30,90,150,0.2); }

    /* Dental (Zahnarzt) — light */
    .fsite-dental { position:absolute; inset:0; background:#f5f2ee; display:flex; flex-direction:column; }
    .fd-nav { height:8%; background:#fff; border-bottom:1px solid #e0ddd8; flex-shrink:0; display:flex; align-items:center; padding:0 8px; }
    .fd-logo { width:30px; height:4px; background:#2c4a6e; border-radius:2px; }
    .fd-links { display:flex; gap:6px; margin-left:auto; }
    .fd-link { width:18px; height:3px; background:#ccc; border-radius:1.5px; }
    .fd-hero { height:40%; background:linear-gradient(135deg,#2c4a6e,#3a5f8a); flex-shrink:0; position:relative; overflow:hidden; display:flex; align-items:flex-end; padding:10px; }
    .fd-hero::before { content:''; position:absolute; top:-30%; right:-15%; width:70%; height:130%; background:rgba(255,255,255,0.06); border-radius:50%; }
    .fd-h-text { display:flex; flex-direction:column; gap:3px; }
    .fd-h-line { height:3px; border-radius:1.5px; background:rgba(255,255,255,0.75); }
    .fd-body { padding:8px; display:flex; flex-direction:column; gap:4px; }
    .fd-bline { height:2.5px; border-radius:1.5px; background:rgba(44,74,110,0.2); }
    .fd-grid { display:grid; grid-template-columns:1fr 1fr 1fr; gap:4px; margin-top:4px; }
    .fd-card { height:22px; border-radius:4px; background:rgba(44,74,110,0.07); border:1px solid rgba(44,74,110,0.14); }
    .fd-btn { width:48px; height:9px; background:#2c4a6e; border-radius:4px; margin-top:6px; }

    /* Resto (Restaurant) — amber dark */
    .fsite-resto { position:absolute; inset:0; background:#1a1208; display:flex; flex-direction:column; }
    .fr-hero { height:45%; background:linear-gradient(160deg,#0e0b04,#1e1608); flex-shrink:0; position:relative; overflow:hidden; border-bottom:1px solid rgba(232,184,75,0.15); display:flex; align-items:flex-end; padding:8px; }
    .fr-hero::before { content:''; position:absolute; top:0; right:0; width:55%; height:100%; background:radial-gradient(ellipse,rgba(232,184,75,0.1),transparent 70%); }
    .fr-h-text { display:flex; flex-direction:column; gap:3px; }
    .fr-h-line { height:3px; border-radius:1.5px; background:rgba(232,184,75,0.65); }
    .fr-body { padding:8px; display:flex; flex-direction:column; gap:4px; }
    .fr-bline { height:2.5px; border-radius:1.5px; background:rgba(232,184,75,0.18); }
    .fr-grid { display:grid; grid-template-columns:1fr 1fr; gap:4px; margin-top:4px; }
    .fr-card { height:28px; border-radius:4px; background:rgba(232,184,75,0.06); border:1px solid rgba(232,184,75,0.12); }

    /* Mobile fallback */
    @media (max-width: 767px) {
      .showcase-track { flex-direction: column; transform: none !important; }
      .showcase-panel { min-width: 100%; height: auto; padding: 48px 0; }
      .dev-laptop { width: 280px; height: 168px; }
    }
```

- [ ] **Schritt 9.2: Showcase-HTML — projects-Section ersetzen**

Finde und ersetze die komplette `<section class="projects" id="projects">...</section>` (Zeilen ~1233–1244) mit:

```html
  <!-- ============================================
       DEVICE SHOWCASE
  ============================================ -->
  <section class="showcase" id="projects">
    <div class="container showcase-header">
      <p class="section-label" id="projectsLabel"></p>
      <h2 class="projects-headline" id="projectsHeadline"></h2>
      <p class="projects-note" id="projectsNote"></p>
    </div>

    <div class="showcase-track-outer" id="showcaseOuter">
      <div class="showcase-track" id="showcaseTrack">

        <!-- PANEL 1: Tablet — Handwerk -->
        <div class="showcase-panel panel-craft" id="panel0">
          <div class="device-wrap" id="devWrap0">
            <div class="dev-tablet">
              <div class="dev-tablet-screen">
                <div class="fsite-craft" id="craftScroll">
                  <div class="fc-hero">
                    <div class="fc-hero-text">
                      <div class="fc-line" style="width:40px"></div>
                      <div class="fc-line" style="width:70px"></div>
                      <div class="fc-line" style="width:55px"></div>
                    </div>
                  </div>
                  <div class="fc-body">
                    <div class="fc-bline" style="width:100%"></div>
                    <div class="fc-bline" style="width:75%"></div>
                    <div class="fc-grid">
                      <div class="fc-card"></div><div class="fc-card"></div>
                      <div class="fc-card"></div><div class="fc-card"></div>
                    </div>
                    <div class="fc-bline" style="width:90%;margin-top:6px"></div>
                    <div class="fc-bline" style="width:60%"></div>
                    <div class="fc-grid">
                      <div class="fc-card"></div><div class="fc-card"></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="device-label">
            <div class="device-industry" id="panel0Industry"></div>
            <div class="device-type" id="panel0Type"></div>
          </div>
        </div>

        <!-- PANEL 2: Laptop — Zahnarztpraxis -->
        <div class="showcase-panel panel-dental" id="panel1">
          <div class="device-wrap" id="devWrap1">
            <div class="dev-laptop-wrap">
              <div class="dev-laptop">
                <div class="dev-laptop-bezel">
                  <div class="fsite-dental" id="dentalScroll">
                    <div class="fd-nav">
                      <div class="fd-logo"></div>
                      <div class="fd-links">
                        <div class="fd-link"></div><div class="fd-link"></div><div class="fd-link"></div>
                      </div>
                    </div>
                    <div class="fd-hero">
                      <div class="fd-h-text">
                        <div class="fd-h-line" style="width:50px"></div>
                        <div class="fd-h-line" style="width:90px"></div>
                        <div class="fd-h-line" style="width:70px"></div>
                      </div>
                    </div>
                    <div class="fd-body">
                      <div class="fd-bline" style="width:100%"></div>
                      <div class="fd-bline" style="width:70%"></div>
                      <div class="fd-grid">
                        <div class="fd-card"></div><div class="fd-card"></div><div class="fd-card"></div>
                      </div>
                      <div class="fd-btn"></div>
                      <div class="fd-bline" style="width:100%;margin-top:8px"></div>
                      <div class="fd-bline" style="width:55%"></div>
                    </div>
                  </div>
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

        <!-- PANEL 3: Phone — Restaurant -->
        <div class="showcase-panel panel-resto" id="panel2">
          <div class="device-wrap" id="devWrap2">
            <div class="dev-phone">
              <div class="dev-phone-notch"></div>
              <div class="dev-phone-screen">
                <div class="fsite-resto" id="restoScroll">
                  <div class="fr-hero">
                    <div class="fr-h-text">
                      <div class="fr-h-line" style="width:35px"></div>
                      <div class="fr-h-line" style="width:60px"></div>
                      <div class="fr-h-line" style="width:48px"></div>
                    </div>
                  </div>
                  <div class="fr-body">
                    <div class="fr-bline" style="width:100%"></div>
                    <div class="fr-bline" style="width:68%"></div>
                    <div class="fr-grid">
                      <div class="fr-card"></div><div class="fr-card"></div>
                    </div>
                    <div class="fr-bline" style="width:85%;margin-top:6px"></div>
                    <div class="fr-bline" style="width:55%"></div>
                    <div class="fr-grid">
                      <div class="fr-card"></div><div class="fr-card"></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="device-label">
            <div class="device-industry" id="panel2Industry"></div>
            <div class="device-type" id="panel2Type"></div>
          </div>
          <div class="showcase-progress">
            <div class="sp-dot active" id="spDot0"></div>
            <div class="sp-dot" id="spDot1"></div>
            <div class="sp-dot" id="spDot2"></div>
          </div>
        </div>

      </div>
    </div>
  </section>
```

- [ ] **Schritt 9.3: i18n-Content für Showcase in `content`-Objekt aktualisieren**

Das bestehende `projects`-Objekt in `content.de` und `content.en` bleibt erhalten (Labels/Headlines), ergänze nur die Panel-Texte:

In `content.de` nach `projects.note`:
```js
        panels: [
          { industry: 'Handwerk', type: 'Tablet' },
          { industry: 'Zahnarztpraxis', type: 'Laptop' },
          { industry: 'Restaurant', type: 'Handy' }
        ]
```

In `content.en` nach `projects.note`:
```js
        panels: [
          { industry: 'Trades', type: 'Tablet' },
          { industry: 'Dental Practice', type: 'Laptop' },
          { industry: 'Restaurant', type: 'Phone' }
        ]
```

- [ ] **Schritt 9.4: Showcase-Render in `render()`-Funktion ergänzen**

Im `render()`-Block, nach `renderProjects(l)` (oder dessen Ersatz), einfügen:

```js
      // Showcase panel labels
      if (c.projects.panels) {
        c.projects.panels.forEach(function(p, i) {
          var indEl = document.getElementById('panel' + i + 'Industry');
          var typEl = document.getElementById('panel' + i + 'Type');
          if (indEl) indEl.textContent = p.industry;
          if (typEl) typEl.textContent = p.type;
        });
      }
```

Außerdem die alte `renderProjects()`-Funktion entfernen (oder leer lassen — sie erzeugt nun nichts mehr da `projectsGrid` nicht existiert).

- [ ] **Schritt 9.5: Commit**

```powershell
git add NetlifyPage/index.html
git commit -m "feat: device showcase HTML + CSS (horizontal panels, device frames)"
```

---

## Task 10: Device Showcase — GSAP Scroll + Eingangs-Animationen

**Files:**
- Modify: `NetlifyPage/index.html` — JS-Block (Showcase-ScrollTrigger + Geräte-Animationen)

- [ ] **Schritt 10.1: Showcase-JS einfügen**

Nach dem `/* SCROLL REVEAL: CONTACT */`-Block im JS, einfügen:

```js
    /* ==========================================
       DEVICE SHOWCASE — HORIZONTAL PIN SCROLL
    ========================================== */
    (function() {
      var isMobile = window.innerWidth < 768;
      if (isMobile) {
        // Mobile: simple fadeInUp per panel
        [0, 1, 2].forEach(function(i) {
          gsap.from('#panel' + i, {
            scrollTrigger: { trigger: '#panel' + i, start: 'top 80%' },
            opacity: 0,
            y: 40,
            duration: 0.8,
            ease: 'power3.out'
          });
        });
        return;
      }

      var track   = document.getElementById('showcaseTrack');
      var outer   = document.getElementById('showcaseOuter');
      var section = document.getElementById('projects');
      var dots    = [
        document.getElementById('spDot0'),
        document.getElementById('spDot1'),
        document.getElementById('spDot2')
      ];

      // Set initial 3D state for each device wrap
      var startState = { rotateX: 28, rotateY: -12, scale: 0.82, opacity: 0 };
      gsap.set(['#devWrap0', '#devWrap1', '#devWrap2'], startState);

      // Horizontal track animation (scroll drives x translation)
      var trackAnim = gsap.to(track, {
        x: function() { return -(track.scrollWidth - window.innerWidth); },
        ease: 'none',
        scrollTrigger: {
          trigger: section,
          pin: true,
          scrub: 1,
          snap: {
            snapTo: 1 / 2,
            duration: { min: 0.3, max: 0.5 },
            ease: 'power2.inOut'
          },
          end: function() { return '+=' + track.scrollWidth; },
          onUpdate: function(self) {
            // Update progress dots
            var prog = self.progress;
            var active = prog < 0.33 ? 0 : prog < 0.66 ? 1 : 2;
            dots.forEach(function(d, i) {
              if (d) d.classList.toggle('active', i === active);
            });

            // Device entrance animations per panel
            // Panel 0: enter when progress 0→0.2
            var p0 = Math.min(1, prog / 0.2);
            gsap.set('#devWrap0', {
              rotateX: 28 * (1 - p0),
              rotateY: -12 * (1 - p0),
              scale: 0.82 + 0.24 * p0,
              opacity: p0
            });

            // Inner scroll for panel 0 (site scrolls when p0 > 0.5)
            var scroll0 = Math.max(0, (p0 - 0.5) / 0.5);
            gsap.set('#craftScroll', { y: -scroll0 * 25 + '%' });

            // Panel 1: enter when progress 0.3→0.55
            var p1 = Math.min(1, Math.max(0, (prog - 0.30) / 0.25));
            gsap.set('#devWrap1', {
              rotateX: 28 * (1 - p1),
              rotateY: -12 * (1 - p1),
              scale: 0.82 + 0.24 * p1,
              opacity: p1
            });
            var scroll1 = Math.max(0, (p1 - 0.5) / 0.5);
            gsap.set('#dentalScroll', { y: -scroll1 * 25 + '%' });

            // Panel 2: enter when progress 0.62→0.85
            var p2 = Math.min(1, Math.max(0, (prog - 0.62) / 0.23));
            gsap.set('#devWrap2', {
              rotateX: 28 * (1 - p2),
              rotateY: -12 * (1 - p2),
              scale: 0.82 + 0.24 * p2,
              opacity: p2
            });
            var scroll2 = Math.max(0, (p2 - 0.5) / 0.5);
            gsap.set('#restoScroll', { y: -scroll2 * 25 + '%' });
          }
        }
      });

      // Showcase header reveal
      gsap.to('#projectsLabel', {
        scrollTrigger: { trigger: section, start: 'top 80%' },
        opacity: 1, y: 0, duration: 0.6, ease: 'power3.out'
      });
      gsap.to('#projectsHeadline', {
        scrollTrigger: { trigger: section, start: 'top 75%' },
        opacity: 1, y: 0, duration: 0.7, ease: 'power3.out', delay: 0.1
      });
      gsap.to('#projectsNote', {
        scrollTrigger: { trigger: section, start: 'top 75%' },
        opacity: 1, y: 0, duration: 0.7, ease: 'power3.out', delay: 0.2
      });

      // Refresh on resize
      window.addEventListener('resize', function() {
        ScrollTrigger.refresh();
      }, { passive: true });
    }());
```

- [ ] **Schritt 10.2: `perspective` CSS-Variable am Wrapper setzen**

Die Device-Wraps brauchen `transform-style: preserve-3d` und `perspective` auf dem Elternelement. Im CSS, zum `.showcase-panel`-Block hinzufügen:

```css
    .showcase-panel {
      perspective: 700px;
    }
    .device-wrap {
      transform-style: preserve-3d;
      will-change: transform;
    }
```

- [ ] **Schritt 10.3: Prüfen**

Desktop-Browser, Fensterbreite > 768px. Zur `#projects`-Section scrollen. Checkliste:
- Section pinnt sich während des Scrollens
- Tablet-Panel (Handwerk) erscheint zuerst: kommt aus 3D-Schräge, richtet sich auf, zoomt leicht rein, Inhalt scrollt im Screen
- Weiterscrollen → Laptop-Panel (Zahnarzt, helle Site) schiebt von rechts rein mit gleicher Animation
- Weiterscrollen → Handy-Panel (Restaurant, amber-dunkel) erscheint zuletzt
- Fortschritts-Dots aktualisieren sich live
- Nach letztem Panel scrollt die Seite normal weiter

Mobile (Fenster < 768px): alle 3 Panels stapeln sich vertikal mit einfachem fadeIn.

- [ ] **Schritt 10.4: Commit**

```powershell
git add NetlifyPage/index.html
git commit -m "feat: device showcase GSAP horizontal scroll + 3D entrance animations"
```

---

## Abschluss-Checkliste

Vor dem Deployment auf Netlify:

- [ ] DevTools Network: keine Requests an `fonts.googleapis.com`
- [ ] Light Mode: Logo wechselt auf `amber-light`
- [ ] Cookie-Banner erscheint beim ersten Besuch, verschwindet nach Klick, erscheint nicht wieder
- [ ] Floating Constellations im Hero sichtbar und autonom
- [ ] Kontaktformular: alle 8 optionalen Felder erscheinen, URL-Feld konditionell, alle Labels DE/EN korrekt
- [ ] Service-Cards klickbar, führen zu korrekten Service-Seiten
- [ ] Alle 4 Service-Seiten: Logo, Theme, Sprache, Animationen, Zurück-Link funktionieren
- [ ] Device-Showcase: Pin, Horizontal-Scroll, 3D-Eingang, Progress-Dots, Mobile-Fallback
- [ ] `legal/impressum.html` und `legal/datenschutz.html` erreichbar
- [ ] Impressum: Adresse und USt-ID eintragen (manuell durch Hendrik)

```powershell
# Netlify Deploy (falls Netlify CLI installiert)
cd C:\Projekte\webzan\NetlifyPage
netlify deploy --prod --dir .
```
