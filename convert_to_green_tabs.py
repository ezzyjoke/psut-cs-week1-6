import re

with open('build_master_hub.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update CSS to Green Theme & Tabs System
green_css = """<style>
    :root {
      --bg: #070b09;
      --surface: #0e1511;
      --surface-subtle: #141f19;
      --border: #1a2c22;
      --border-focus: #3fb950;
      --border-muted: #132219;
      --text: #e6edf3;
      --text-muted: #8b9a90;
      --text-dim: #54655a;
      --link: #3fb950;
      --accent-green: #3fb950;
      --accent-green-bright: #2ea043;
      --success: #3fb950;
      --danger: #f85149;
      --warning: #d29922;
      --code-bg: #050806;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
      --sidebar-w: 250px;
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

    /* Clean Green Sidebar */
    aside.sidebar {
      width: var(--sidebar-w);
      background: #050806;
      border-right: 1px solid var(--border);
      position: fixed;
      top: 0;
      bottom: 0;
      left: 0;
      overflow-y: auto;
      padding: 18px 12px;
      display: flex;
      flex-direction: column;
      z-index: 100;
      transition: transform 0.2s ease;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border);
      margin-bottom: 14px;
    }

    .brand-logo {
      width: 32px;
      height: 32px;
      background: #141f19;
      border: 1px solid var(--accent-green);
      border-radius: 6px;
      display: grid;
      place-items: center;
      font-weight: 700;
      font-size: 13px;
      color: var(--accent-green);
      font-family: var(--font-mono);
    }

    .brand-title {
      font-weight: 700;
      font-size: 0.92rem;
      color: var(--text);
      line-height: 1.2;
    }

    .brand-sub {
      font-size: 0.7rem;
      color: var(--accent-green);
      font-family: var(--font-mono);
    }

    .nav-group-title {
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-dim);
      margin: 14px 6px 6px;
      font-weight: 700;
    }

    .nav-link {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 7px 10px;
      border-radius: 6px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 500;
      transition: all 0.15s ease;
      margin-bottom: 2px;
      cursor: pointer;
    }

    .nav-link:hover, .nav-link.active {
      background: var(--surface-subtle);
      color: var(--accent-green);
      border-left: 3px solid var(--accent-green);
    }

    .nav-badge {
      margin-left: auto;
      background: var(--surface-subtle);
      border: 1px solid var(--border);
      color: var(--accent-green);
      font-size: 0.66rem;
      padding: 1px 6px;
      border-radius: 4px;
      font-family: var(--font-mono);
    }

    /* Main Container */
    main.content {
      margin-left: var(--sidebar-w);
      flex: 1;
      padding: 24px 36px 90px;
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
        padding: 14px 14px 90px;
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
      color: var(--accent-green);
      border-radius: 6px;
      width: 44px;
      height: 44px;
      font-size: 20px;
      z-index: 150;
      cursor: pointer;
    }

    /* --- TOP TAB BAR (Tabbed UI, Zero Scroll Hell) --- */
    .tabs-header-bar {
      display: flex;
      gap: 6px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 6px;
      margin-bottom: 20px;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      position: sticky;
      top: 10px;
      z-index: 90;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    }

    .tab-btn {
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-muted);
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .tab-btn:hover {
      background: var(--surface-subtle);
      color: var(--text);
    }

    .tab-btn.active {
      background: var(--surface-subtle);
      border-color: var(--accent-green);
      color: var(--accent-green);
      font-weight: 700;
    }

    /* Tab Panes */
    .tab-pane {
      display: none;
      animation: tabFadeIn 0.15s ease-out;
    }

    .tab-pane.active {
      display: block;
    }

    @keyframes tabFadeIn {
      from { opacity: 0; transform: translateY(4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Search Bar */
    .top-search-bar {
      display: flex;
      align-items: center;
      gap: 10px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 8px 14px;
      margin-bottom: 18px;
    }

    .top-search-bar input {
      flex: 1;
      background: transparent;
      border: none;
      outline: none;
      color: var(--text);
      font-size: 0.88rem;
      font-family: inherit;
    }

    .top-search-bar input::placeholder {
      color: var(--text-dim);
    }

    /* Minimal Hero */
    .hero {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 18px 20px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }

    .hero-title-group h1 {
      font-size: 1.45rem;
      font-weight: 700;
      color: var(--text);
      letter-spacing: -0.01em;
    }

    .hero-title-group p {
      font-size: 0.88rem;
      color: var(--text-muted);
      margin-top: 2px;
    }

    .hero-stats-group {
      display: flex;
      gap: 8px;
    }

    .stat-pill {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 6px 12px;
      text-align: center;
    }

    .stat-num {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--accent-green);
      font-family: var(--font-mono);
      line-height: 1;
    }

    .stat-label {
      font-size: 0.65rem;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      font-weight: 600;
      margin-top: 2px;
    }

    /* Cards */
    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 18px;
      margin-bottom: 16px;
    }

    .card h3 {
      font-size: 1.05rem;
      font-weight: 600;
      margin-bottom: 12px;
      color: var(--accent-green);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .grid-2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 12px;
    }

    /* Section Headers */
    .section-header {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border);
    }

    .section-num {
      width: 26px;
      height: 26px;
      background: var(--surface-subtle);
      border: 1px solid var(--accent-green);
      border-radius: 4px;
      display: grid;
      place-items: center;
      font-weight: 700;
      font-size: 0.8rem;
      color: var(--accent-green);
      font-family: var(--font-mono);
    }

    .section-header h2 {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text);
    }

    .section-desc {
      color: var(--text-muted);
      margin-bottom: 16px;
      font-size: 0.88rem;
    }

    /* Tables */
    .table-container {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      margin: 10px 0;
      border: 1px solid var(--border);
      border-radius: 6px;
    }

    .custom-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
    }

    .custom-table th, .custom-table td {
      border: 1px solid var(--border);
      padding: 8px 11px;
      text-align: left;
    }

    .custom-table th {
      background: #050806;
      color: var(--accent-green);
      font-weight: 600;
    }

    .custom-table tr:nth-child(even) {
      background: rgba(255, 255, 255, 0.015);
    }

    /* Code Blocks with Green Accents */
    .code-wrapper {
      position: relative;
      margin: 10px 0;
      border: 1px solid var(--border);
      border-radius: 6px;
      overflow: hidden;
    }

    .code-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #050806;
      border-bottom: 1px solid var(--border);
      padding: 5px 10px;
      font-size: 0.72rem;
      font-family: var(--font-mono);
      color: var(--text-dim);
    }

    .code-header .code-lang {
      color: var(--accent-green);
      font-weight: 600;
    }

    .code-header .btn-copy {
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 0.7rem;
      cursor: pointer;
      font-family: var(--font-mono);
    }

    .code-header .btn-copy:hover {
      color: var(--accent-green);
      border-color: var(--accent-green);
    }

    .code-header .btn-copy.copied {
      color: var(--accent-green);
      border-color: var(--accent-green);
    }

    pre {
      background: var(--code-bg);
      padding: 11px 13px;
      overflow-x: auto;
      font-family: var(--font-mono);
      font-size: 0.84rem;
      line-height: 1.5;
      color: #e6edf3;
      margin: 0;
    }

    code {
      font-family: var(--font-mono);
      font-size: 0.86em;
      background: #141f19;
      color: #7ee787;
      padding: 2px 5px;
      border-radius: 4px;
      border: 1px solid var(--border);
    }

    pre code {
      background: transparent;
      color: inherit;
      padding: 0;
      border: none;
    }

    /* Callouts */
    .callout {
      border: 1px solid var(--border);
      border-left: 3px solid;
      border-radius: 4px;
      padding: 11px 13px;
      margin: 12px 0;
      font-size: 0.88rem;
      background: var(--surface);
    }

    .callout-warning { border-left-color: var(--warning); }
    .callout-danger { border-left-color: var(--danger); }
    .callout-tip { border-left-color: var(--accent-green); }
    .callout-info { border-left-color: var(--accent-green); }

    .callout strong {
      display: block;
      margin-bottom: 4px;
      font-weight: 600;
      font-size: 0.9rem;
      color: var(--text);
    }

    /* Slicing Visualizer */
    .visualizer-container {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 18px;
      margin: 14px 0;
    }

    .preset-btns {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 14px;
    }

    .preset-btn {
      background: var(--bg);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 4px 9px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 0.76rem;
      cursor: pointer;
    }

    .preset-btn:hover {
      border-color: var(--accent-green);
      color: var(--accent-green);
    }

    .slice-inputs {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 14px;
    }

    .input-group {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .input-group label {
      font-size: 0.74rem;
      font-weight: 600;
      color: var(--text-muted);
      font-family: var(--font-mono);
    }

    .input-group input {
      background: var(--bg);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 6px 9px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 0.85rem;
      outline: none;
    }

    .input-group input:focus {
      border-color: var(--accent-green);
    }

    .visual-indices {
      display: flex;
      flex-wrap: nowrap;
      overflow-x: auto;
      gap: 5px;
      padding: 10px 0;
      margin-bottom: 12px;
    }

    .char-box {
      min-width: 40px;
      display: flex;
      flex-direction: column;
      align-items: center;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 5px 3px;
    }

    .char-box.selected {
      background: #14281c;
      border-color: var(--accent-green);
    }

    .char-box .char-val {
      font-size: 1.15rem;
      font-weight: 700;
      font-family: var(--font-mono);
      color: var(--text);
    }

    .char-box .pos-idx {
      font-size: 0.68rem;
      color: var(--accent-green);
      font-family: var(--font-mono);
    }

    .char-box .neg-idx {
      font-size: 0.68rem;
      color: var(--danger);
      font-family: var(--font-mono);
    }

    .slice-result {
      background: var(--code-bg);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 10px 12px;
      font-family: var(--font-mono);
      font-size: 0.92rem;
      color: var(--text);
    }

    /* Stack Demo */
    .stack-demo-container {
      display: flex;
      flex-direction: column;
      gap: 6px;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 12px;
      margin: 12px 0;
    }

    .stack-frame {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 8px 11px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .stack-frame.active {
      border-color: var(--accent-green);
      background: #13241a;
    }

    /* Accordions */
    .accordion {
      border: 1px solid var(--border);
      border-radius: 4px;
      margin-bottom: 8px;
      overflow: hidden;
      background: var(--surface);
    }

    .accordion-header {
      padding: 12px 14px;
      background: var(--surface);
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-weight: 600;
      font-size: 0.9rem;
      user-select: none;
    }

    .accordion-header:hover {
      background: var(--surface-subtle);
    }

    .accordion-icon {
      font-size: 0.8rem;
      color: var(--text-dim);
      transition: transform 0.2s ease;
    }

    .accordion.open .accordion-icon {
      transform: rotate(180deg);
    }

    .accordion-body {
      padding: 14px;
      display: none;
      border-top: 1px solid var(--border);
      background: var(--bg);
    }

    .accordion.open .accordion-body {
      display: block;
    }

    /* Flashcards */
    .flashcards-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
      margin-top: 14px;
    }

    .flashcard {
      min-height: 190px;
      perspective: 1000px;
      cursor: pointer;
    }

    .flashcard-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.35s ease;
      transform-style: preserve-3d;
      border-radius: 4px;
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
      border-radius: 4px;
      padding: 18px;
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
      font-size: 0.95rem;
      margin-bottom: 6px;
      color: var(--accent-green);
    }

    .flashcard-front p {
      font-size: 0.86rem;
      color: var(--text-muted);
    }

    .flashcard-back {
      background: #0f1d15;
      color: var(--text);
      transform: rotateY(180deg);
      border-color: var(--accent-green);
      font-size: 0.84rem;
      line-height: 1.5;
    }

    /* Quiz */
    .quiz-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 18px;
      margin-bottom: 16px;
    }

    .quiz-q {
      font-size: 0.98rem;
      font-weight: 600;
      margin-bottom: 12px;
      color: var(--text);
      line-height: 1.5;
    }

    .quiz-options {
      display: flex;
      flex-direction: column;
      gap: 7px;
    }

    .quiz-opt {
      background: var(--bg);
      border: 1px solid var(--border);
      padding: 9px 12px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 0.88rem;
      display: flex;
      align-items: center;
      gap: 10px;
      min-height: 42px;
    }

    .quiz-opt:hover {
      background: var(--surface-subtle);
      border-color: var(--text-dim);
    }

    .quiz-opt.correct {
      background: #112a1b !important;
      border-color: var(--accent-green) !important;
      color: #7ee787;
      font-weight: 600;
    }

    .quiz-opt.incorrect {
      background: #361418 !important;
      border-color: var(--danger) !important;
      color: #ffa198;
    }

    .quiz-explanation {
      margin-top: 12px;
      padding: 10px 12px;
      background: var(--bg);
      border-left: 3px solid var(--accent-green);
      border-radius: 0 4px 4px 0;
      font-size: 0.86rem;
      color: var(--text-muted);
      display: none;
    }

    .quiz-progress-bar {
      height: 5px;
      background: var(--surface-subtle);
      border-radius: 3px;
      margin-bottom: 16px;
      overflow: hidden;
    }

    .quiz-progress-fill {
      height: 100%;
      background: var(--accent-green);
      width: 0%;
      transition: width 0.2s ease;
    }

    .score-banner {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 14px 18px;
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }

    .btn-retake {
      background: var(--surface-subtle);
      border: 1px solid var(--border);
      color: var(--accent-green);
      padding: 6px 12px;
      border-radius: 4px;
      font-weight: 600;
      font-size: 0.8rem;
      cursor: pointer;
    }

    .btn-retake:hover {
      border-color: var(--accent-green);
    }

    /* Mobile Dock */
    .mobile-dock {
      display: none;
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      height: 54px;
      background: #050806;
      border-top: 1px solid var(--border);
      z-index: 999;
      justify-content: space-around;
      align-items: center;
      padding: 0 6px calc(env(safe-area-inset-bottom, 0px) + 2px);
    }

    .dock-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.65rem;
      font-weight: 600;
      cursor: pointer;
      padding: 4px 6px;
    }

    .dock-item.active, .dock-item:hover {
      color: var(--accent-green);
    }

    .dock-item .dock-icon {
      font-size: 1.05rem;
    }

    @media (max-width: 960px) {
      .mobile-dock { display: flex; }
      main.content { padding-bottom: 80px !important; }
      .mobile-toggle { bottom: 64px !important; }
    }

    .back-to-top {
      position: fixed;
      bottom: 68px;
      left: 14px;
      width: 36px;
      height: 36px;
      border-radius: 4px;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--accent-green);
      display: grid;
      place-items: center;
      font-size: 1rem;
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
      aside.sidebar, .mobile-toggle, .tabs-header-bar, .mobile-dock, .back-to-top, .top-search-bar { display: none !important; }
      main.content { margin: 0 !important; padding: 0 !important; max-width: 100% !important; }
      .tab-pane { display: block !important; }
      body { background: #fff; color: #000; }
      .card, .hero, .quiz-card { border: 1px solid #ccc; background: #fff; color: #000; }
      pre { background: #f6f8fa; color: #000; border: 1px solid #ddd; }
    }
  </style>"""

# Replace style block
pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
text = pattern.sub(green_css, text)

# 2. Update Sidebar links to call switchTab(tabId)
sidebar_clean = """  <!-- Sidebar -->
  <aside class="sidebar" id="sidebar">
    <div class="brand">
      <div class="brand-logo">PSUT</div>
      <div>
        <div class="brand-title">11102 Computing</div>
        <div class="brand-sub">Midterm Portal</div>
      </div>
    </div>

    <div class="nav-group-title">Study Tabs</div>
    <a class="nav-link active" id="nav-cram-sheet" onclick="switchTab('cram-sheet')">📋 Cram Sheet <span class="nav-badge">High Yield</span></a>
    <a class="nav-link" id="nav-functions-directory" onclick="switchTab('functions-directory')">📚 Functions Directory <span class="nav-badge">40+</span></a>
    <a class="nav-link" id="nav-slicing-lab" onclick="switchTab('slicing-lab')">🔬 Slicing Lab <span class="nav-badge">Live</span></a>
    <a class="nav-link" id="nav-call-stack-lab" onclick="switchTab('call-stack-lab')">🧱 Call Stack</a>
    <a class="nav-link" id="nav-traps" onclick="switchTab('traps')">⚠️ 20 Fatal Traps <span class="nav-badge">Traps</span></a>
    <a class="nav-link" id="nav-flashcards" onclick="switchTab('flashcards')">🃏 41 Flashcards</a>
    <a class="nav-link" id="nav-mock-exam" onclick="switchTab('mock-exam')">📝 40-Q Mock Exam <span class="nav-badge">40 Qs</span></a>
    <a class="nav-link" id="nav-lecture-bible" onclick="switchTab('lecture-bible')">📖 Lecture Bible (W1-W6)</a>
  </aside>"""

# Replace sidebar
sidebar_pattern = re.compile(r'<!-- Sidebar -->.*?<!-- Main Content -->', re.DOTALL)
text = sidebar_pattern.sub(sidebar_clean + '\n\n  <!-- Main Content -->', text)

# 3. Add Top Tabs Bar and Minimal Hero inside Main Content
top_tabs_html = """    <!-- Minimal Flat Hero -->
    <div class="hero">
      <div class="hero-title-group">
        <h1>PSUT 11102 · Midterm Prep Portal</h1>
        <p>Complete Weeks 1–6 revision handbook. Tab-based layout for zero distraction.</p>
      </div>
      <div class="hero-stats-group">
        <div class="stat-pill"><div class="stat-num">40</div><div class="stat-label">Exam Qs</div></div>
        <div class="stat-pill"><div class="stat-num">20</div><div class="stat-label">Traps</div></div>
        <div class="stat-pill"><div class="stat-num">41</div><div class="stat-label">Cards</div></div>
        <div class="stat-pill"><div class="stat-num">6</div><div class="stat-label">Weeks</div></div>
      </div>
    </div>

    <!-- STICKY TOP TAB BAR -->
    <nav class="tabs-header-bar" id="topTabsBar">
      <button class="tab-btn active" id="tabbtn-cram-sheet" onclick="switchTab('cram-sheet')">📋 Cram Sheet</button>
      <button class="tab-btn" id="tabbtn-functions-directory" onclick="switchTab('functions-directory')">📚 Functions Directory</button>
      <button class="tab-btn" id="tabbtn-slicing-lab" onclick="switchTab('slicing-lab')">🔬 Slicing Lab</button>
      <button class="tab-btn" id="tabbtn-call-stack-lab" onclick="switchTab('call-stack-lab')">🧱 Call Stack</button>
      <button class="tab-btn" id="tabbtn-traps" onclick="switchTab('traps')">⚠️ 20 Traps</button>
      <button class="tab-btn" id="tabbtn-flashcards" onclick="switchTab('flashcards')">🃏 41 Cards</button>
      <button class="tab-btn" id="tabbtn-mock-exam" onclick="switchTab('mock-exam')">📝 40-Q Exam</button>
      <button class="tab-btn" id="tabbtn-lecture-bible" onclick="switchTab('lecture-bible')">📖 Lecture Bible</button>
    </nav>"""

# Replace hero & quick-filter-pills with top_tabs_html
hero_pattern = re.compile(r'<!-- Hero Banner -->.*?<div class="quick-filter-pills">.*?</div>', re.DOTALL)
text = hero_pattern.sub(top_tabs_html, text)

# 4. Wrap sections into tab panes:
# Section cram-sheet -> <div id="cram-sheet" class="tab-pane active"><section ...> ... </section></div>
text = text.replace('<section id="cram-sheet">', '<div id="cram-sheet" class="tab-pane active">\n    <section>')
text = text.replace('<section id="functions-directory">', '</div>\n    <div id="functions-directory" class="tab-pane">\n    <section>')
text = text.replace('<section id="slicing-lab">', '</div>\n    <div id="slicing-lab" class="tab-pane">\n    <section>')
text = text.replace('<section id="call-stack-lab">', '</div>\n    <div id="call-stack-lab" class="tab-pane">\n    <section>')
text = text.replace('<section id="traps">', '</div>\n    <div id="traps" class="tab-pane">\n    <section>')
text = text.replace('<section id="flashcards">', '</div>\n    <div id="flashcards" class="tab-pane">\n    <section>')
text = text.replace('<section id="mock-exam">', '</div>\n    <div id="mock-exam" class="tab-pane">\n    <section>')

# Group weeks 1 to 6 into lecture-bible tab pane
lecture_bible_open = """</div>
    <!-- Tab Pane: Lecture Bible (Weeks 1 to 6) -->
    <div id="lecture-bible" class="tab-pane">
      <div style="display:flex; flex-wrap:wrap; gap:6px; margin-bottom:16px;">
        <button class="pill-btn active" onclick="filterBibleWeek('all')">All Weeks</button>
        <button class="pill-btn" onclick="filterBibleWeek('week1')">Week 1: Basics & Types</button>
        <button class="pill-btn" onclick="filterBibleWeek('week2')">Week 2: Conditionals</button>
        <button class="pill-btn" onclick="filterBibleWeek('week3')">Week 3: Loops & Scope</button>
        <button class="pill-btn" onclick="filterBibleWeek('week4')">Week 4: Nested Loops</button>
        <button class="pill-btn" onclick="filterBibleWeek('week5')">Week 5: Strings & Slicing</button>
        <button class="pill-btn" onclick="filterBibleWeek('week6')">Week 6: Lists & Practice</button>
      </div>
"""

text = text.replace('<!-- Week 1 -->\n    <section id="week1">', lecture_bible_open + '    <!-- Week 1 -->\n    <section id="week1" class="bible-week">')
text = text.replace('<!-- Week 2 -->\n    <section id="week2">', '    <!-- Week 2 -->\n    <section id="week2" class="bible-week">')
text = text.replace('<!-- Week 3 -->\n    <section id="week3">', '    <!-- Week 3 -->\n    <section id="week3" class="bible-week">')
text = text.replace('<!-- Week 4 -->\n    <section id="week4">', '    <!-- Week 4 -->\n    <section id="week4" class="bible-week">')
text = text.replace('<!-- Week 5 -->\n    <section id="week5">', '    <!-- Week 5 -->\n    <section id="week5" class="bible-week">')
text = text.replace('<!-- Week 6 -->\n    <section id="week6">', '    <!-- Week 6 -->\n    <section id="week6" class="bible-week">')

# Close the last tab pane before mobile dock
dock_pattern = re.compile(r'<!-- Floating Back to Top -->')
text = dock_pattern.sub('</div>\n\n    <!-- Floating Back to Top -->', text, count=1)

# 5. Update Mobile Dock onclick calls
dock_replace = """    <!-- Mobile App Bottom Dock -->
    <nav class="mobile-dock" id="mobileDock">
      <a class="dock-item active" id="dock-cram-sheet" onclick="switchTab('cram-sheet')">
        <span class="dock-icon">📋</span>
        <span>Cram</span>
      </a>
      <a class="dock-item" id="dock-functions-directory" onclick="switchTab('functions-directory')">
        <span class="dock-icon">📚</span>
        <span>Functions</span>
      </a>
      <a class="dock-item" id="dock-slicing-lab" onclick="switchTab('slicing-lab')">
        <span class="dock-icon">🔬</span>
        <span>Slicing</span>
      </a>
      <a class="dock-item" id="dock-traps" onclick="switchTab('traps')">
        <span class="dock-icon">⚠️</span>
        <span>Traps</span>
      </a>
      <a class="dock-item" id="dock-flashcards" onclick="switchTab('flashcards')">
        <span class="dock-icon">🃏</span>
        <span>Cards</span>
      </a>
      <a class="dock-item" id="dock-mock-exam" onclick="switchTab('mock-exam')">
        <span class="dock-icon">📝</span>
        <span>Quiz</span>
      </a>
      <a class="dock-item" id="dock-lecture-bible" onclick="switchTab('lecture-bible')">
        <span class="dock-icon">📖</span>
        <span>Bible</span>
      </a>
    </nav>"""

mobile_dock_pattern = re.compile(r'<!-- Mobile App Bottom Dock -->.*?<\/nav>', re.DOTALL)
text = mobile_dock_pattern.sub(dock_replace, text)

# 6. Add switchTab JavaScript function and initial hash reading
tab_js = """
    // --- TAB SWITCHING SYSTEM (Zero Scroll Hell) ---
    const allTabIds = [
      'cram-sheet',
      'functions-directory',
      'slicing-lab',
      'call-stack-lab',
      'traps',
      'flashcards',
      'mock-exam',
      'lecture-bible'
    ];

    function switchTab(tabId) {
      if (!allTabIds.includes(tabId)) tabId = 'cram-sheet';

      // 1. Show only selected pane
      allTabIds.forEach(id => {
        const pane = document.getElementById(id);
        if (pane) {
          pane.classList.toggle('active', id === tabId);
        }
      });

      // 2. Update Top Tab Bar Buttons
      document.querySelectorAll('.tabs-header-bar .tab-btn').forEach(btn => {
        btn.classList.toggle('active', btn.id === `tabbtn-${tabId}`);
      });

      // 3. Update Sidebar Nav Links
      document.querySelectorAll('aside.sidebar .nav-link').forEach(link => {
        link.classList.toggle('active', link.id === `nav-${tabId}`);
      });

      // 4. Update Mobile Dock Items
      document.querySelectorAll('.mobile-dock .dock-item').forEach(item => {
        item.classList.toggle('active', item.id === `dock-${tabId}`);
      });

      // 5. Scroll to top of content
      window.scrollTo({ top: 0, behavior: 'instant' });

      // 6. Dismiss mobile drawer if open
      if (window.innerWidth <= 960) {
        document.getElementById('sidebar').classList.remove('open');
      }

      // 7. Update URL hash
      if (history.replaceState) {
        history.replaceState(null, null, `#${tabId}`);
      } else {
        location.hash = `#${tabId}`;
      }
    }

    function filterBibleWeek(weekId) {
      document.querySelectorAll('#lecture-bible .pill-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('onclick').includes(weekId));
      });

      const weeks = document.querySelectorAll('.bible-week');
      if (weekId === 'all') {
        weeks.forEach(w => w.style.display = 'block');
      } else {
        weeks.forEach(w => {
          w.style.display = (w.id === weekId) ? 'block' : 'none';
        });
      }
    }

    // Read hash on page load
    window.addEventListener('DOMContentLoaded', () => {
      const hash = window.location.hash.replace('#', '');
      if (hash && allTabIds.includes(hash)) {
        switchTab(hash);
      }
    });
"""

text = text.replace('// --- On Load Initialization ---', tab_js + '\n    // --- On Load Initialization ---')

with open('build_master_hub.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully converted build_master_hub.py to Green Theme & Tabbed Interface!")
