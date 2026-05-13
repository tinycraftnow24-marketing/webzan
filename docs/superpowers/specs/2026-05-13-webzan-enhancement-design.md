# WebZan.de Enhancement — Design Spec
**Datum:** 2026-05-13  
**Hosting:** Netlify (Static HTML/CSS/JS — kein Framework, kein Build-Step)  
**Hauptdatei:** `NetlifyPage/index.html` (bisher `mockup-orbit.html`)  
**Libraries:** GSAP 3.12 · ScrollTrigger · Lenis 1.0 (alle CDN)

---

## Entschiedene Architektur

```
NetlifyPage/
  index.html                        ← bisherige mockup-orbit.html
  assets/
    logo/                           ← vorhanden
    fonts/                          ← NEU: Inter self-hosted
      inter-400.woff2
      inter-600.woff2
      inter-700.woff2
      inter-900.woff2
  services/
    wordpress.html                  ← NEU
    motion.html                     ← NEU
    landing-page.html               ← NEU
    ui-ux.html                      ← NEU
  legal/
    impressum.html                  ← NEU (deployed)
    datenschutz.html                ← NEU (aktualisiert)
```

---

## Feature 1 — Mehrsprachigkeit DE / EN

**Status:** Bereits vollständig implementiert.  
`localStorage.getItem('lang') || 'de'` — Default Deutsch korrekt.  
**Aufwand:** Nur verifizieren. Neue Felder (Kontaktformular, Service-Seiten) ins `content`-Objekt ergänzen.

---

## Feature 2 — Dark / Light Mode

**Status:** CSS-Vars für beide Themes vorhanden. Ein Fehler zu korrigieren:

```js
// AKTUELL (falsch):
img.src = t === 'dark' ? 'assets/logo/webzan-logo-amber-dark-1024.png'
                       : 'assets/logo/webzan-logo-transparent-1024.png';

// KORREKT:
img.src = t === 'dark' ? 'assets/logo/webzan-logo-amber-dark-1024.png'
                       : 'assets/logo/webzan-logo-amber-light-1024.png';
```

