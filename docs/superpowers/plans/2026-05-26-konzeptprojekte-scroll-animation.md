# Konzeptprojekte Scroll Animation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the horizontal-scroll device carousel in the Konzeptprojekte section with a vertically-pinned GSAP animation where all three devices are visible simultaneously, and each device in turn scales up to the center with its real website screenshot slowly scrolling inside.

**Architecture:** Single `NetlifyPage/index.html` file — three targeted edits: (1) CSS block replacement, (2) HTML section replacement, (3) JS IIFE replacement. Three webp images copied to `assets/projects/`. No new files created beyond the images.

**Tech Stack:** GSAP 3.12 + ScrollTrigger (already loaded), vanilla JS, CSS transforms

---

## File Map

| File | Change |
|---|---|
| `NetlifyPage/index.html` | CSS block, HTML section, JS IIFE — all replaced |
| `NetlifyPage/assets/projects/handwerk.webp` | New — copied from Downloads |
| `NetlifyPage/assets/projects/dental.webp` | New — copied from Downloads |
| `NetlifyPage/assets/projects/restaurant.webp` | New — copied from Downloads |

---

### Task 1: Copy images to assets

**Files:**
- Create dir: `NetlifyPage/assets/projects/`
- Create: `NetlifyPage/assets/projects/handwerk.webp`
- Create: `NetlifyPage/assets/projects/dental.webp`
- Create: `NetlifyPage/assets/projects/restaurant.webp`

- [ ] **Step 1: Create directory and copy files**

```powershell
New-Item -ItemType Directory -Force "C:\Projekte\webzan\NetlifyPage\assets\projects"
Copy-Item "C:\Users\handb\Downloads\original-1247d260ad951102d2d1af3f4aab4a06.webp" "C:\Projekte\webzan\NetlifyPage\assets\projects\handwerk.webp"
Copy-Item "C:\Users\handb\Downloads\original-ce85d1922032430e17f215b2429eb2c4.webp"  "C:\Projekte\webzan\NetlifyPage\assets\projects\dental.webp"
Copy-Item "C:\Users\handb\Downloads\original-769e0b86f702b69834898016b20738eb.webp"  "C:\Projekte\webzan\NetlifyPage\assets\projects\restaurant.webp"
```

- [ ] **Step 2: Verify files exist**

```powershell
Get-ChildItem "C:\Projekte\webzan\NetlifyPage\assets\projects\"
```

Expected output: three `.webp` files, each several hundred KB.

- [ ] **Step 3: Commit**

```bash
cd "C:/Projekte/webzan"
git add NetlifyPage/assets/projects/
git commit -m "Add project screenshot images for device showcase"
```

---

### Task 2: Replace CSS block

**Files:**
- Modify: `NetlifyPage/index.html` — CSS section between the `DEVICE SHOWCASE` comment and `</style>`

The existing block starts at the comment `/* ============ DEVICE SHOWCASE — HORIZONTAL PIN SCROLL` and runs to the `@media (max-width: 767px)` block that contains `.showcase-track`. Replace everything from that comment through the closing `</style>` tag of that block.

- [ ] **Step 1: Remove old showcase CSS and insert new**

Find this entire block in index.html (starting around line 1307):

```css
    /* ============================================
       DEVICE SHOWCASE — HORIZONTAL PIN SCROLL
    ============================================ */
    .showcase { position: relative; overflow: hidden; }
    .showcase-header { padding: clamp(60px,8vw,100px) 0 48px; }
    .showcase-track-outer { overflow: hidden; position: relative; }
    .showcase-track { display: flex; will-change: transform; }
    .showcase-panel {
```

…all the way through to the end of that CSS block (the closing `}` of the `@media (max-width: 767px)` rule that includes `.showcase-track`), and replace it with:

```css
    /* ============================================
       DEVICE SHOWCASE — PIN SCROLL
    ============================================ */
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

    .dev-shell--tablet {
      width: 180px; height: 240px;
      background: #0d0d10;
      border-radius: 14px;
      border: 2px solid #2a2a30;
      box-shadow: 0 24px 60px rgba(0,0,0,0.55);
      overflow: hidden;
      position: relative;
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

    .dev-screen {
      position: absolute; inset: 6px;
      overflow: hidden;
      border-radius: inherit;
    }
    .dev-laptop-body .dev-screen { inset: 5px; border-radius: 3px; }
    .dev-screen img {
      width: 100%;
      height: auto;
      display: block;
      will-change: transform;
    }

    .device-label { text-align: center; }
    .device-industry { font-size: 1rem; font-weight: 800; letter-spacing: -0.02em; color: var(--text); }
    .device-type { font-size: 11px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); margin-top: 4px; }

    @media (max-width: 767px) {
      .devices-row { flex-direction: column; gap: 40px; padding: 32px 0 48px; }
    }
```

- [ ] **Step 2: Verify in browser — open `http://localhost:8080`**

