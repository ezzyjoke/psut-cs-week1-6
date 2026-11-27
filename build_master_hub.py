import json
import html

# Load datasets
with open('traps_data.json', 'r', encoding='utf-8') as f:
    traps = json.load(f)

with open('flashcards_data.json', 'r', encoding='utf-8') as f:
    flashcards = json.load(f)

with open('quiz_data.json', 'r', encoding='utf-8') as f:
    quiz = json.load(f)

print(f"Loaded {len(traps)} traps, {len(flashcards)} flashcards, {len(quiz)} quiz questions.")

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="theme-color" content="#070a13">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <title>PSUT 11102 · Introduction to Computing — Complete Midterm Revision Master Hub</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
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
  </style>
</head>
<body>

  <!-- Mobile Toggle Button -->
  <button class="mobile-toggle" onclick="toggleSidebar()">☰</button>

    <!-- Sidebar -->
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
    <a class="nav-link" id="nav-lecture-notes" onclick="switchTab('lecture-notes')">📖 Lecture Notes (W1-W6)</a>
  </aside>

  <!-- Main Content -->
  <main class="content">

    <!-- Global Search -->
    <div class="top-search-bar">
      <span style="color:#38bdf8; font-size:1.1rem;">🔍</span>
      <input type="text" id="globalSearch" placeholder="Search any topic, operator, method, error, or quiz question (e.g. 'slice', '-17 // 5', 'unreachable', 'split')..." oninput="filterGlobalSearch()">
    </div>

        <!-- Minimal Flat Hero -->
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
      <button class="tab-btn" id="tabbtn-lecture-notes" onclick="switchTab('lecture-notes')">📖 Lecture Notes</button>
    </nav>

    <!-- ========================================================================= -->
    <!-- MASTER FUNCTION DIRECTORY -->
    <!-- ========================================================================= -->
    <div id="functions-directory" class="tab-pane">
    <section>
      <div class="section-header">
        <div class="section-num">📚</div>
        <h2>Master Function Directory (All Functions & Methods Used)</h2>
      </div>
      <p class="section-desc">A complete, categorized reference guide of every built-in function, standard library function, string method, list method, and custom exam algorithm function used in Weeks 1 through 6.</p>

      <!-- Category 1: Built-ins -->
      <div class="card">
        <h3 style="color:#38bdf8;">1. Python Standard Built-in Functions</h3>
        <table class="custom-table">
          <tr><th>Function</th><th>Syntax / Signature</th><th>What It Does</th><th>Return Type</th><th>Exam Example & Output</th></tr>
          <tr>
            <td><code>print()</code></td>
            <td><code>print(*args, sep=' ', end='\n')</code></td>
            <td>Outputs values to console. <code>sep</code> controls separator between items; <code>end</code> controls line termination.</td>
            <td><code>None</code></td>
            <td><code>print(1, 2, sep='-', end='!')</code><br>&rarr; <code>1-2!</code></td>
          </tr>
          <tr>
            <td><code>input()</code></td>
            <td><code>input(prompt='')</code></td>
            <td>Pauses execution, displays prompt, waits for user to press Enter. <strong>ALWAYS returns a string!</strong></td>
            <td><code>str</code></td>
            <td><code>age = int(input('Age: '))</code><br>(Must convert to do math!)</td>
          </tr>
          <tr>
            <td><code>int()</code></td>
            <td><code>int(x)</code></td>
            <td>Converts a string or float to an integer. Truncates towards zero (chops decimals).</td>
            <td><code>int</code></td>
            <td><code>int('42') &rarr; 42</code><br><code>int(3.99) &rarr; 3</code></td>
          </tr>
          <tr>
            <td><code>float()</code></td>
            <td><code>float(x)</code></td>
            <td>Converts an integer or string to a floating-point decimal number.</td>
            <td><code>float</code></td>
            <td><code>float('2.5') &rarr; 2.5</code><br><code>float(7) &rarr; 7.0</code></td>
          </tr>
          <tr>
            <td><code>str()</code></td>
            <td><code>str(x)</code></td>
            <td>Converts any Python value to its string representation. Essential for string concatenation.</td>
            <td><code>str</code></td>
            <td><code>'Score: ' + str(95) &rarr; 'Score: 95'</code></td>
          </tr>
          <tr>
            <td><code>bool()</code></td>
            <td><code>bool(x)</code></td>
            <td>Evaluates the truthiness of <code>x</code>. <code>0</code>, <code>0.0</code>, <code>''</code>, <code>[]</code>, <code>None</code> are <code>False</code>; all else is <code>True</code>.</td>
            <td><code>bool</code></td>
            <td><code>bool(0) &rarr; False</code><br><code>bool('hi') &rarr; True</code></td>
          </tr>
          <tr>
            <td><code>type()</code></td>
            <td><code>type(x)</code></td>
            <td>Returns the class / type of the object.</td>
            <td><code>type</code></td>
            <td><code>type(10 / 2) &rarr; &lt;class 'float'&gt;</code><br><code>type(True) &rarr; &lt;class 'bool'&gt;</code></td>
          </tr>
          <tr>
            <td><code>len()</code></td>
            <td><code>len(sequence)</code></td>
            <td>Returns number of items in a string, list, or collection. Last valid index is <code>len - 1</code>.</td>
            <td><code>int</code></td>
            <td><code>len('PYTHON') &rarr; 6</code><br><code>len([10, 20]) &rarr; 2</code></td>
          </tr>
          <tr>
            <td><code>sum()</code></td>
            <td><code>sum(iterable)</code></td>
            <td>Calculates the total of all numbers in an iterable.</td>
            <td><code>int</code> / <code>float</code></td>
            <td><code>sum([10, 20, 30]) &rarr; 60</code></td>
          </tr>
          <tr>
            <td><code>max()</code></td>
            <td><code>max(a, b, ...)</code> or <code>max(list)</code></td>
            <td>Returns the largest item. When initializing manual max, never use 0 if inputs could be negative.</td>
            <td>Same as items</td>
            <td><code>max(4, 9, 2) &rarr; 9</code><br><code>max([-5, -1]) &rarr; -1</code></td>
          </tr>
          <tr>
            <td><code>min()</code></td>
            <td><code>min(a, b, ...)</code> or <code>min(list)</code></td>
            <td>Returns the smallest item. Crucial for unequal list merges: <code>min(len(a), len(b))</code>.</td>
            <td>Same as items</td>
            <td><code>min(4, 9, 2) &rarr; 2</code></td>
          </tr>
          <tr>
            <td><code>abs()</code></td>
            <td><code>abs(x)</code></td>
            <td>Returns the absolute (non-negative) magnitude of a number.</td>
            <td><code>int</code> / <code>float</code></td>
            <td><code>abs(-12) &rarr; 12</code><br><code>abs(3.5) &rarr; 3.5</code></td>
          </tr>
          <tr>
            <td><code>round()</code></td>
            <td><code>round(number, ndigits=0)</code></td>
            <td>Rounds a float to a specified number of decimal digits.</td>
            <td><code>int</code> / <code>float</code></td>
            <td><code>round(3.14159, 2) &rarr; 3.14</code></td>
          </tr>
          <tr>
            <td><code>range()</code></td>
            <td><code>range(stop)</code><br><code>range(start, stop[, step])</code></td>
            <td>Generates an immutable sequence of numbers from start up to, but NOT including, stop.</td>
            <td><code>range</code></td>
            <td><code>range(5) &rarr; 0,1,2,3,4</code><br><code>range(5,0,-1) &rarr; 5,4,3,2,1</code></td>
          </tr>
          <tr>
            <td><code>sorted()</code></td>
            <td><code>sorted(iterable)</code></td>
            <td>Returns a <strong>brand new sorted list</strong>, leaving the original sequence unchanged.</td>
            <td><code>list</code></td>
            <td><code>a = [3, 1]; b = sorted(a)</code><br>&rarr; <code>b=[1, 3], a=[3, 1]</code></td>
          </tr>
          <tr>
            <td><code>list()</code></td>
            <td><code>list(iterable)</code></td>
            <td>Constructs a mutable list from an iterable (like a range or string).</td>
            <td><code>list</code></td>
            <td><code>list(range(3)) &rarr; [0, 1, 2]</code><br><code>list('ABC') &rarr; ['A', 'B', 'C']</code></td>
          </tr>
          <tr>
            <td><code>set()</code></td>
            <td><code>set(iterable)</code></td>
            <td>Constructs a collection of unique elements. Used in slides to test if all elements are unique.</td>
            <td><code>set</code></td>
            <td><code>len(set(nums)) == len(nums)</code><br>(Returns <code>True</code> if all unique)</td>
          </tr>
        </table>
      </div>

      <!-- Category 2: Modules math and random -->
      <div class="card">
        <h3 style="color:#10b981;">2. Standard Library Modules (<code>math</code> & <code>random</code>)</h3>
        <table class="custom-table">
          <tr><th>Module Function / Const</th><th>Syntax</th><th>What It Does</th><th>Return Type</th><th>Exam Example & Output</th></tr>
          <tr>
            <td><code>math.sqrt()</code></td>
            <td><code>math.sqrt(x)</code></td>
            <td>Computes the square root &radic;x. <code>x</code> must be &ge; 0. Always returns a float.</td>
            <td><code>float</code></td>
            <td><code>math.sqrt(49) &rarr; 7.0</code></td>
          </tr>
          <tr>
            <td><code>math.pi</code></td>
            <td><code>math.pi</code></td>
            <td>Mathematical constant &pi; &approx; 3.141592653589793.</td>
            <td><code>float</code></td>
            <td><code>area = math.pi * r ** 2</code></td>
          </tr>
          <tr>
            <td><code>math.floor()</code></td>
            <td><code>math.floor(x)</code></td>
            <td>Rounds down to the nearest integer (same as <code>//</code> logic).</td>
            <td><code>int</code></td>
            <td><code>math.floor(3.8) &rarr; 3</code></td>
          </tr>
          <tr>
            <td><code>math.ceil()</code></td>
            <td><code>math.ceil(x)</code></td>
            <td>Rounds up to the nearest integer.</td>
            <td><code>int</code></td>
            <td><code>math.ceil(3.2) &rarr; 4</code></td>
          </tr>
          <tr>
            <td><code>random.randint()</code></td>
            <td><code>random.randint(a, b)</code></td>
            <td>Returns a random integer N such that a &le; N &le; b. <strong>INCLUSIVE of both endpoints!</strong></td>
            <td><code>int</code></td>
            <td><code>random.randint(1, 6)</code><br>&rarr; Can return 1, 2, 3, 4, 5, or 6</td>
          </tr>
        </table>
      </div>

      <!-- Category 3: String Methods -->
      <div class="card">
        <h3 style="color:#a855f7;">3. String Methods (Strings are IMMUTABLE &mdash; all return NEW strings)</h3>
        <table class="custom-table">
          <tr><th>String Method</th><th>Syntax</th><th>What It Does</th><th>Return Type</th><th>Exam Example & Output</th></tr>
          <tr>
            <td><code>.upper()</code></td>
            <td><code>s.upper()</code></td>
            <td>Returns a copy of <code>s</code> converted to uppercase. Original <code>s</code> is unchanged!</td>
            <td><code>str</code></td>
            <td><code>'hello'.upper() &rarr; 'HELLO'</code></td>
          </tr>
          <tr>
            <td><code>.lower()</code></td>
            <td><code>s.lower()</code></td>
            <td>Returns a copy of <code>s</code> converted to lowercase. Ideal for case-insensitive checks.</td>
            <td><code>str</code></td>
            <td><code>'PSUT'.lower() &rarr; 'psut'</code></td>
          </tr>
          <tr>
            <td><code>.strip()</code></td>
            <td><code>s.strip()</code></td>
            <td>Returns a copy with whitespace (spaces, tabs, newlines) removed from BOTH ends.</td>
            <td><code>str</code></td>
            <td><code>'  hi  '.strip() &rarr; 'hi'</code></td>
          </tr>
          <tr>
            <td><code>.find()</code></td>
            <td><code>s.find(sub[, start])</code></td>
            <td>Returns index of <strong>first</strong> occurrence of <code>sub</code>. Returns <strong>-1</strong> if not found. Does not crash!</td>
            <td><code>int</code></td>
            <td><code>'banana'.find('na') &rarr; 2</code><br><code>'banana'.find('xyz') &rarr; -1</code></td>
          </tr>
          <tr>
            <td><code>.count()</code></td>
            <td><code>s.count(sub)</code></td>
            <td>Returns number of non-overlapping occurrences of substring <code>sub</code>.</td>
            <td><code>int</code></td>
            <td><code>'banana'.count('a') &rarr; 3</code></td>
          </tr>
          <tr>
            <td><code>.replace()</code></td>
            <td><code>s.replace(old, new)</code></td>
            <td>Returns copy with all occurrences of <code>old</code> replaced by <code>new</code>.</td>
            <td><code>str</code></td>
            <td><code>'banana'.replace('a', 'o') &rarr; 'bonono'</code></td>
          </tr>
          <tr>
            <td><code>.split()</code></td>
            <td><code>s.split(sep=None)</code></td>
            <td>Splits string into a list of words. If <code>sep</code> is omitted, splits by ANY whitespace.</td>
            <td><code>list</code></td>
            <td><code>'a b c'.split() &rarr; ['a', 'b', 'c']</code><br><code>'1,2,3'.split(',') &rarr; ['1','2','3']</code></td>
          </tr>
          <tr>
            <td><code>.join()</code></td>
            <td><code>sep.join(list_of_str)</code></td>
            <td>Concatenates a list of strings into one string, inserting <code>sep</code> between each element.</td>
            <td><code>str</code></td>
            <td><code>'-'.join(['a', 'b']) &rarr; 'a-b'</code></td>
          </tr>
          <tr>
            <td><code>.startswith()</code></td>
            <td><code>s.startswith(prefix)</code></td>
            <td>Returns <code>True</code> if the string begins with <code>prefix</code>.</td>
            <td><code>bool</code></td>
            <td><code>'hello'.startswith('he') &rarr; True</code></td>
          </tr>
          <tr>
            <td><code>.endswith()</code></td>
            <td><code>s.endswith(suffix)</code></td>
            <td>Returns <code>True</code> if the string ends with <code>suffix</code> (e.g. <code>.jo</code>).</td>
            <td><code>bool</code></td>
            <td><code>'psut.edu.jo'.endswith('.jo') &rarr; True</code></td>
          </tr>
          <tr>
            <td><code>.isalpha()</code></td>
            <td><code>s.isalpha()</code></td>
            <td>Returns <code>True</code> if all characters are alphabetic letters and length &gt; 0.</td>
            <td><code>bool</code></td>
            <td><code>'Abc'.isalpha() &rarr; True</code><br><code>'A 1'.isalpha() &rarr; False</code></td>
          </tr>
          <tr>
            <td><code>.isdigit()</code></td>
            <td><code>s.isdigit()</code></td>
            <td>Returns <code>True</code> if all characters are numeric digits and length &gt; 0.</td>
            <td><code>bool</code></td>
            <td><code>'123'.isdigit() &rarr; True</code><br><code>'12.3'.isdigit() &rarr; False</code></td>
          </tr>
          <tr>
            <td><code>.rjust()</code></td>
            <td><code>s.rjust(width)</code></td>
            <td>Right-aligns string in a field of given width, padding with spaces (used in multiplication grid).</td>
            <td><code>str</code></td>
            <td><code>'4'.rjust(3) &rarr; '  4'</code></td>
          </tr>
        </table>
      </div>

      <!-- Category 4: List Methods -->
      <div class="card">
        <h3 style="color:#f59e0b;">4. List Methods (Lists are MUTABLE &mdash; in-place methods return <code>None</code>)</h3>
        <table class="custom-table">
          <tr><th>List Method</th><th>Syntax</th><th>What It Does</th><th>Mutates List?</th><th>Return Value</th><th>Exam Pitfall / Example</th></tr>
          <tr>
            <td><code>.append()</code></td>
            <td><code>a.append(x)</code></td>
            <td>Adds item <code>x</code> to the very end of list <code>a</code>.</td>
            <td><strong>Yes</strong></td>
            <td><code>None</code></td>
            <td><code>a = [1]; a.append(2) &rarr; [1, 2]</code></td>
          </tr>
          <tr>
            <td><code>.insert()</code></td>
            <td><code>a.insert(i, x)</code></td>
            <td>Inserts item <code>x</code> at index <code>i</code>, shifting elements to the right.</td>
            <td><strong>Yes</strong></td>
            <td><code>None</code></td>
            <td><code>a = [1, 2]; a.insert(0, 9) &rarr; [9, 1, 2]</code></td>
          </tr>
          <tr>
            <td><code>.remove()</code></td>
            <td><code>a.remove(x)</code></td>
            <td>Removes the <strong>first</strong> occurrence of value <code>x</code>. Raises <code>ValueError</code> if <code>x</code> not in list!</td>
            <td><strong>Yes</strong></td>
            <td><code>None</code></td>
            <td><strong>DANGER:</strong> Looping with <code>a.remove(x)</code> skips subsequent elements!</td>
          </tr>
          <tr>
            <td><code>.pop()</code></td>
            <td><code>a.pop(i=-1)</code></td>
            <td>Removes and <strong>returns</strong> the item at index <code>i</code> (default is last item).</td>
            <td><strong>Yes</strong></td>
            <td><strong>Removed item</strong></td>
            <td><code>a = [10, 20]; x = a.pop() &rarr; x = 20, a = [10]</code></td>
          </tr>
          <tr>
            <td><code>.sort()</code></td>
            <td><code>a.sort()</code></td>
            <td>Sorts list <strong>in-place</strong> in ascending order.</td>
            <td><strong>Yes</strong></td>
            <td><strong><code>None</code></strong></td>
            <td><strong>FATAL TRAP:</strong> <code>a = a.sort()</code> destroys list by setting <code>a = None</code>!</td>
          </tr>
          <tr>
            <td><code>.reverse()</code></td>
            <td><code>a.reverse()</code></td>
            <td>Reverses elements of list <strong>in-place</strong>.</td>
            <td><strong>Yes</strong></td>
            <td><code>None</code></td>
            <td><code>a = [1, 2]; a.reverse() &rarr; a = [2, 1]</code> (Alters caller's list!)</td>
          </tr>
        </table>
      </div>

      <!-- Category 5: Course Custom Functions & Algorithms -->
      <div class="card">
        <h3 style="color:#f43f5e;">5. Course Algorithm Functions & Practice Problems (Weeks 1 to 6)</h3>
        <table class="custom-table">
          <tr><th>Function Name</th><th>Parameters</th><th>Core Logic & Exam Purpose</th><th>Return Value</th></tr>
          <tr>
            <td><code>distance(x1, y1, x2, y2)</code></td>
            <td><code>(x1, y1, x2, y2)</code></td>
            <td>Computes Euclidean distance between points: <code>math.sqrt((x1-x2)**2 + (y1-y2)**2)</code>.</td>
            <td><code>float</code></td>
          </tr>
          <tr>
            <td><code>circle_area(cx, cy, px, py)</code></td>
            <td><code>(cx, cy, px, py)</code></td>
            <td>Composes <code>distance</code> to compute radius $r$, then returns &pi; r<sup>2</sup>. Demonstrates function composition.</td>
            <td><code>float</code></td>
          </tr>
          <tr>
            <td><code>is_leap_year(year)</code></td>
            <td><code>year</code></td>
            <td>Checks leap year rule: Divisible by 400, or (divisible by 4 and NOT 100).</td>
            <td><code>bool</code> (True/False)</td>
          </tr>
          <tr>
            <td><code>days_in_february(year)</code></td>
            <td><code>year</code></td>
            <td>Reuses <code>is_leap_year(year)</code>: returns 29 if True, else 28.</td>
            <td><code>int</code></td>
          </tr>
          <tr>
            <td><code>is_prime(n)</code></td>
            <td><code>n</code></td>
            <td>Flag loop testing divisors from 2 up to $n-1$. Early <code>return False</code> on first divisor; <code>return True</code> outside loop.</td>
            <td><code>bool</code></td>
          </tr>
          <tr>
            <td><code>print_table(n)</code></td>
            <td><code>n</code></td>
            <td>Loops <code>k</code> from 1 to 12 printing <code>n x k = n*k</code>. Helper function for nested multiplication table.</td>
            <td><code>None</code></td>
          </tr>
          <tr>
            <td><code>integer_square_root(n)</code></td>
            <td><code>n</code></td>
            <td>Slide mystery: Loops <code>i</code> from 0 to $n$. If <code>i*i == n</code> returns <code>i</code>, else returns <code>-1</code>.</td>
            <td><code>int</code></td>
          </tr>
          <tr>
            <td><code>second_largest(count)</code></td>
            <td><code>count</code></td>
            <td>Slide mystery: Maintains <code>largest</code> and <code>second</code> variables across <code>count</code> user inputs.</td>
            <td><code>int</code></td>
          </tr>
          <tr>
            <td><code>last_even()</code></td>
            <td>None</td>
            <td>Slide mystery: Loops until 0, overwrites <code>result = num</code> whenever <code>num % 2 == 0</code>. Returns last even number entered.</td>
            <td><code>int</code> or <code>None</code></td>
          </tr>
          <tr>
            <td><code>is_palindrome(s)</code></td>
            <td><code>s</code></td>
            <td>Two pointers <code>i = 0, j = len(s) - 1</code> advancing inward checking <code>s[i] != s[j]</code>. (Or <code>s == s[::-1]</code>).</td>
            <td><code>bool</code></td>
          </tr>
          <tr>
            <td><code>is_equivalent(a, b)</code></td>
            <td><code>(a, b)</code></td>
            <td>Slide Week 6: Two-way membership test: every element of <code>a</code> in <code>b</code> AND every element of <code>b</code> in <code>a</code>. Ignores order/frequency.</td>
            <td><code>bool</code></td>
          </tr>
          <tr>
            <td><code>is_sublist(a, b)</code></td>
            <td><code>(a, b)</code></td>
            <td>Slide Week 6 mystery: Sliding window of size $n = len(a)$ over $b$: <code>if b[i:i+n] == a: return True</code>.</td>
            <td><code>bool</code></td>
          </tr>
          <tr>
            <td><code>is_sorted(nums)</code></td>
            <td><code>nums</code></td>
            <td>Neighbor comparison loop <code>range(len(nums) - 1)</code>: if <code>nums[i] > nums[i+1]</code> returns <code>False</code>.</td>
            <td><code>bool</code></td>
          </tr>
          <tr>
            <td><code>reverse_in_place(a)</code></td>
            <td><code>a</code></td>
            <td>Two pointers swapping <code>a[i], a[j] = a[j], a[i]</code> or <code>a[:] = a[::-1]</code>. Modifies original list.</td>
            <td><code>None</code></td>
          </tr>
          <tr>
            <td><code>find_index(nums, target)</code></td>
            <td><code>(nums, target)</code></td>
            <td>Linear search: returns <code>i</code> immediately when <code>nums[i] == target</code>. Returns <code>-1</code> after loop finishes.</td>
            <td><code>int</code></td>
          </tr>
          <tr>
            <td><code>merge_lists(a, b)</code></td>
            <td><code>(a, b)</code></td>
            <td>Alternates elements up to <code>min(len(a), len(b))</code>, then appends slice leftovers <code>a[n:] + b[n:]</code>.</td>
            <td><code>list</code></td>
          </tr>
          <tr>
            <td><code>remove_duplicates(a)</code></td>
            <td><code>a</code></td>
            <td>Accumulator list: loops <code>for x in a:</code> and appends <code>x</code> only if <code>x not in result</code>. Preserves order.</td>
            <td><code>list</code></td>
          </tr>
          <tr>
            <td><code>count_greater(a, x)</code></td>
            <td><code>(a, x)</code></td>
            <td>Counts how many elements in list <code>a</code> are strictly greater than threshold <code>x</code>.</td>
            <td><code>int</code></td>
          </tr>
          <tr>
            <td><code>rotate_left(a)</code></td>
            <td><code>a</code></td>
            <td>Returns new list with first element moved to the back: <code>a[1:] + a[:1]</code>.</td>
            <td><code>list</code></td>
          </tr>
        </table>
      </div>
    </section>
    </div>

    <!-- ========================================================================= -->
    <!-- 1-HOUR EMERGENCY CRAM SHEET -->
    <!-- ========================================================================= -->
    <div id="cram-sheet" class="tab-pane active">
    <section>
      <div class="section-header">
        <div class="section-num">📋</div>
        <h2>The 1-Hour Pre-Exam Emergency Cram Sheet</h2>
      </div>
      <p class="section-desc">The absolute highest-yield rules and formulas condensed for rapid review before entering the exam room.</p>

      <div class="grid-2">
        <!-- Card 1: Math & Precedence -->
        <div class="card">
          <h3 style="color:#38bdf8;">⚡ Math & Operator Precedence</h3>
          <table class="custom-table">
            <tr><th>Rule / Operator</th><th>Exam Example</th><th>Exact Output</th></tr>
            <tr><td><code>/</code> (True division)</td><td><code>10 / 2</code></td><td><code>5.0</code> (float, never int!)</td></tr>
            <tr><td><code>//</code> (Positive)</td><td><code>17 // 5</code></td><td><code>3</code> (3.4 floored)</td></tr>
            <tr><td><code>//</code> (Negative)</td><td><code>-17 // 5</code></td><td><code>-4</code> (floors towards &minus;&infin;)</td></tr>
            <tr><td><code>%</code> (Negative)</td><td><code>-17 % 5</code></td><td><code>3</code> (since -17 = (-4 &times; 5) + 3)</td></tr>
            <tr><td><code>**</code> (Associativity)</td><td><code>2 ** 3 ** 2</code></td><td><code>512</code> (2<sup>(3<sup>2</sup>)</sup> = 2<sup>9</sup>)</td></tr>
            <tr><td>PEMDAS Order</td><td><code>2 + 3 * 4 ** 2</code></td><td><code>50</code> (4&sup2; = 16 &rarr; 3 &times; 16 = 48 &rarr; 48 + 2 = 50)</td></tr>
          </table>
        </div>

        <!-- Card 2: Slicing Rules -->
        <div class="card">
          <h3 style="color:#10b981;">⚡ Slicing Matrix <code>s[start:stop:step]</code></h3>
          <table class="custom-table">
            <tr><th>Slice</th><th>String: <code>'PYTHON'</code></th><th>Key Rule</th></tr>
            <tr><td><code>s[::]</code></td><td><code>'PYTHON'</code></td><td>Default copy</td></tr>
            <tr><td><code>s[::-1]</code></td><td><code>'NOHTYP'</code></td><td>Full reverse</td></tr>
            <tr><td><code>s[4:1:-1]</code></td><td><code>'OHT'</code></td><td>Indices 4, 3, 2 (1 excluded)</td></tr>
            <tr><td><code>s[0:6:-1]</code></td><td><code>''</code> (Empty)</td><td>Step direction mismatch!</td></tr>
            <tr><td><code>s[-5:-1:1]</code></td><td><code>'YTHO'</code></td><td>Negative to positive bounds</td></tr>
            <tr><td><code>s[0:100]</code></td><td><code>'PYTHON'</code></td><td>Slices NEVER crash with IndexError!</td></tr>
          </table>
        </div>

        <!-- Card 3: Functions & Memory -->
        <div class="card">
          <h3 style="color:#a855f7;">⚡ Functions, Scope & Call Stack</h3>
          <table class="custom-table">
            <tr><th>Topic</th><th>Critical Exam Rule</th></tr>
            <tr><td><code>print()</code> vs <code>return</code></td><td>Function without <code>return</code> produces <code>None</code>! Trying to use result in math crashes with <code>TypeError</code>.</td></tr>
            <tr><td>Call Frames</td><td>Created when function is called, destroyed when it returns. Local variables disappear!</td></tr>
            <tr><td>Variable Shadowing</td><td>A local variable with the same name as a global hides the global without changing it.</td></tr>
            <tr><td>In-place List Reversal</td><td><code>a[:] = a[::-1]</code> or <code>a.reverse()</code> modifies caller's list. <code>a = a[::-1]</code> rebinds locally!</td></tr>
          </table>
        </div>

        <!-- Card 4: Built-in Methods & Traps -->
        <div class="card">
          <h3 style="color:#f59e0b;">⚡ Methods & Common Traps</h3>
          <table class="custom-table">
            <tr><th>Method / Syntax</th><th>Behavior / Pitfall</th></tr>
            <tr><td><code>a = a.sort()</code></td><td><strong>FATAL TRAP!</strong> Sets <code>a = None</code> because <code>.sort()</code> returns None. Use <code>a.sort()</code> alone or <code>sorted(a)</code>.</td></tr>
            <tr><td><code>random.randint(1, 6)</code></td><td><strong>INCLUSIVE</strong> of both 1 and 6!</td></tr>
            <tr><td><code>s.find('xyz')</code></td><td>Returns <code>-1</code> if not found (does NOT crash).</td></tr>
            <tr><td><code>range(len(a) - 1)</code></td><td>Required when comparing <code>a[i]</code> and <code>a[i+1]</code> to avoid <code>IndexError</code>.</td></tr>
            <tr><td>Looping with <code>remove()</code></td><td><code>for x in a: a.remove(x)</code> skips elements due to index shifting!</td></tr>
          </table>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- INTERACTIVE SLICING LAB V2 -->
    <!-- ========================================================================= -->
    </div>
    <div id="slicing-lab" class="tab-pane">
    <section>
      <div class="section-header">
        <div class="section-num">🔬</div>
        <h2>Interactive Slicing Lab v2 (CPython-Exact)</h2>
      </div>
      <p class="section-desc">Click any slide preset or enter custom bounds to inspect character selection, directional movement, and index positions.</p>

      <div class="visualizer-container">
        <div style="font-size:0.85rem; font-weight:700; color:#94a3b8; margin-bottom:8px;">SLIDE PRESETS (Click to test instantly):</div>
        <div class="preset-btns">
          <button class="preset-btn" onclick="applyPreset('PYTHON', '', '', '')">s[::] (Identity)</button>
          <button class="preset-btn" onclick="applyPreset('PYTHON', '', '', '-1')">s[::-1] (Reverse)</button>
          <button class="preset-btn" onclick="applyPreset('PYTHON', '4', '1', '-1')">s[4:1:-1] ('OHT')</button>
          <button class="preset-btn" onclick="applyPreset('PYTHON', '0', '6', '-1')">s[0:6:-1] (Mismatch '')</button>
          <button class="preset-btn" onclick="applyPreset('PYTHON', '-5', '-1', '1')">s[-5:-1:1] ('YTHO')</button>
          <button class="preset-btn" onclick="applyPreset('PYTHON', '', '', '2')">s[::2] ('PTO')</button>
          <button class="preset-btn" onclick="applyPreset('PYTHON', '0', '30', '1')">s[0:30] (Clamped)</button>
          <button class="preset-btn" onclick="applyPreset('PYTHON', '5', '-1', '-1')">s[5:-1:-1] (Stop -1 Trap '')</button>
          <button class="preset-btn" onclick="applyPreset('PYTHON', '10', '-10', '-2')">s[10:-10:-2] ('NHY')</button>
        </div>

        <div class="slice-inputs">
          <div class="input-group" style="flex: 2; min-width: 220px;">
            <label>Sequence String</label>
            <input type="text" id="sliceText" value="PYTHON" oninput="updateVisualizer()">
          </div>
          <div class="input-group" style="flex: 1; min-width: 80px;">
            <label>Start</label>
            <input type="text" id="sliceStart" value="1" placeholder="e.g. 1" oninput="updateVisualizer()">
          </div>
          <div class="input-group" style="flex: 1; min-width: 80px;">
            <label>Stop (Excluded)</label>
            <input type="text" id="sliceStop" value="5" placeholder="e.g. 5" oninput="updateVisualizer()">
          </div>
          <div class="input-group" style="flex: 1; min-width: 80px;">
            <label>Step</label>
            <input type="text" id="sliceStep" value="1" placeholder="e.g. 1" oninput="updateVisualizer()">
          </div>
        </div>

        <div style="font-size: 0.8rem; color: #94a3b8; margin-bottom: 8px;">
          Visual Map: <span style="color:#10b981; font-weight:700;">Green = Positive Index</span> | <span style="color:#f43f5e; font-weight:700;">Pink = Negative Index</span> | <span style="color:#38bdf8; font-weight:700;">Glowing Cyan = Selected Character</span>
        </div>

        <div class="visual-indices" id="visualBoxes"></div>

        <div class="slice-result" id="sliceOutput">
          Output: <span id="sliceVal" style="color: #f8fafc; font-weight: 700;">'YTHO'</span> &nbsp; | &nbsp; Length: <span id="sliceLen">4</span>
        </div>
        <div id="sliceExplanation" style="margin-top: 10px; font-size: 0.88rem; color: #94a3b8;"></div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- INTERACTIVE CALL STACK VISUALIZER -->
    <!-- ========================================================================= -->
    </div>
    <div id="call-stack-lab" class="tab-pane">
    <section>
      <div class="section-header">
        <div class="section-num">🧱</div>
        <h2>Function Execution Stack & Call Frames Visualizer</h2>
      </div>
      <p class="section-desc">Understand how Python creates activation records (call frames) on the stack, isolates local variables, and destroys frames on return.</p>

      <div class="card">
        <h3>Trace Case Study: <code>circle_area(0, 0, 3, 4)</code></h3>
        <p style="color:#94a3b8; margin-bottom:14px;">Click the buttons below to step through Python's call stack like a debugger.</p>

        <div style="display:flex; gap:10px; margin-bottom:16px;">
          <button class="pill-btn active" id="btnStepPrev" onclick="stepStack(-1)">◀ Previous Step</button>
          <button class="pill-btn active" id="btnStepNext" onclick="stepStack(1)">Next Step ▶</button>
          <button class="pill-btn" onclick="resetStack()">Reset</button>
        </div>

        <div class="grid-2">
          <div>
            <pre><code id="stackCode">def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def circle_area(cx, cy, px, py):
    r = distance(cx, cy, px, py)
    return math.pi * r ** 2

def main():
    a1 = circle_area(0, 0, 3, 4)
    print("Area:", round(a1, 2))

main()</code></pre>
          </div>
          <div>
            <div style="font-size:0.85rem; font-weight:700; color:#38bdf8; margin-bottom:8px;">CALL STACK STATE:</div>
            <div class="stack-demo-container" id="stackFramesContainer">
              <!-- Frames rendered by JS -->
            </div>
            <div id="stackStepExplanation" style="font-size:0.9rem; color:#cbd5e1; padding:10px 14px; background:#0e1626; border-radius:8px; border:1px solid #1e293b;">
              Execution starts in the Global Scope.
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 20 FATAL EXAM TRAPS -->
    <!-- ========================================================================= -->
    </div>
    <div id="traps" class="tab-pane">
    <section>
      <div class="section-header">
        <div class="section-num">⚠️</div>
        <h2>The 20 Fatal Exam Traps (Spot the Bug)</h2>
      </div>
      <p class="section-desc">Comprehensive list of the exact traps, edge cases, and output prediction pitfalls tested on the midterm.</p>

      <div id="trapsContainer">
        <!-- Rendered by JS or injected below -->
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- COMPREHENSIVE LECTURE NOTES (WEEKS 1 TO 6) -->
    <!-- ========================================================================= -->

    </div>
    <!-- Tab Pane: Lecture Notes (Weeks 1 to 6) -->
    <div id="lecture-notes" class="tab-pane">
      <div style="display:flex; flex-wrap:wrap; gap:6px; margin-bottom:16px;">
        <button class="pill-btn active" onclick="filterNotesWeek('all')">All Weeks</button>
        <button class="pill-btn" onclick="filterNotesWeek('week1')">Week 1: Basics & Types</button>
        <button class="pill-btn" onclick="filterNotesWeek('week2')">Week 2: Conditionals</button>
        <button class="pill-btn" onclick="filterNotesWeek('week3')">Week 3: Loops & Scope</button>
        <button class="pill-btn" onclick="filterNotesWeek('week4')">Week 4: Nested Loops</button>
        <button class="pill-btn" onclick="filterNotesWeek('week5')">Week 5: Strings & Slicing</button>
        <button class="pill-btn" onclick="filterNotesWeek('week6')">Week 6: Lists & Practice</button>
      </div>
    <!-- Week 1 -->
    <section id="week1" class="bible-week">
      <div class="section-header">
        <div class="section-num">1</div>
        <h2>Week 1: Introduction to Computing, Variables & Expressions</h2>
      </div>

      <div class="card">
        <h3>1. Language Hierarchy & How Python Runs</h3>
        <p>Computers understand only binary machine code (0s and 1s). High-level languages provide human-readable abstractions.</p>
        <table class="custom-table">
          <tr><th>Tier</th><th>Language Type</th><th>Characteristics</th><th>Example</th></tr>
          <tr><td>1</td><td>Natural Language</td><td>English, Arabic. Ambiguous, high redundancy, cannot be executed directly.</td><td>"Add two numbers"</td></tr>
          <tr><td>2</td><td>High-Level Language</td><td>Portable, structured, abstracts hardware registers and memory addresses.</td><td>Python, Java, C++</td></tr>
          <tr><td>3</td><td>Low-Level (Assembly)</td><td>Architecture-specific, direct mapping to CPU instructions.</td><td><code>MOV AL, 61h</code></td></tr>
          <tr><td>4</td><td>Machine Code</td><td>Binary sequences (0s and 1s) directly executed by the ALU/CPU.</td><td><code>10110000 01100001</code></td></tr>
        </table>

        <div class="callout callout-info">
          <strong>How Python Runs (The Hybrid Architecture):</strong><br>
          Unlike pure compilers (C/C++) which generate machine binaries ahead of time, or pure interpreters that parse raw text line by line, Python uses a two-phase hybrid model:
          <ol style="margin-left:20px; margin-top:6px;">
            <li><strong>Compilation Phase:</strong> Python compiles source code (<code>.py</code>) into portable, optimized <strong>Bytecode</strong> (<code>.pyc</code> stored in <code>__pycache__</code>).</li>
            <li><strong>Interpretation Phase:</strong> The <strong>Python Virtual Machine (PVM)</strong> interprets and executes the bytecode instructions on the host machine.</li>
          </ol>
        </div>
      </div>

      <div class="card">
        <h3>2. The Three Categories of Programming Errors</h3>
        <table class="custom-table">
          <tr><th>Error Category</th><th>Definition & Impact</th><th>Slide Example</th><th>Who Catches It?</th></tr>
          <tr>
            <td><strong>Syntax Error</strong></td>
            <td>Violates grammar rules of the language. Python refuses to start executing the program at all.</td>
            <td><code>1 + 2 *</code><br><code>if x = 5:</code></td>
            <td>Python compiler before running</td>
          </tr>
          <tr>
            <td><strong>Semantic / Runtime Error</strong></td>
            <td>Grammar is valid, but the requested operation is mathematically or logically illegal at runtime (program crashes).</td>
            <td><code>10 / 0</code> (ZeroDivisionError)<br><code>"Age: " + 20</code> (TypeError)</td>
            <td>Python interpreter while running</td>
          </tr>
          <tr>
            <td><strong>Logic Error</strong></td>
            <td>Code runs to completion without crashing, but yields an incorrect answer due to flawed algorithm design.</td>
            <td><code>avg = a + b / 2</code> (Missing parentheses divides only b by 2!)</td>
            <td><strong>Only the programmer</strong> through testing!</td>
          </tr>
        </table>
      </div>

      <div class="card">
        <h3>3. Operators, Division Rules & Algorithms</h3>
        <div class="grid-2">
          <div>
            <h4 style="color:#38bdf8; margin-bottom:8px;">Integer Division (//) & Modulo (%)</h4>
            <p><code>//</code> rounds DOWN towards &minus;&infin; (negative infinity).</p>
            <pre><code># The Invariant: a = (a // b) * b + (a % b)
17 // 5  = 3   |  17 % 5  = 2
-17 // 5 = -4  |  -17 % 5 = 3
# Because: -17 = (-4 * 5) + 3</code></pre>
          </div>
          <div>
            <h4 style="color:#10b981; margin-bottom:8px;">Digit Extraction & Decomposition</h4>
            <pre><code>n = 1234
last_digit = n % 10          # 4
without_last = n // 10       # 123
tens_digit = (n // 10) % 10  # 3</code></pre>
          </div>
        </div>
      </div>
    </section>

        <!-- Week 2 -->
    <section id="week2" class="bible-week">
      <div class="section-header">
        <div class="section-num">2</div>
        <h2>Week 2: Conditionals & Functions (Part 1)</h2>
      </div>

      <div class="card">
        <h3>1. Logical Operators & Short-Circuit Evaluation</h3>
        <p>Precedence order: <strong><code>not</code> &gt; <code>and</code> &gt; <code>or</code></strong>.</p>
        <div class="callout callout-tip">
          <strong>Short-Circuit Evaluation Mechanism:</strong>
          <ul>
            <li>In <code>A or B</code>: if <code>A</code> evaluates to True, Python knows the result must be True, so <code>B</code> is NEVER evaluated.</li>
            <li>In <code>A and B</code>: if <code>A</code> evaluates to False, Python knows the result must be False, so <code>B</code> is NEVER evaluated.</li>
          </ul>
          <pre><code>x = 5
if x > 2 or x / 0 > 1:  # x / 0 is SKIPPED, preventing a crash!
    print("Safe")</code></pre>
        </div>
      </div>

      <div class="card">
        <h3>2. Finding the Maximum of 3 Numbers: 3 Approaches</h3>
        <pre><code># Approach A: Compound Conditions
if a >= b and a >= c:
    m = a
elif b >= a and b >= c:
    m = b
else:
    m = c

# Approach B: Running Maximum (Most maintainable and scalable)
m = a
if b > m:
    m = b
if c > m:
    m = c

# Approach C: Nested Conditionals
if a >= b:
    if a >= c:
        m = a
    else:
        m = c
else:
    if b >= c:
        m = b
    else:
        m = c</code></pre>
      </div>

      <div class="card">
        <h3>3. Leap Year Algorithm & Predicate Functions</h3>
        <pre><code>def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Compact Boolean expression:
def is_leap_year_compact(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)</code></pre>
      </div>
    </section>

        <!-- Week 3 -->
    <section id="week3" class="bible-week">
      <div class="section-header">
        <div class="section-num">3</div>
        <h2>Week 3: Functions (Part 2), Scope & Loops</h2>
      </div>

      <div class="card">
        <h3>1. <code>for</code> Loops & <code>range()</code> Signatures</h3>
        <table class="custom-table">
          <tr><th>Signature</th><th>Call Example</th><th>Sequence Generated</th><th>Notes</th></tr>
          <tr><td><code>range(stop)</code></td><td><code>range(4)</code></td><td><code>0, 1, 2, 3</code></td><td>Starts at 0, stops before 4</td></tr>
          <tr><td><code>range(start, stop)</code></td><td><code>range(1, 5)</code></td><td><code>1, 2, 3, 4</code></td><td>Starts at 1, stops before 5</td></tr>
          <tr><td><code>range(start, stop, step)</code></td><td><code>range(1, 10, 2)</code></td><td><code>1, 3, 5, 7, 9</code></td><td>Steps by +2</td></tr>
          <tr><td>Negative Step</td><td><code>range(5, 0, -1)</code></td><td><code>5, 4, 3, 2, 1</code></td><td>Counts down; stops strictly BEFORE 0!</td></tr>
        </table>
      </div>

      <div class="card">
        <h3>2. Classic Loop Patterns</h3>
        <pre><code># Pattern 1: Accumulator (Sum & Factorial)
total = 0                 # Neutral element for addition is 0
for i in range(1, n + 1):
    total += i

fact = 1                  # Neutral element for multiplication is 1
for i in range(1, n + 1):
    fact *= i

# Pattern 2: Running Maximum (Handling Negatives Properly)
largest = nums[0]         # Never initialize to 0!
for x in nums[1:]:
    if x > largest:
        largest = x

# Pattern 3: Sentinel While Loop (-1 to Stop)
val = int(input("Enter number (-1 to stop): ")) # Read BEFORE
total = 0
while val != -1:
    total += val
    val = int(input("Enter number (-1 to stop): ")) # Read at BOTTOM</code></pre>
      </div>
    </section>

        <!-- Week 4 -->
    <section id="week4" class="bible-week">
      <div class="section-header">
        <div class="section-num">4</div>
        <h2>Week 4: Nested Loops & Code Tracing</h2>
      </div>

      <div class="card">
        <h3>1. Nested Loop Multiplicative Work</h3>
        <p>If the outer loop iterates <em>R</em> times and the inner loop iterates <em>C</em> times, the inner loop body executes <em>R</em> &times; <em>C</em> times.</p>
        <pre><code># Nested: Multiplies work (1,000 * 1,000 = 1,000,000 executions)
for i in range(1000):
    for j in range(1000):
        print(j)

# Sequential: Adds work (1,000 + 1,000 = 2,000 executions)
for i in range(1000):
    print(i)
for j in range(1000):
    print(j)</code></pre>
      </div>

      <div class="card">
        <h3>2. Prime Number Algorithms: Early Break vs Counter</h3>
        <pre><code># Flag with Early Exit (Fastest)
def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False   # Immediately stop on first divisor
    return True            # Outside loop!

# Divisor Counter (Exhaustive)
def is_prime_counter(n):
    if n < 2:
        return False
    count = 0
    for d in range(1, n + 1):
        if n % d == 0:
            count += 1
    return count == 2</code></pre>
      </div>

      <div class="card">
        <h3>3. 2D Coordinate Grid Diagonals</h3>
        <pre><code>n = 4
for i in range(n):
    for j in range(n):
        if i == j:
            print("X", end="")  # Main Diagonal
        elif i + j == n - 1:
            print("O", end="")  # Anti-Diagonal
        else:
            print("-", end="")
    print()</code></pre>
      </div>
    </section>

        <!-- Week 5 -->
    <section id="week5" class="bible-week">
      <div class="section-header">
        <div class="section-num">5</div>
        <h2>Week 5: Strings & Slicing Masterclass</h2>
      </div>

      <div class="card">
        <h3>1. Complete String Slicing Traversal Table</h3>
        <table class="custom-table">
          <tr><th>Slice Call</th><th>Result for <code>'PYTHON'</code></th><th>Explanation</th></tr>
          <tr><td><code>s[0:6]</code></td><td><code>'PYTHON'</code></td><td>From index 0 to 6 (excluded)</td></tr>
          <tr><td><code>s[0:6:1]</code></td><td><code>'PYTHON'</code></td><td>Explicit step +1</td></tr>
          <tr><td><code>s[0:6:-1]</code></td><td><code>''</code></td><td>Negative step cannot travel from 0 to 6</td></tr>
          <tr><td><code>s[-1:-7:-1]</code></td><td><code>'NOHTYP'</code></td><td>From -1 down to -7 stepping -1</td></tr>
          <tr><td><code>s[::-1]</code></td><td><code>'NOHTYP'</code></td><td>Full reverse shorthand</td></tr>
          <tr><td><code>s[4:1:-1]</code></td><td><code>'OHT'</code></td><td>Indices 4, 3, 2</td></tr>
          <tr><td><code>s[-2:-5:-1]</code></td><td><code>'OHT'</code></td><td>Negative index reverse slice</td></tr>
          <tr><td><code>s[-5:-1:1]</code></td><td><code>'YTHO'</code></td><td>Negative index forward slice</td></tr>
          <tr><td><code>s[::2]</code></td><td><code>'PTO'</code></td><td>Every second character (0, 2, 4)</td></tr>
          <tr><td><code>s[0:30:1]</code></td><td><code>'PYTHON'</code></td><td>Graceful out-of-bounds clamping</td></tr>
        </table>
      </div>

      <div class="card">
        <h3>2. String Methods Directory</h3>
        <table class="custom-table">
          <tr><th>Method</th><th>Sample Call</th><th>Result</th><th>Notes</th></tr>
          <tr><td><code>.upper() / .lower()</code></td><td><code>'Hi'.upper()</code></td><td><code>'HI'</code></td><td>Returns new string; does not alter original</td></tr>
          <tr><td><code>.strip()</code></td><td><code>' cat '.strip()</code></td><td><code>'cat'</code></td><td>Strips leading & trailing whitespace</td></tr>
          <tr><td><code>.find(sub)</code></td><td><code>'banana'.find('na')</code></td><td><code>2</code></td><td>Index of first match; returns <strong>-1</strong> if not found</td></tr>
          <tr><td><code>.count(sub)</code></td><td><code>'banana'.count('a')</code></td><td><code>3</code></td><td>Non-overlapping occurrences count</td></tr>
          <tr><td><code>.replace(old, new)</code></td><td><code>'banana'.replace('a', 'o')</code></td><td><code>'bonono'</code></td><td>Replaces all occurrences</td></tr>
          <tr><td><code>.split(sep)</code></td><td><code>'a,b,c'.split(',')</code></td><td><code>['a', 'b', 'c']</code></td><td>Splits into list of strings</td></tr>
          <tr><td><code>sep.join(list)</code></td><td><code>'-'.join(['a', 'b'])</code></td><td><code>'a-b'</code></td><td>Joins list of strings with separator</td></tr>
        </table>
      </div>
    </section>

        <!-- Week 6 -->
    <section id="week6" class="bible-week">
      <div class="section-header">
        <div class="section-num">6</div>
        <h2>Week 6: Lists in Practice & Advanced Algorithms</h2>
      </div>

      <div class="card">
        <h3>1. Key Algorithms from Slides</h3>
        <pre><code># 1. Generate 100 UNIQUE Random Numbers
import random
nums = []
while len(nums) < 100:
    r = random.randint(0, 1000)
    if r not in nums:
        nums.append(r)
nums.sort()

# 2. Sublist Sliding Window (is_sublist)
def is_sublist(a, b):
    n = len(a)
    for i in range(len(b) - n + 1):
        if b[i:i + n] == a:
            return True
    return False

# 3. Frequency Counter List (Histogram)
counts = [0] * 3
for n in [0, 1, 1, 2, 1]:
    counts[n] += 1
# counts is [1, 3, 1]

# 4. Safe Merging of Unequal Lists
def merge_lists(a, b):
    res = []
    n = min(len(a), len(b))
    for i in range(n):
        res.append(a[i])
        res.append(b[i])
    res += a[n:] + b[n:]
    return res</code></pre>
      </div>

      <div class="card">
        <h3>2. The 6-Point Exam Edge Case Checklist</h3>
        <ol style="margin-left:20px; color:#cbd5e1; line-height:1.8;">
          <li><strong>Empty list <code>[]</code>:</strong> Checks whether code crashes on <code>a[0]</code>, <code>max(a)</code>, or division by zero (<code>sum(a)/len(a)</code>).</li>
          <li><strong>Single-element list <code>[x]</code>:</strong> Neighbor loops with <code>range(len(a) - 1)</code> run 0 times. Does the function return the right default?</li>
          <li><strong>All duplicates <code>[3, 3, 3]</code>:</strong> Does uniqueness or search logic behave properly?</li>
          <li><strong>Missing target:</strong> When searching for a non-existent element, does the code return <code>-1</code> or <code>False</code> without throwing an error?</li>
          <li><strong>Unequal lengths:</strong> Parallel lists or merge functions with lists of different sizes.</li>
          <li><strong>All negative numbers <code>[-5, -2, -9]</code>:</strong> Running maximum functions must not be initialized to <code>0</code>.</li>
        </ol>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 41 ACTIVE RECALL FLASHCARDS -->
    <!-- ========================================================================= -->
    </div>
    <div id="flashcards" class="tab-pane">
    <section>
      <div class="section-header">
        <div class="section-num">🃏</div>
        <h2>41 Active Recall Flashcards</h2>
      </div>
      <p class="section-desc">Click any card to flip and test your knowledge. Use the category pills to filter cards by week.</p>

      <div class="quick-filter-pills" id="flashcardFilters">
        <button class="pill-btn active" onclick="filterFlashcards('All')">All (41)</button>
        <button class="pill-btn" onclick="filterFlashcards('Week 1')">Week 1</button>
        <button class="pill-btn" onclick="filterFlashcards('Week 2')">Week 2</button>
        <button class="pill-btn" onclick="filterFlashcards('Week 3')">Week 3</button>
        <button class="pill-btn" onclick="filterFlashcards('Week 4')">Week 4</button>
        <button class="pill-btn" onclick="filterFlashcards('Week 5')">Week 5</button>
        <button class="pill-btn" onclick="filterFlashcards('Week 6')">Week 6</button>
      </div>

      <div class="flashcards-container" id="cardsDeck"></div>
    </section>

    <!-- ========================================================================= -->
    <!-- 40-QUESTION MIDTERM MOCK EXAM -->
    <!-- ========================================================================= -->
    </div>
    <div id="mock-exam" class="tab-pane">
    <section>
      <div class="section-header">
        <div class="section-num">📝</div>
        <h2>Midterm Mock Exam (40 Questions)</h2>
      </div>
      <p class="section-desc">Interactive practice test covering the entire midterm syllabus. Answer all questions to see your final score and detailed explanations.</p>

      <div class="quick-filter-pills" id="quizFilters">
        <button class="pill-btn active" onclick="filterQuiz('All')">All Questions (40)</button>
        <button class="pill-btn" onclick="filterQuiz('Week 1')">Week 1</button>
        <button class="pill-btn" onclick="filterQuiz('Week 2')">Week 2</button>
        <button class="pill-btn" onclick="filterQuiz('Week 3')">Week 3</button>
        <button class="pill-btn" onclick="filterQuiz('Week 4')">Week 4</button>
        <button class="pill-btn" onclick="filterQuiz('Week 5')">Week 5</button>
        <button class="pill-btn" onclick="filterQuiz('Week 6')">Week 6</button>
      </div>

      <div class="quiz-progress-bar">
        <div class="quiz-progress-fill" id="quizProgress"></div>
      </div>

      <div class="score-banner" id="scoreBanner">
        <div>
          <h3 style="font-size: 1.35rem; color: #f8fafc; margin-bottom: 4px;">Score: <span id="userScore" style="color:#38bdf8;">0</span> / <span id="totalVisibleQ">40</span></h3>
          <p style="font-size: 0.88rem; color: #94a3b8;" id="scoreComment">Select an answer for each question below.</p>
        </div>
        <button class="btn-retake" onclick="resetQuiz()">🔄 Reset / Retake Mock Exam</button>
      </div>

      <div id="quizContainer"></div>
    </section>

  
    </div>

    <!-- Floating Back to Top -->
    <button class="back-to-top" id="backToTop" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" title="Back to top">↑</button>

        <!-- Mobile App Bottom Dock -->
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
      <a class="dock-item" id="dock-lecture-notes" onclick="switchTab('lecture-notes')">
        <span class="dock-icon">📖</span>
        <span>Notes</span>
      </a>
    </nav>

  </main>

  <script>
    // Injected Data
    const trapsData = ''' + json.dumps(traps) + ''';
    const flashcardsData = ''' + json.dumps(flashcards) + ''';
    const quizData = ''' + json.dumps(quiz) + ''';

    // Global App State
    let userAnswers = {};
    let currentQuizFilter = 'All';
    let currentCardFilter = 'All';

    // --- Mobile Sidebar Toggle ---
    function toggleSidebar() {
      document.getElementById('sidebar').classList.toggle('open');
    }

    function jumpSection(id) {
      const el = document.getElementById(id);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
        if (window.innerWidth <= 960) {
          document.getElementById('sidebar').classList.remove('open');
        }
      }
    }

    // --- Accordions ---
    function toggleAccordion(header) {
      const parent = header.parentElement;
      parent.classList.toggle('open');
    }

    function renderTraps() {
      const container = document.getElementById('trapsContainer');
      container.innerHTML = '';
      trapsData.forEach(t => {
        const el = document.createElement('div');
        el.className = 'accordion';
        el.id = `trap-acc-${t.id}`;
        el.innerHTML = `
          <div class="accordion-header" onclick="toggleAccordion(this)">
            <span><strong style="color:#38bdf8;">Trap #${t.id}:</strong> ${t.title} <span style="font-size:0.75rem; background:#1e293b; color:#94a3b8; padding:2px 8px; border-radius:10px; margin-left:8px;">${t.category}</span></span>
            <span class="accordion-icon">▼</span>
          </div>
          <div class="accordion-body">
            <div class="callout callout-danger">
              <strong>❌ Faulty / Exam Snippet:</strong>
              <pre><code>${escapeHtml(t.buggy)}</code></pre>
              <strong>Result / Output:</strong> <code>${escapeHtml(t.result)}</code>
            </div>
            <p><strong>💡 Why It Happens:</strong> ${t.explanation}</p>
            <div class="callout callout-tip" style="margin-top:14px;">
              <strong>✅ Correct Fix:</strong>
              <pre><code>${escapeHtml(t.fix)}</code></pre>
            </div>
          </div>
        `;
        container.appendChild(el);
      });
      if (document.getElementById('globalSearch') && document.getElementById('globalSearch').value.trim() !== '') {
        filterGlobalSearch();
      }
    }

    function escapeHtml(str) {
      return str.replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#039;");
    }

    // --- Slicing Lab v2 (Strict CPython-Exact) ---
    function applyPreset(text, start, stop, step) {
      document.getElementById('sliceText').value = text;
      document.getElementById('sliceStart').value = start;
      document.getElementById('sliceStop').value = stop;
      document.getElementById('sliceStep').value = step;
      updateVisualizer();
    }

    function updateVisualizer() {
      const text = document.getElementById('sliceText').value;
      const startVal = document.getElementById('sliceStart').value.trim();
      const stopVal = document.getElementById('sliceStop').value.trim();
      const stepVal = document.getElementById('sliceStep').value.trim();

      const n = text.length;
      const boxesContainer = document.getElementById('visualBoxes');
      boxesContainer.innerHTML = '';

      for (let i = 0; i < n; i++) {
        const box = document.createElement('div');
        box.className = 'char-box';
        box.id = `char-box-${i}`;

        const posIdx = document.createElement('div');
        posIdx.className = 'pos-idx';
        posIdx.textContent = i;

        const charVal = document.createElement('div');
        charVal.className = 'char-val';
        charVal.textContent = text[i];

        const negIdx = document.createElement('div');
        negIdx.className = 'neg-idx';
        negIdx.textContent = i - n;

        box.appendChild(posIdx);
        box.appendChild(charVal);
        box.appendChild(negIdx);
        boxesContainer.appendChild(box);
      }

      let step = stepVal === '' ? 1 : parseInt(stepVal);
      if (isNaN(step)) step = 1;

      if (step === 0) {
        document.getElementById('sliceVal').textContent = 'ValueError: slice step cannot be zero';
        document.getElementById('sliceVal').style.color = '#fb7185';
        document.getElementById('sliceLen').textContent = 0;
        document.getElementById('sliceExplanation').innerHTML = 
          '<span style="color:#fb7185; font-weight:700;">⚠️ Python Exception:</span> Slice step cannot be zero (raises ValueError in Python).';
        return;
      }

      document.getElementById('sliceVal').style.color = '#f8fafc';

      let start, stop;
      if (step > 0) {
        if (startVal === '') {
          start = 0;
        } else {
          start = parseInt(startVal);
          if (isNaN(start)) start = 0;
          if (start < 0) start = Math.max(0, n + start);
          else if (start > n) start = n;
        }

        if (stopVal === '') {
          stop = n;
        } else {
          stop = parseInt(stopVal);
          if (isNaN(stop)) stop = n;
          if (stop < 0) stop = Math.max(0, n + stop);
          else if (stop > n) stop = n;
        }
      } else {
        if (startVal === '') {
          start = n - 1;
        } else {
          start = parseInt(startVal);
          if (isNaN(start)) start = n - 1;
          if (start < 0) start = n + start;
          else if (start >= n) start = n - 1;
          if (start < -1) start = -1;
        }

        if (stopVal === '') {
          stop = -1;
        } else {
          stop = parseInt(stopVal);
          if (isNaN(stop)) stop = -1;
          if (stop < 0) stop = n + stop;
          else if (stop >= n) stop = n - 1;
          if (stop < -1) stop = -1;
        }
      }

      let resultChars = [];
      let selectedIndices = [];

      if (step > 0) {
        for (let i = start; i < stop; i += step) {
          if (i >= 0 && i < n) {
            resultChars.push(text[i]);
            selectedIndices.push(i);
          }
        }
      } else {
        for (let i = start; i > stop; i += step) {
          if (i >= 0 && i < n) {
            resultChars.push(text[i]);
            selectedIndices.push(i);
          }
        }
      }

      selectedIndices.forEach(idx => {
        const box = document.getElementById(`char-box-${idx}`);
        if (box) box.classList.add('selected');
      });

      const resStr = resultChars.join('');
      document.getElementById('sliceVal').textContent = `'${resStr}'`;
      document.getElementById('sliceLen').textContent = resStr.length;

      let exp = `Slice representation: text[${startVal === '' ? '' : startVal}:${stopVal === '' ? '' : stopVal}:${stepVal === '' ? '' : stepVal}] → Selected ${selectedIndices.length} character(s).`;
      if (resStr.length === 0) {
        exp += ` (Note: Yielded empty string '' due to index ordering or step direction conflict)`;
      }
      document.getElementById('sliceExplanation').textContent = exp;
    }

    // --- Interactive Call Stack Stepper ---
    const stackSteps = [
      {
        frames: [
          { name: '<Global Scope>', vars: 'main = &lt;function&gt;, circle_area = &lt;function&gt;, distance = &lt;function&gt;' }
        ],
        desc: 'Step 1: Python defines all functions in the Global Scope. Execution begins at the call main().'
      },
      {
        frames: [
          { name: '<Global Scope>', vars: '...' },
          { name: 'main() Frame', vars: 'Waiting for circle_area()' }
        ],
        desc: 'Step 2: main() is called. A new stack frame for main is pushed to the call stack.'
      },
      {
        frames: [
          { name: '<Global Scope>', vars: '...' },
          { name: 'main() Frame', vars: 'Waiting on a1...' },
          { name: 'circle_area(0, 0, 3, 4) Frame', vars: 'cx=0, cy=0, px=3, py=4 | Calling distance()' }
        ],
        desc: 'Step 3: circle_area is invoked with arguments (0, 0, 3, 4). Parameters become local variables in its frame.'
      },
      {
        frames: [
          { name: '<Global Scope>', vars: '...' },
          { name: 'main() Frame', vars: 'Waiting...' },
          { name: 'circle_area() Frame', vars: 'Waiting on r...' },
          { name: 'distance(0, 0, 3, 4) Frame', vars: 'x1=0, y1=0, x2=3, y2=4 | returns 5.0' }
        ],
        desc: 'Step 4: distance() is called. Its frame is pushed on top. It computes sqrt((0-3)^2 + (0-4)^2) = 5.0 and returns 5.0.'
      },
      {
        frames: [
          { name: '<Global Scope>', vars: '...' },
          { name: 'main() Frame', vars: 'Waiting on a1...' },
          { name: 'circle_area() Frame', vars: 'r = 5.0 | Computing pi * 5^2 -> returns 78.54' }
        ],
        desc: 'Step 5: distance() frame is POPPED and destroyed! Return value 5.0 is assigned to local variable r in circle_area. It computes area = 78.54 and returns it.'
      },
      {
        frames: [
          { name: '<Global Scope>', vars: '...' },
          { name: 'main() Frame', vars: 'a1 = 78.54 | Prints: Area: 78.54' }
        ],
        desc: 'Step 6: circle_area() frame is POPPED and destroyed! Return value 78.54 is stored in local variable a1 in main(). main() finishes and returns None.'
      },
      {
        frames: [
          { name: '<Global Scope>', vars: 'All function calls completed.' }
        ],
        desc: 'Step 7: All local frames destroyed. Only Global Scope remains.'
      }
    ];

    let currentStackStep = 0;

    function renderStack() {
      const container = document.getElementById('stackFramesContainer');
      container.innerHTML = '';
      const step = stackSteps[currentStackStep];

      for (let i = step.frames.length - 1; i >= 0; i--) {
        const f = step.frames[i];
        const el = document.createElement('div');
        el.className = 'stack-frame' + (i === step.frames.length - 1 ? ' active' : '');
        el.innerHTML = `
          <div>
            <strong style="color:#38bdf8;">${f.name}</strong>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'Fira Code', monospace;">${f.vars}</div>
          </div>
          <span style="font-size:0.75rem; background:#1e293b; color:#38bdf8; padding:2px 8px; border-radius:12px;">Frame #${i+1}</span>
        `;
        container.appendChild(el);
      }

      document.getElementById('stackStepExplanation').textContent = step.desc;
    }

    function stepStack(delta) {
      currentStackStep = Math.max(0, Math.min(stackSteps.length - 1, currentStackStep + delta));
      renderStack();
    }

    function resetStack() {
      currentStackStep = 0;
      renderStack();
    }

    // --- Flashcards Logic ---
    function renderFlashcards() {
      const container = document.getElementById('cardsDeck');
      container.innerHTML = '';
      const filtered = flashcardsData.filter(c => currentCardFilter === 'All' || c.week === currentCardFilter);

      filtered.forEach((card, idx) => {
        const el = document.createElement('div');
        el.className = 'flashcard';
        el.onclick = () => el.classList.toggle('flipped');
        el.innerHTML = `
          <div class="flashcard-inner">
            <div class="flashcard-front">
              <span style="font-size:0.75rem; background:#1e293b; color:#38bdf8; padding:2px 8px; border-radius:12px; margin-bottom:8px;">${card.week}</span>
              <h4>Card #${idx + 1}</h4>
              <p>${escapeHtml(card.q)}</p>
              <span style="font-size:0.75rem; color:#64748b; margin-top:12px;">(Click to reveal answer)</span>
            </div>
            <div class="flashcard-back">
              <strong style="color:#38bdf8; margin-bottom:8px; display:block;">Answer:</strong>
              <div style="white-space: pre-line;">${escapeHtml(card.a)}</div>
            </div>
          </div>
        `;
        container.appendChild(el);
      });
      if (document.getElementById('globalSearch') && document.getElementById('globalSearch').value.trim() !== '') {
        filterGlobalSearch();
      }
    }

    function filterFlashcards(week) {
      currentCardFilter = week;
      document.querySelectorAll('#flashcardFilters .pill-btn').forEach(btn => {
        btn.classList.toggle('active', btn.textContent.includes(week));
      });
      renderFlashcards();
    }

    // --- Quiz Logic ---
    function renderQuiz() {
      const container = document.getElementById('quizContainer');
      container.innerHTML = '';
      const filtered = quizData.filter(q => currentQuizFilter === 'All' || q.week === currentQuizFilter);
      document.getElementById('totalVisibleQ').textContent = filtered.length;

      filtered.forEach((item, filteredIdx) => {
        const qIdx = item.id - 1; // 0-based original ID
        const qCard = document.createElement('div');
        qCard.className = 'quiz-card';
        qCard.id = `q-card-${qIdx}`;

        let optsHtml = '';
        item.opts.forEach((opt, optIdx) => {
          optsHtml += `
            <div class="quiz-opt" id="opt-${qIdx}-${optIdx}" onclick="handleAnswer(${qIdx}, ${optIdx})">
              <span style="font-weight:700; width:24px;">${String.fromCharCode(65 + optIdx)})</span>
              <span>${escapeHtml(opt)}</span>
            </div>
          `;
        });

        qCard.innerHTML = `
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
            <span style="font-size:0.75rem; background:#141b2d; border:1px solid #23314d; color:#38bdf8; padding:3px 10px; border-radius:12px; font-weight:700;">${item.week} &bull; ${item.category}</span>
            <span style="font-size:0.75rem; color:#64748b;">Question ${item.id} of ${quizData.length}</span>
          </div>
          <div class="quiz-q">${escapeHtml(item.q)}</div>
          <div class="quiz-options">${optsHtml}</div>
          <div class="quiz-explanation" id="exp-${qIdx}">
            <strong>💡 Explanation:</strong> ${escapeHtml(item.exp)}
          </div>
        `;
        container.appendChild(qCard);
      });

      // Restore previously answered states
      Object.keys(userAnswers).forEach(qIdx => {
        const selectedOpt = userAnswers[qIdx];
        const correctOpt = quizData[qIdx].ans;
        const selectedEl = document.getElementById(`opt-${qIdx}-${selectedOpt}`);
        const correctEl = document.getElementById(`opt-${qIdx}-${correctOpt}`);
        const expEl = document.getElementById(`exp-${qIdx}`);

        if (selectedEl && correctEl && expEl) {
          if (selectedOpt === correctOpt) {
            selectedEl.classList.add('correct');
          } else {
            selectedEl.classList.add('incorrect');
            correctEl.classList.add('correct');
          }
          expEl.style.display = 'block';
        }
      });

      updateQuizProgress();
      if (document.getElementById('globalSearch') && document.getElementById('globalSearch').value.trim() !== '') {
        filterGlobalSearch();
      }
    }

    function handleAnswer(qIdx, optIdx) {
      if (userAnswers[qIdx] !== undefined) return;
      userAnswers[qIdx] = optIdx;

      const correctOpt = quizData[qIdx].ans;
      const clickedEl = document.getElementById(`opt-${qIdx}-${optIdx}`);
      const correctEl = document.getElementById(`opt-${qIdx}-${correctOpt}`);
      const expEl = document.getElementById(`exp-${qIdx}`);

      if (optIdx === correctOpt) {
        clickedEl.classList.add('correct');
      } else {
        clickedEl.classList.add('incorrect');
        correctEl.classList.add('correct');
      }

      expEl.style.display = 'block';
      updateQuizProgress();
    }

    function updateQuizProgress() {
      const filtered = quizData.filter(q => currentQuizFilter === 'All' || q.week === currentQuizFilter);
      let answeredInFilter = 0;
      let scoreInFilter = 0;

      filtered.forEach(q => {
        const qIdx = q.id - 1;
        if (userAnswers[qIdx] !== undefined) {
          answeredInFilter++;
          if (userAnswers[qIdx] === q.ans) {
            scoreInFilter++;
          }
        }
      });

      document.getElementById('userScore').textContent = scoreInFilter;
      const pct = (answeredInFilter / filtered.length) * 100;
      document.getElementById('quizProgress').style.width = `${pct}%`;

      const commentEl = document.getElementById('scoreComment');
      if (answeredInFilter === filtered.length) {
        const ratio = scoreInFilter / filtered.length;
        if (ratio >= 0.9) {
          commentEl.textContent = '🌟 Outstanding! You are 100% prepared for an A+ on tomorrow’s midterm!';
          commentEl.style.color = '#10b981';
        } else if (ratio >= 0.75) {
          commentEl.textContent = '👍 Great job! Review the questions you missed and the 20 traps above.';
          commentEl.style.color = '#38bdf8';
        } else {
          commentEl.textContent = '⚠️ Keep reviewing! Pay special attention to Slicing, Operators, and Return vs Print.';
          commentEl.style.color = '#f59e0b';
        }
      } else {
        commentEl.textContent = `Answered ${answeredInFilter} of ${filtered.length} questions.`;
        commentEl.style.color = '#94a3b8';
      }
    }

    function resetQuiz() {
      userAnswers = {};
      renderQuiz();
    }

    function filterQuiz(week) {
      currentQuizFilter = week;
      document.querySelectorAll('#quizFilters .pill-btn').forEach(btn => {
        btn.classList.toggle('active', btn.textContent.includes(week));
      });
      renderQuiz();
    }

    // --- Global Search Filter ---
    function filterGlobalSearch() {
      const query = document.getElementById('globalSearch').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.card, .accordion, .quiz-card, .flashcard');

      if (query === '') {
        cards.forEach(c => c.style.display = '');
        return;
      }

      cards.forEach(c => {
        const text = c.textContent.toLowerCase();
        if (text.includes(query)) {
          c.style.display = '';
        } else {
          c.style.display = 'none';
        }
      });
    }

    
    // --- TAB SWITCHING SYSTEM (Zero Scroll Hell) ---
    const allTabIds = [
      'cram-sheet',
      'functions-directory',
      'slicing-lab',
      'call-stack-lab',
      'traps',
      'flashcards',
      'mock-exam',
      'lecture-notes'
    ];

    function switchTab(tabId) {
      if (tabId === 'lecture-bible') tabId = 'lecture-notes';
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

    function filterBibleWeek(weekId) { return filterNotesWeek(weekId); }
    function filterNotesWeek(weekId) {
      document.querySelectorAll('#lecture-notes .pill-btn').forEach(btn => {
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

    // --- On Load Initialization ---
    window.onload = function() {
      renderTraps();
      updateVisualizer();
      renderStack();
      renderFlashcards();
      renderQuiz();
      setupCopyCodeButtons();
      wrapTablesForMobile();

      // Read hash from URL if present
      const hash = window.location.hash.replace('#', '');
      if (hash && allTabIds.includes(hash)) {
        switchTab(hash);
      } else {
        switchTab('cram-sheet');
      }
    };
  
    // --- Pro Copy Code Buttons ---
    function setupCopyCodeButtons() {
      document.querySelectorAll('pre').forEach((pre, idx) => {
        // Prevent double-wrapping
        if (pre.parentElement.classList.contains('code-wrapper')) return;

        const wrapper = document.createElement('div');
        wrapper.className = 'code-wrapper';

        const header = document.createElement('div');
        header.className = 'code-header';
        header.innerHTML = `
          <span class="code-lang">🐍 Python 3</span>
          <button class="btn-copy" onclick="copySnippet(this, ${idx})">
            <span>📋</span>
            <span>Copy</span>
          </button>
        `;

        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(header);
        wrapper.appendChild(pre);
      });
    }

    function copySnippet(btn, idx) {
      const pre = btn.closest('.code-wrapper').querySelector('pre');
      const text = pre.innerText || pre.textContent;

      navigator.clipboard.writeText(text).then(() => {
        btn.classList.add('copied');
        btn.innerHTML = '<span>✓</span><span>Copied!</span>';
        setTimeout(() => {
          btn.classList.remove('copied');
          btn.innerHTML = '<span>📋</span><span>Copy</span>';
        }, 2000);
      }).catch(err => {
        console.error('Copy failed: ', err);
      });
    }

    // --- Table Responsive Wrappers ---
    function wrapTablesForMobile() {
      document.querySelectorAll('table.custom-table').forEach(table => {
        if (table.parentElement.classList.contains('table-container')) return;
        const container = document.createElement('div');
        container.className = 'table-container';
        table.parentNode.insertBefore(container, table);
        container.appendChild(table);
      });
    }

    // --- Back to Top Listener ---
    window.addEventListener('scroll', () => {
      const btn = document.getElementById('backToTop');
      if (window.scrollY > 300) {
        btn.classList.add('show');
      } else {
        btn.classList.remove('show');
      }
    });

    // Enhance window.onload
    const originalOnload = window.onload;
    window.onload = function() {
      if (originalOnload) originalOnload();
      setupCopyCodeButtons();
      wrapTablesForMobile();
    };

  </script>
</body>
</html>
'''

with open(r'c:\Users\Fadi\Desktop\loops cs\index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Master Revision Hub v2 generated successfully at index.html!")