`webzan-logo-amber-light-1024.png` liegt unter `C:\Projekte\webzan\Logo\` und muss nach `NetlifyPage/assets/logo/` kopiert werden.

---

## Feature 3 — Hintergrund-Animation (Floating Constellations)

**Entschieden:** Stil C — Floating Constellations.

**Implementierung:** `<canvas>` hinter dem Hero-Content, `z-index: -1`.

```
- 35 Nodes, autonome Bewegung via requestAnimationFrame
- Farbe: rgba(232, 184, 75, alpha) — Amber
- Linien zwischen Nodes wenn Abstand < 80px, Opacity proportional zur Nähe
- Linienstärke: 0.6px
- Keine Maus-Interaktion
- Performance: canvas.style.willChange = 'transform'
- Respektiert prefers-reduced-motion: Animation pausiert wenn aktiv
```

Auf Service-Detailseiten: gleiche Animation, aber 20 Nodes und 40% geringere Opacity (weniger Ablenkung).

---

## Feature 4 — Erweitertes Kontaktformular

**Neue optionale Felder** (in dieser Reihenfolge, nach Name/E-Mail/Nachricht):

### Block "Dein Projekt"
| Feld | Typ | Optionen |
|------|-----|---------|
| Existiert bereits eine Website? | Radio | Ja / Nein |
| Falls ja, welche URL? | Text-Input | Erscheint nur wenn Ja (CSS transition `max-height`) |
| Projektumfang | Select | Neue Website · Redesign / Relaunch · Landing Page · UI/UX Beratung · Noch unklar |
| Branche | Select | Restaurant/Gastronomie · Zahnarzt/Medizin · Handwerk/Bau · Einzelhandel · Dienstleistung · Startup/Tech · Andere |
| Wunsch-Zeitrahmen | Select | So bald wie möglich · 1–3 Monate · 3–6 Monate · Noch flexibel |
| Hauptziel der Website | Select | Anfragen/Leads generieren · Online-Termine buchen · Produkte verkaufen · Marke/Portfolio aufbauen · Bestehende Seite aktualisieren · Noch unklar |

### Block "Noch etwas"
| Feld | Typ | Hinweis |
|------|-----|---------|
| Inspirations-URLs | Textarea | Placeholder: "z.B. apple.com, studio.com — Seiten die dir gefallen" |
| Wie bist du auf mich gestoßen? | Select | Google · Empfehlung · Instagram/LinkedIn · Anderes |

**Alle Felder optional** — Netlify Forms empfängt alle Felder automatisch.  
**Vollständige i18n** — alle Labels, Placeholders, Options in `content.de` und `content.en`.  
**Konditionelles URL-Feld:** `max-height: 0 → 80px` via CSS, gesteuert per JS auf Radio-Change.

---

## Feature 5 — Service-Detailseiten (Option B)

4 separate HTML-Dateien unter `services/`. Jede teilt den gleichen CSS-Grundstock (inline oder shared `<link>`).

**Aufbau jeder Seite:**
```
Nav (identisch zur Hauptseite, mit Theme/Lang Toggle)
↓
Hero: Service-Name + 1-Satz-Tagline + GSAP Clip-Path Reveal
↓
Was ist das? — 2–3 konkrete Absätze
↓
Für wen? — 3 Bullet-Points mit SVG-Icon
↓
Mein Prozess — 3–4 Schritte (gleiche Optik wie Hauptseite)
↓
Beispiel — kleines Device-Mockup der passenden Branche (statisch)
↓
CTA: "Projekt anfragen →" (Link zu index.html#contact) + "← Zurück"
```

**Navigation zurück:** Pfeil-Link oben links + `history.back()` als Fallback.  
**Floating Constellations** im Hintergrund (reduziert, 20 Nodes).  
**Vollständig i18n** — alle 4 Seiten DE + EN.

| Datei | Service | Branche-Beispiel |
|-------|---------|-----------------|
| `services/wordpress.html` | WordPress Websites | Zahnarztpraxis |
| `services/motion.html` | Motion Websites | Restaurant |
| `services/landing-page.html` | Landing Pages | Handwerk |
| `services/ui-ux.html` | UI/UX & Branding | Allgemein |

Service-Cards in `index.html` erhalten `href="services/motion.html"` etc. + `cursor: pointer`.

---

## Feature 6 — DSGVO-Audit

**Gefundene Probleme & Lösungen:**

| Problem | Lösung |
|---------|--------|
| Google Fonts CDN (`fonts.googleapis.com`) überträgt IP ohne Einwilligung | Inter als `.woff2` self-hosted in `assets/fonts/` — 4 Schnitte (400/600/700/900) |
| GSAP + Lenis via CDN (cdnjs/jsdelivr) | Bleibt CDN — keine personenbezogenen Daten übertragen, kein Cookie gesetzt. Akzeptables Restrisiko, in Datenschutzerklärung erwähnen |
| Netlify Forms speichert Formular-Submissions | In Datenschutzerklärung dokumentieren: Verantwortlicher, Zweck, Speicherdauer, Netlify als Auftragsverarbeiter |
| `localStorage` für Theme/Sprache | Kein Einwilligung nötig — TTDSG §25 Abs. 2 Nr. 2 (technisch notwendig) |

**Font-Einbindung nach Fix:**
```css
@font-face {
  font-family: 'Inter';
  src: url('assets/fonts/inter-400.woff2') format('woff2');
  font-weight: 400;
  font-display: swap;
}
/* … je Schnitt */
```

---

## Feature 7 — Cookie Consent Banner

**Minimal-Banner** (Bottom-Bar, kein Modal — kein Tracking, daher kein Opt-In nötig):

```
┌─────────────────────────────────────────────────────────┐
│ Wir verwenden keine Tracking-Cookies. Formulardaten     │
│ werden von Netlify verarbeitet. [Datenschutz]  [OK]     │
└─────────────────────────────────────────────────────────┘
```

- Erscheint beim ersten Besuch (kein `localStorage('consent')` vorhanden)
- "OK" setzt `localStorage('consent', '1')` und blendet Banner aus
- `[Datenschutz]` → Link zu `legal/datenschutz.html`
- GSAP `slideInUp` Eingangsanimation (0.4s, von unten)
- Vollständig i18n (DE/EN)
- `z-index: 9999`, Position `fixed bottom-0`

---

## Feature 8 — Device Showcase (Horizontal Pin Scroll)

**Ersetzt** den bisherigen `projects`-Abschnitt in `index.html`.

### Scroll-Mechanik
GSAP ScrollTrigger mit `pin: true`. Die Section ist während des Durchscrollens fixiert. Vertikales Scrollen treibt horizontale Translation an (`scrub: 1`). Snap auf Panel-Grenzen (`snap: 1/2`).

```js
gsap.to(track, {
  x: () => -(track.scrollWidth - window.innerWidth),
  ease: 'none',
  scrollTrigger: {
    trigger: showcaseSection,
    pin: true,
    scrub: 1,
    snap: { snapTo: 1/2, duration: 0.4, ease: 'power2.inOut' },
    end: () => '+=' + track.scrollWidth
  }
});
```

### Device-Eingangs-Animation (pro Panel, scroll-getriggert)
Jedes Gerät startet in 3D-Schräge und richtet sich auf während es ins Viewport scrollt:

```
Start:  perspective(700px) rotateX(28°) rotateY(-12°) scale(0.82) — opacity 0
Phase 1: rotateX(0) rotateY(0) — Gerät richtet sich auf (scrub-proportional)
Phase 2: scale(1.06) — leichter Zoom rein
Phase 3: inner content translateY(-25%) — Seite scrollt im Screen
Ende:   scale(1) — kurz bevor nächstes Panel kommt
```

Panels sind versetzt: Panel 2 startet Animation wenn Panel 1 zu 60% fertig ist.

### Panel-Aufbau

| Panel | Gerät | Branche | Farbklima |
|-------|-------|---------|-----------|
| 01 (Start) | Tablet | Handwerk | Dunkelblau `#0e1825` / `#1e3a5a` |
| 02 (Mitte) | Laptop | Zahnarztpraxis | Hell `#f5f2ee` / `#2c4a6e` — wie thenoomo Cadence |
| 03 (Ende) | Handy | Restaurant | Amber-Dunkel `#1a1208` / `#E8B84B` |

Kein Branding, keine echten Logos — stilisierte Placeholder-Websites als HTML/CSS.

### Laptop-Stil (Referenz: thenoomo "Cadence")
- Dunkle Bezel, minimales Frame
- Leichte 3D-Perspektive `perspective(900px) rotateX(2°)` im Ruhezustand
- Klarer Kontrast: helles Website-Content auf dunklem Gerät

### Mobile Fallback
Unter 768px: kein Horizontal-Scroll. Panels stapeln sich vertikal, jedes Gerät erscheint mit einfachem `fadeInUp` beim Einrollen in den Viewport.

### Progress-Indikator
3 Punkte oben rechts in der Section (`●○○` → `○●○` → `○○●`), live aktualisiert per ScrollTrigger `onUpdate`.

---

## Implementierungs-Reihenfolge

| Phase | Features | Datei(en) |
|-------|----------|-----------|
| 1 — Sofort | DSGVO Fonts · Logo-Fix · Cookie-Banner | `index.html`, `assets/fonts/`, `legal/` |
| 2 — Kern | Dot-Animation · Formular-Erweiterung | `index.html` |
| 3 — Content | 4 Service-Detailseiten | `services/*.html` |
| 4 — WOW | Device-Showcase Horizontal Scroll | `index.html` |

---

## Offene Punkte (kein Design-Blocker)

- Inhalte der Service-Detailseiten (Texte DE/EN) — Hendrik liefert oder wir generieren gemeinsam
- Datenschutzerklärung finale Texte — muss juristisch geprüft werden (kein Rechtsrat durch Claude)
- `webzan-logo-amber-light-1024.png` muss nach `NetlifyPage/assets/logo/` kopiert werden
- Inter `.woff2` Dateien müssen heruntergeladen werden (google-webfonts-helper.herokuapp.com)