The Konzeptprojekte section should show three small device frames side by side with a broken image icon in each (images not wired up in HTML yet). No horizontal scroll. Labels visible below each device.

---

### Task 3: Replace HTML structure

**Files:**
- Modify: `NetlifyPage/index.html` — the `<section class="showcase">` block

- [ ] **Step 1: Replace the showcase-track-outer div and its contents**

Find this opening tag inside `<section class="showcase" id="projects">`:

```html
    <div class="showcase-track-outer" id="showcaseOuter">
      <div class="showcase-track" id="showcaseTrack">
```

…and everything through the closing `</div></div>` of that structure (ends just before `</section>`), replacing it with:

```html
    <div class="devices-row" id="devicesRow">

      <div class="dev-item" id="devItem0">
        <div class="dev-shell dev-shell--tablet" id="devShell0">
          <div class="dev-screen">
            <img src="assets/projects/handwerk.webp" alt="Handwerk Konzept" id="devImg0" loading="lazy">
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
                <img src="assets/projects/dental.webp" alt="Zahnarzt Konzept" id="devImg1" loading="lazy">
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
            <img src="assets/projects/restaurant.webp" alt="Restaurant Konzept" id="devImg2" loading="lazy">
          </div>
        </div>
        <div class="device-label">
          <div class="device-industry" id="panel2Industry"></div>
          <div class="device-type" id="panel2Type"></div>
        </div>
      </div>

    </div>
```

- [ ] **Step 2: Verify in browser — reload `http://localhost:8080`**

Three device frames with actual screenshots visible inside them. Tablet (handwerk), Laptop (dental), Phone (restaurant). Labels show industry names. No horizontal scroll behaviour.

- [ ] **Step 3: Commit**

```bash
cd "C:/Projekte/webzan"
git add NetlifyPage/index.html
git commit -m "Replace showcase HTML/CSS: devices-row layout with real screenshots"
```

---

### Task 4: Replace JS IIFE

**Files:**
- Modify: `NetlifyPage/index.html` — the showcase JS IIFE (around line 3117)

- [ ] **Step 1: Replace the showcase IIFE**

Find this entire block:

```js
    /* ==========================================
       DEVICE SHOWCASE — HORIZONTAL PIN SCROLL
    ========================================== */
    (function() {
      var isMobile = window.innerWidth < 768;
      if (isMobile) {
```

…through its closing `}());` (the block ends just before the `/* COOKIE CONSENT BANNER */` comment), and replace with:

```js
    /* ==========================================
       DEVICE SHOWCASE — PIN SCROLL
    ========================================== */
    (function() {
      var section = document.getElementById('projects');
      if (!section) return;

      var isMobile = window.innerWidth < 768;
      if (isMobile) {
        ['#devItem0','#devItem1','#devItem2'].forEach(function(sel) {
          gsap.from(sel, {
            scrollTrigger: { trigger: sel, start: 'top 85%' },
            opacity: 0, y: 30, duration: 0.7, ease: 'power3.out'
          });
        });
        return;
      }

      var SCALE_FOCUS = 2.2;
      var OPACITY_DIM = 0.22;

      function getCenterOffset(el) {
        var row    = document.getElementById('devicesRow').getBoundingClientRect();
        var rect   = el.getBoundingClientRect();
        var rowMid = row.left + row.width / 2;
        var elMid  = rect.left + rect.width / 2;
        return rowMid - elMid;
      }

      var tl = gsap.timeline({
        scrollTrigger: {
          trigger: section,
          pin: true,
          scrub: 1,
          end: '+=300vh',
          onRefresh: function() { tl.invalidate(); }
        }
      });

      /* Phase 0–20 %: Eingang */
      tl.from(['#devItem0','#devItem1','#devItem2'], {
        opacity: 0, y: 40, stagger: 0.08, duration: 0.2
      });

      /* Phase 20–40 %: Gerät 0 (Tablet — Handwerk) */
      tl.to('#devItem0', {
            scale: SCALE_FOCUS,
            x: function() { return getCenterOffset(document.getElementById('devItem0')); },
            duration: 0.18, ease: 'power2.inOut'
          }, 0.2)
        .to(['#devItem1','#devItem2'], { opacity: OPACITY_DIM, duration: 0.12 }, 0.2)
        .to('#devImg0', { y: '-40%', ease: 'none', duration: 0.18 }, 0.22)
        .to('#devItem0', { scale: 1, x: 0, duration: 0.14, ease: 'power2.inOut' }, 0.38)
        .to(['#devItem1','#devItem2'], { opacity: 1, duration: 0.1 }, 0.38);

      /* Phase 40–60 %: Gerät 1 (Laptop — Zahnarzt) */
      tl.to('#devItem1', { scale: SCALE_FOCUS, duration: 0.18, ease: 'power2.inOut' }, 0.4)
        .to(['#devItem0','#devItem2'], { opacity: OPACITY_DIM, duration: 0.12 }, 0.4)
        .to('#devImg1', { y: '-40%', ease: 'none', duration: 0.18 }, 0.42)
        .to('#devItem1', { scale: 1, duration: 0.14, ease: 'power2.inOut' }, 0.58)
        .to(['#devItem0','#devItem2'], { opacity: 1, duration: 0.1 }, 0.58);

      /* Phase 60–80 %: Gerät 2 (Phone — Restaurant) */
      tl.to('#devItem2', {
            scale: SCALE_FOCUS,
            x: function() { return getCenterOffset(document.getElementById('devItem2')); },
            duration: 0.18, ease: 'power2.inOut'
          }, 0.6)
        .to(['#devItem0','#devItem1'], { opacity: OPACITY_DIM, duration: 0.12 }, 0.6)
        .to('#devImg2', { y: '-40%', ease: 'none', duration: 0.18 }, 0.62)
        .to('#devItem2', { scale: 1, x: 0, duration: 0.14, ease: 'power2.inOut' }, 0.78)
        .to(['#devItem0','#devItem1'], { opacity: 1, duration: 0.1 }, 0.78);

      /* Phase 80–100 %: Ausgang */
      tl.to(['#devItem0','#devItem1','#devItem2'], {
        opacity: 0, duration: 0.15
      }, 0.85);

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

      window.addEventListener('resize', function() {
        ScrollTrigger.refresh();
      }, { passive: true });
    }());
```

