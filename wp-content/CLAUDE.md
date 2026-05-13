# WebZan — WordPress.com Projekt

## Kontext

Website für Hendrik Zanzig / WebZan (Webdesign für KMU).
Hosting: **WordPress.com Premium** — Site ID `254472538`, Domain `web-zan.com` (intern: handballhendrik-hujre.wordpress.com).
Inhalte werden per **MCP-Tool** (`wpcom-mcp-content-authoring`) direkt eingespielt.

---

## Seiten-IDs

| Seite        | ID | URL                       |
|--------------|----|---------------------------|
| Startseite   | 31 | /startseite/ (Front Page) |
| Kontakt      | 33 | /kontakt/                 |
| Impressum    | 34 | /impressum/               |
| Datenschutz  | 35 | /datenschutz/             |

Page 31 ist als statische Frontpage eingestellt (Settings → Reading). Nie löschen — immer updaten, sonst muss Reading Settings manuell neu konfiguriert werden.

---

## Lokale Dateien

```
C:\Projekte\webzan\
  pages\
    startseite.html     # Vollständiger HTML-Content für Page 31 (~69KB)
    kontakt.html        # Page 33
    impressum.html      # Page 34
    datenschutz.html    # Page 35
  webzan-customizer.css # Muss manuell in WP Customizer eingefügt werden
```

---

## CSS-Delivery — KRITISCH

WordPress.com KSES entfernt `<style>`-Tags aus Page-Content. **Alle Animationen und CSS-Klassen müssen in den Customizer.**

**Pfad:** Darstellung → Anpassen → Zusätzliches CSS → Inhalt von `webzan-customizer.css` einfügen.

Aktuelle Version: **v2** — enthält alle `wz-*`-Klassen, alle `@keyframes`, CF7-Styling, Responsive-Breakpoints.

---

## Design-System

```
--navy:   #152342   (Hintergrund überall)
--blue:   #3D5AFE   (Primary Accent)
--blue2:  #536DFE   (Hover-Zustand)
--violet: #7B2FFF   (KI-Sektion)
--text:   #F0F2FF   (Haupttext)
--muted:  rgba(210,218,255,.62)  (Sekundärtext)
```

**Glassmorphism-Card-Muster:**
```css
background: rgba(255,255,255,.09);
border: 1px solid rgba(255,255,255,.16);
border-radius: 20px;
backdrop-filter: blur(12px);
```

**Typografie:**
- Hero H1: `clamp(2.8rem,8vw,7rem)` / `font-weight:900` / `letter-spacing:-.04em`
- Section H2: `clamp(1.8rem,4vw,3.2rem)` / `font-weight:900` / `letter-spacing:-.03em`
- Body: `.95rem` / `line-height:1.8`

---

## HTML-Regeln für Content

- **Keine `<style>`-Tags** — KSES entfernt sie
- **Keine `<script>`-Tags** — kein JS möglich
- **Keine Emojis** — verursachen JSON-Parse-Fehler (`Permission denied: params must be an object`). SVG-Icons stattdessen.
- **Keine `list-style:none`** auf `<ul>` inline — wird von KSES entfernt. Flex-Column als Ersatz.
- **HTML-Entities** für Sonderzeichen: `&#183;` `&#8212;` `&#9733;` `&#8364;` `&#8594;` `&#252;` `&#228;` etc.
- Alle wz-* CSS-Klassen können verwendet werden — sie sind im Customizer definiert.

---

## JS-Abhängige Features — nicht umsetzbar auf WP.com Premium

Diese Mockup-Features existieren im Original, wurden aber durch CSS-Alternativen ersetzt:

| Feature | Original | Ersatz |
|---|---|---|
| Canvas-Partikel | `<canvas>` Punktnetz mit requestAnimationFrame | CSS-Punktgitter `.wz-hero::before` + Orb-Blobs |
| Custom-Cursor | `#cursor` + `#cursor-ring` via mousemove | Standard-Cursor |
| IntersectionObserver | `.anim`-Klassen fade/slide beim Scrollen | CSS `animation-delay` gestaffelt beim Load (nur Hero) |
| Portfolio-Filter | Filter-Buttons Alle/Handwerk/etc. | Portfolio-Grid weggelassen |
| Counter-Animationen | 0→48, 0→5, 0→100 zählen | Statische Zahlen mit fadeUp-Animation |

---

## Aktive Plugins

Gutenberg 22.9, Contact Form 7 6.1.5 (Shortcode: `[contact-form-7 id="1"]`), Jetpack 15.8, Yoast SEO 27.4, ACF 6.8, Layout Grid 1.8.5, Akismet, UpdraftPlus, Custom Post Type UI, Crowdsignal, Gravatar Enhanced, Page Optimize, Big Sky.

CF7-Formular-ID im WP-Admin prüfen (Kontakt → Kontaktformulare). Wenn nicht `1`, Shortcode in kontakt.html anpassen.

---

## MCP-Upload-Regeln

- **Immer `pages.update`**, nie `pages.create` für die 4 Hauptseiten — Seiten existieren bereits.
- `include_fields: ["id", "status", "link"]` verwenden, sonst Response zu groß (119KB).
- Bei großem Content (>30KB) in der JSON-Payload: Umlaute als HTML-Entities kodieren (`ü` → `&#252;` etc.) oder direkt als Unicode — beides funktioniert.
- `user_confirmed` muss in params mitgegeben werden.

---

## Offene Todos (manuell durch Hendrik)

1. **Customizer CSS** aktualisieren — `webzan-customizer.css` v2 einfügen
2. **Adresse + USt-ID** in Impressum (Page 34) ergänzen
3. **CF7-ID** verifizieren
4. **Reading Settings** — Page 31 als Front Page bestätigt?

---

## Was Hendrik will

- **1:1 Umsetzung des Mockups** — keine eigenmächtigen Design-Entscheidungen, kein Abweichen ohne Rückfrage
- **Selbst prüfen vor Abgabe** — Probleme eigenständig erkennen und fixen, nicht erst nach Feedback
- **Korrekte Reihenfolge einhalten:** Erst Ist-Stand analysieren (Plugins, Zugänge, Constraints), dann konzipieren, dann umsetzen
- **Keine Emojis**, keine unnötigen Kommentare im Code
- **Motion/Dynamik ist wichtig** — fehlende Animationen sind ein Mangel, auch wenn technisch limitiert; CSS-Alternativen maximal ausschöpfen
- **Fonts und Typografie exakt** — falsche Schriftgrößen/Gewichte sind inakzeptabel
- **Direkte Antworten** — kein Recap, kein Entschuldigen, keine langen Vorreden
