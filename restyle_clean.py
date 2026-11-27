# Script to restyle the site with a clean, high-signal, zero-gradient developer docs aesthetic (GitHub/Linear/MDN style)
import re

with open('build_master_hub.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the entire <style> ... </style> block with a clean, flat, minimalist, professional developer theme
clean_css = """<style>
    :root {
      --bg: #0d1117;
      --surface: #161b22;
      --surface-subtle: #21262d;
      --border: #30363d;
      --border-muted: #21262d;
      --text: #f0f6fc;
      --text-muted: #8b949e;
      --text-dim: #6e7681;
      --link: #58a6ff;
      --success: #3fb950;
      --danger: #f85149;
      --warning: #d29922;
      --code-bg: #090d13;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
      --sidebar-w: 260px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      font-family: var(--font-sans);
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      display: flex;
      min-height: 100vh;
      overflow-x: hidden;
      padding-bottom: env(safe-area-inset-bottom, 20px);
    }

    /* Scrollbars */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: var(--bg);
    }
    ::-webkit-scrollbar-thumb {
      background: var(--border);
      border-radius: 3px;
    }

    /* Clean Sidebar */
    aside.sidebar {
      width: var(--sidebar-w);
      background: #090d13;
      border-right: 1px solid var(--border);
      position: fixed;
      top: 0;
      bottom: 0;
      left: 0;
      overflow-y: auto;
      padding: 20px 14px;
      display: flex;
      flex-direction: column;
      z-index: 100;
      transition: transform 0.2s ease;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border);
      margin-bottom: 16px;
    }

    .brand-logo {
      width: 32px;
      height: 32px;
      background: #21262d;
      border: 1px solid var(--border);
      border-radius: 6px;
      display: grid;
      place-items: center;
      font-weight: 700;
      font-size: 14px;
      color: var(--text);
      font-family: var(--font-mono);
    }

    .brand-title {
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--text);
      line-height: 1.2;
    }

    .brand-sub {
      font-size: 0.72rem;
      color: var(--text-muted);
      font-family: var(--font-mono);
    }

    .nav-group-title {
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-dim);
      margin: 16px 8px 6px;
      font-weight: 700;
    }

    .nav-link {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 10px;
      border-radius: 6px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 500;
      transition: all 0.15s ease;
      margin-bottom: 2px;
    }

    .nav-link:hover, .nav-link.active {
      background: var(--surface);
      color: var(--text);
    }

    .nav-badge {
      margin-left: auto;
      background: var(--surface-subtle);
      border: 1px solid var(--border);
      color: var(--text-muted);
      font-size: 0.68rem;
      padding: 1px 6px;
      border-radius: 4px;
      font-family: var(--font-mono);
    }

    /* Main Container */
    main.content {
      margin-left: var(--sidebar-w);
      flex: 1;
      padding: 28px 40px 100px;
      max-width: 1100px;
    }

    @media (max-width: 960px) {
      aside.sidebar {
        transform: translateX(-100%);
      }
      aside.sidebar.open {
        transform: translateX(0);
      }
      main.content {
        margin-left: 0;
        padding: 16px 16px 90px;
      }
      .mobile-toggle {
        display: block !important;
      }
    }

    .mobile-toggle {
      display: none;
      position: fixed;
      bottom: 74px;
      right: 16px;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text);
      border-radius: 8px;
      width: 44px;
      height: 44px;
      font-size: 20px;
      z-index: 150;
      cursor: pointer;
    }

    /* Clean Search Bar */
    .top-search-bar {
      display: flex;
      align-items: center;
      gap: 10px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 8px 14px;
      margin-bottom: 24px;
    }

    .top-search-bar input {
      flex: 1;
      background: transparent;
      border: none;
      outline: none;
      color: var(--text);
      font-size: 0.9rem;
      font-family: inherit;
    }

    .top-search-bar input::placeholder {
      color: var(--text-dim);
    }

    /* Clean Filter Pills */
    .quick-filter-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 24px;
    }

    .pill-btn {
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 5px 12px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .pill-btn:hover, .pill-btn.active {
      background: var(--surface-subtle);
      border-color: var(--text-dim);
      color: var(--text);
    }

    /* Clean Hero Box (Solid, Flat, Minimalist) */
    .hero {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 24px;
      margin-bottom: 32px;
    }

    .hero-badge {
      display: inline-block;
      background: #21262d;
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 600;
      font-family: var(--font-mono);
      margin-bottom: 12px;
    }

    .hero h1 {
      font-size: 1.85rem;
      font-weight: 700;
      color: var(--text);
      letter-spacing: -0.02em;
      margin-bottom: 8px;
    }

    .hero p {
      font-size: 0.95rem;
      color: var(--text-muted);
      max-width: 800px;
      margin-bottom: 18px;
    }

    .stats-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
      gap: 10px;
      margin-top: 16px;
      border-top: 1px solid var(--border);
      padding-top: 16px;
    }

    .stat-card {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 10px 14px;
      text-align: left;
    }

    .stat-num {
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--text);
      font-family: var(--font-mono);
    }

    .stat-label {
      font-size: 0.72rem;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      font-weight: 600;
    }

    /* Sections */
    section {
      margin-bottom: 48px;
      scroll-margin-top: 20px;
    }

    .section-header {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 14px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border);
    }

    .section-num {
      width: 28px;
      height: 28px;
      background: var(--surface-subtle);
      border: 1px solid var(--border);
      border-radius: 6px;
      display: grid;
      place-items: center;
      font-weight: 700;
      font-size: 0.85rem;
      color: var(--text);
      font-family: var(--font-mono);
    }

    .section-header h2 {
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--text);
    }

    .section-desc {
      color: var(--text-muted);
      margin-bottom: 18px;
      font-size: 0.92rem;
    }

    /* Flat Cards */
    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 20px;
      margin-bottom: 18px;
    }

    .card h3 {
      font-size: 1.1rem;
      font-weight: 600;
      margin-bottom: 12px;
      color: var(--text);
    }

    .grid-2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 14px;
    }

    /* Table Design (Clean GitHub Style) */
    .table-container {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      margin: 12px 0;
      border: 1px solid var(--border);
      border-radius: 6px;
    }

    .custom-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }

    .custom-table th, .custom-table td {
      border: 1px solid var(--border);
      padding: 8px 12px;
      text-align: left;
    }

    .custom-table th {
      background: #090d13;
      color: var(--text);
      font-weight: 600;
    }

    .custom-table tr:nth-child(even) {
      background: rgba(255, 255, 255, 0.02);
    }

    /* Code Blocks */
    .code-wrapper {
      position: relative;
      margin: 12px 0;
      border: 1px solid var(--border);
      border-radius: 6px;
      overflow: hidden;
    }

    .code-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #090d13;
      border-bottom: 1px solid var(--border);
      padding: 6px 12px;
      font-size: 0.75rem;
      font-family: var(--font-mono);
      color: var(--text-dim);
    }

    .code-header .code-lang {
      color: var(--text-muted);
      font-weight: 600;
    }

    .code-header .btn-copy {
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 0.72rem;
      cursor: pointer;
      font-family: var(--font-mono);
    }

    .code-header .btn-copy:hover {
      color: var(--text);
      background: var(--surface-subtle);
    }

    .code-header .btn-copy.copied {
      color: var(--success);
      border-color: var(--success);
    }

    pre {
      background: var(--code-bg);
      padding: 12px 14px;
      overflow-x: auto;
      font-family: var(--font-mono);
      font-size: 0.85rem;
      line-height: 1.55;
      color: #e6edf3;
      margin: 0;
    }

    code {
      font-family: var(--font-mono);
      font-size: 0.88em;
      background: #21262d;
      color: #e6edf3;
      padding: 2px 5px;
      border-radius: 4px;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }

    pre code {
      background: transparent;
      color: inherit;
      padding: 0;
      border: none;
    }

    /* Callouts (Flat, Solid Border) */
    .callout {
      border: 1px solid var(--border);
      border-left: 3px solid;
      border-radius: 4px;
      padding: 12px 14px;
      margin: 14px 0;
      font-size: 0.9rem;
      background: var(--surface);
    }

    .callout-warning {
      border-left-color: var(--warning);
    }

    .callout-danger {
      border-left-color: var(--danger);
    }

    .callout-tip {
      border-left-color: var(--success);
    }

    .callout-info {
      border-left-color: var(--link);
    }

    .callout strong {
      display: block;
      margin-bottom: 4px;
      font-weight: 600;
      font-size: 0.92rem;
      color: var(--text);
    }

    /* Flat Slicing Visualizer */
    .visualizer-container {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 20px;
      margin: 16px 0;
    }

    .preset-btns {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 16px;
    }

    .preset-btn {
      background: var(--bg);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 4px 10px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      cursor: pointer;
    }

    .preset-btn:hover {
      background: var(--surface-subtle);
      color: var(--text);
      border-color: var(--text-dim);
    }

    .slice-inputs {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 16px;
    }

    .input-group {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .input-group label {
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text-muted);
      font-family: var(--font-mono);
    }

    .input-group input {
      background: var(--bg);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 7px 10px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 0.88rem;
      outline: none;
    }

    .input-group input:focus {
      border-color: var(--link);
    }

    .visual-indices {
      display: flex;
      flex-wrap: nowrap;
      overflow-x: auto;
      gap: 6px;
      padding: 12px 0;
      margin-bottom: 14px;
    }

    .char-box {
      min-width: 42px;
      display: flex;
      flex-direction: column;
      align-items: center;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 6px 4px;
    }

    .char-box.selected {
      background: #1c2d42;
      border-color: var(--link);
    }

    .char-box .char-val {
      font-size: 1.2rem;
      font-weight: 700;
      font-family: var(--font-mono);
      color: var(--text);
      margin: 2px 0;
    }

    .char-box .pos-idx {
      font-size: 0.7rem;
      color: var(--success);
      font-family: var(--font-mono);
    }

    .char-box .neg-idx {
      font-size: 0.7rem;
      color: var(--danger);
      font-family: var(--font-mono);
    }

    .slice-result {
      background: var(--code-bg);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 12px 14px;
      font-family: var(--font-mono);
      font-size: 0.95rem;
      color: var(--text);
    }

    /* Stack Demo */
    .stack-demo-container {
      display: flex;
      flex-direction: column;
      gap: 8px;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 14px;
      margin: 14px 0;
    }

    .stack-frame {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 10px 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .stack-frame.active {
      border-color: var(--link);
      background: #172338;
    }

    /* Accordions */
    .accordion {
      border: 1px solid var(--border);
      border-radius: 6px;
      margin-bottom: 10px;
      overflow: hidden;
      background: var(--surface);
    }

    .accordion-header {
      padding: 14px 16px;
      background: var(--surface);
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-weight: 600;
      font-size: 0.92rem;
      user-select: none;
    }

    .accordion-header:hover {
      background: var(--surface-subtle);
    }

    .accordion-icon {
      font-size: 0.85rem;
      color: var(--text-dim);
      transition: transform 0.2s ease;
    }

    .accordion.open .accordion-icon {
      transform: rotate(180deg);
    }

    .accordion-body {
      padding: 16px;
      display: none;
      border-top: 1px solid var(--border);
      background: var(--bg);
    }

    .accordion.open .accordion-body {
      display: block;
    }

    /* Flat Flashcards */
    .flashcards-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 14px;
      margin-top: 16px;
    }

    .flashcard {
      min-height: 200px;
      perspective: 1000px;
      cursor: pointer;
    }

    .flashcard-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.4s ease;
      transform-style: preserve-3d;
      border-radius: 6px;
    }

    .flashcard.flipped .flashcard-inner {
      transform: rotateY(180deg);
    }

    .flashcard-front, .flashcard-back {
      position: absolute;
      width: 100%;
      height: 100%;
      -webkit-backface-visibility: hidden;
      backface-visibility: hidden;
      border-radius: 6px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      border: 1px solid var(--border);
    }

    .flashcard-front {
      background: var(--surface);
      color: var(--text);
    }

    .flashcard-front h4 {
      font-size: 0.98rem;
      margin-bottom: 6px;
      color: var(--text);
    }

    .flashcard-front p {
      font-size: 0.88rem;
      color: var(--text-muted);
    }

    .flashcard-back {
      background: #111a28;
      color: var(--text);
      transform: rotateY(180deg);
      border-color: var(--link);
      font-size: 0.85rem;
      line-height: 1.5;
    }

    /* Flat Quiz */
    .quiz-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 20px;
      margin-bottom: 18px;
    }

    .quiz-q {
      font-size: 1.02rem;
      font-weight: 600;
      margin-bottom: 14px;
      color: var(--text);
      line-height: 1.5;
    }

    .quiz-options {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .quiz-opt {
      background: var(--bg);
      border: 1px solid var(--border);
      padding: 10px 14px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 0.9rem;
      transition: all 0.15s ease;
      display: flex;
      align-items: center;
      gap: 10px;
      min-height: 44px;
    }

    .quiz-opt:hover {
      background: var(--surface-subtle);
      border-color: var(--text-dim);
    }

    .quiz-opt.correct {
      background: #0f2d1e !important;
      border-color: var(--success) !important;
      color: #7ee787;
      font-weight: 600;
    }

    .quiz-opt.incorrect {
      background: #361418 !important;
      border-color: var(--danger) !important;
      color: #ffa198;
    }

    .quiz-explanation {
      margin-top: 14px;
      padding: 12px 14px;
      background: var(--bg);
      border-left: 3px solid var(--link);
      border-radius: 0 4px 4px 0;
      font-size: 0.88rem;
      color: var(--text-muted);
      display: none;
    }

    .quiz-progress-bar {
      height: 6px;
      background: var(--surface-subtle);
      border-radius: 3px;
      margin-bottom: 18px;
      overflow: hidden;
    }

    .quiz-progress-fill {
      height: 100%;
      background: var(--link);
      width: 0%;
      transition: width 0.25s ease;
    }

    .score-banner {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 16px 20px;
      margin-bottom: 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }

    .btn-retake {
      background: var(--surface-subtle);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 6px 14px;
      border-radius: 4px;
      font-weight: 600;
      font-size: 0.82rem;
      cursor: pointer;
    }

    .btn-retake:hover {
      background: var(--border);
    }

    /* Minimalist Mobile Dock */
    .mobile-dock {
      display: none;
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      height: 56px;
      background: #090d13;
      border-top: 1px solid var(--border);
      z-index: 999;
      justify-content: space-around;
      align-items: center;
      padding: 0 8px calc(env(safe-area-inset-bottom, 0px) + 2px);
    }

    .dock-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.68rem;
      font-weight: 600;
      cursor: pointer;
      padding: 4px 8px;
    }

    .dock-item:hover, .dock-item.active {
      color: var(--text);
    }

    .dock-item .dock-icon {
      font-size: 1.1rem;
    }

    @media (max-width: 960px) {
      .mobile-dock {
        display: flex;
      }
      main.content {
        padding-bottom: 90px !important;
      }
      .mobile-toggle {
        bottom: 70px !important;
      }
    }

    .back-to-top {
      position: fixed;
      bottom: 74px;
      left: 16px;
      width: 40px;
      height: 40px;
      border-radius: 6px;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text);
      display: grid;
      place-items: center;
      font-size: 1.1rem;
      cursor: pointer;
      z-index: 120;
      opacity: 0;
      visibility: hidden;
      transition: all 0.2s ease;
    }

    .back-to-top.show {
      opacity: 1;
      visibility: visible;
    }

    /* Print */
    @media print {
      aside.sidebar, .mobile-toggle, .visualizer-container, .flashcards-container, .top-search-bar, .quick-filter-pills, .btn-retake, .mobile-dock, .back-to-top {
        display: none !important;
      }
      main.content {
        margin: 0 !important;
        padding: 0 !important;
        max-width: 100% !important;
      }
      body {
        background: #fff;
        color: #000;
      }
      .card, .hero, .quiz-card {
        border: 1px solid #ccc;
        background: #fff;
        color: #000;
      }
      pre {
        background: #f6f8fa;
        color: #000;
        border: 1px solid #ddd;
      }
    }
  </style>"""

# Replace in text: find existing <style>...</style> and replace with clean_css
pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
text = pattern.sub(clean_css, text)

# Also remove inline linear-gradient from hero badge or brand logo if any
text = text.replace('background: linear-gradient(135deg, #0284c7, #4f46e5);', 'background: #21262d;')
text = text.replace('background: linear-gradient(135deg, #0284c7, #6366f1);', 'background: #21262d;')
text = text.replace('background: linear-gradient(90deg, #38bdf8, #6366f1);', 'background: var(--link);')

with open('build_master_hub.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Restyled build_master_hub.py cleanly: zero gradients, clean developer docs theme!")