- [ ] **Step 2: Verify in browser — reload `http://localhost:8080`, scroll to Konzeptprojekte**

Expected behaviour:
- Section pins while scrolling
- Tablet (Handwerk) scales up and moves to center first, screenshot scrolls inside, then retreats
- Laptop (Zahnarzt) scales up from center, screenshot scrolls, retreats
- Phone (Restaurant) scales up and moves to center, screenshot scrolls, retreats
- Other two devices dim to ~22% opacity during each focus phase
- All three fade out at the end before section unpins

- [ ] **Step 3: Commit**

```bash
cd "C:/Projekte/webzan"
git add NetlifyPage/index.html
git commit -m "Add GSAP pin timeline for device showcase scroll animation"
```

---

### Task 5: Fine-tune image scroll depth

**Files:**
- Modify: `NetlifyPage/index.html` — the three `y: '-40%'` values in the JS IIFE

The `-40%` is a GSAP `translateY` on the `<img>` element, as a percentage of the **img's own height**. Since the images are much taller than their container (website screenshots), this moves them down in the frame to reveal more content. The correct value depends on each image's aspect ratio vs the device frame ratio. Adjust after visual inspection.

- [ ] **Step 1: Check each device visually**

Open `http://localhost:8080`, scroll to each focus phase. For each device, note:
- Does the image start at the top (hero visible)?
- Does it scroll far enough to show meaningful content below the fold?
- Does it scroll too far (blank space at bottom)?

Target: image starts at top of the screenshot, scrolls to reveal approximately 50–60% of the full page height.

- [ ] **Step 2: Adjust y values if needed**

In the JS IIFE, the three image scroll lines are:

```js
.to('#devImg0', { y: '-40%', ease: 'none', duration: 0.18 }, 0.22)  // Handwerk tablet
.to('#devImg1', { y: '-40%', ease: 'none', duration: 0.18 }, 0.42)  // Dental laptop
.to('#devImg2', { y: '-40%', ease: 'none', duration: 0.18 }, 0.62)  // Restaurant phone
```

Typical adjustments:
- If image doesn't scroll far enough → increase magnitude: `-50%`, `-55%`
- If image overshoots (blank at bottom) → reduce: `-30%`, `-25%`
- Each device can have its own value — they are independent

- [ ] **Step 3: Commit after tuning**

```bash
cd "C:/Projekte/webzan"
git add NetlifyPage/index.html
git commit -m "Tune device image scroll depths for showcase animation"
```

---

### Task 6: Final check and push

- [ ] **Step 1: Full page walkthrough at `http://localhost:8080`**

Check these in order:
1. Hero section — wZ animation still renders ✓
2. Scroll into Konzeptprojekte — section header fades in ✓
3. Section pins — all three devices appear ✓
4. Tablet focus — scales to center, Handwerk screenshot scrolls ✓
5. Laptop focus — scales up in place, Dental screenshot scrolls ✓
6. Phone focus — scales to center, Restaurant screenshot scrolls ✓
7. Section unpins — scroll continues to next section ✓
8. Mobile view (resize to <768px) — vertical stack, no pin, fade-in per device ✓
9. Dark mode toggle — device frames and labels adapt correctly ✓

- [ ] **Step 2: Push to GitHub**

```bash
cd "C:/Projekte/webzan"
git push origin master
```

Netlify auto-deploys on credits reset (May 29).
