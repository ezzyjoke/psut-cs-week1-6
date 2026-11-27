# Python script to build the PSUT 11102 Midterm Revision website
import os

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PSUT 11102 · Introduction to Computing — Complete Midterm Revision Master Hub</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0b0f19;
      --card-bg: #111827;
      --card-border: #1f293d;
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --accent-blue: #38bdf8;
      --accent-indigo: #818cf8;
      --accent-purple: #c084fc;
      --accent-emerald: #34d399;
      --accent-amber: #fbbf24;
      --accent-rose: #fb7185;
      --code-bg: #0d1117;
      --code-border: #30363d;
      --sidebar-w: 290px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.65;
      display: flex;
      min-height: 100vh;
      overflow-x: hidden;
    }

    /* Sidebar Navigation */
    aside.sidebar {
      width: var(--sidebar-w);
      background: #0d121f;
      border-right: 1px solid var(--card-border);
      position: fixed;
      top: 0;
      bottom: 0;
      left: 0;
      overflow-y: auto;
      padding: 24px 16px;
      display: flex;
      flex-direction: column;
      z-index: 50;
      transition: transform 0.3s ease;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      padding-bottom: 20px;
      border-bottom: 1px solid var(--card-border);
      margin-bottom: 20px;
    }

    .brand-logo {
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, #0284c7, #6366f1);
      border-radius: 10px;
      display: grid;
      place-items: center;
      font-weight: 800;
      font-size: 20px;
      color: #fff;
    }

    .brand-title {
      font-weight: 700;
      font-size: 0.95rem;
      line-height: 1.25;
      color: #fff;
    }

    .brand-sub {
      font-size: 0.75rem;
      color: var(--accent-blue);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .nav-group-title {
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #64748b;
      margin: 18px 8px 8px;
      font-weight: 700;
    }

    .nav-link {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 12px;
      border-radius: 8px;
      color: #94a3b8;
      text-decoration: none;
      font-size: 0.88rem;
      font-weight: 500;
      transition: all 0.15s ease;
      margin-bottom: 3px;
    }

    .nav-link:hover, .nav-link.active {
      background: #1e293b;
      color: #38bdf8;
    }

    .nav-badge {
      margin-left: auto;
      background: #1e293b;
      color: #38bdf8;
      font-size: 0.7rem;
      padding: 2px 7px;
      border-radius: 12px;
      font-weight: 600;
    }

    /* Main Content */
    main.content {
      margin-left: var(--sidebar-w);
      flex: 1;
      padding: 40px 48px 120px;
      max-width: 1200px;
    }

    @media (max-width: 900px) {
      aside.sidebar {
        transform: translateX(-100%);
      }
      aside.sidebar.open {
        transform: translateX(0);
      }
      main.content {
        margin-left: 0;
        padding: 24px 16px 80px;
      }
      .mobile-toggle {
        display: block !important;
      }
    }

    .mobile-toggle {
      display: none;
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: #38bdf8;
      color: #0b0f19;
      border: none;
      border-radius: 50%;
      width: 52px;
      height: 52px;
      font-size: 24px;
      font-weight: bold;
      z-index: 99;
      box-shadow: 0 4px 16px rgba(56, 189, 248, 0.4);
      cursor: pointer;
    }

    /* Hero Banner */
    .hero {
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.85), rgba(15, 23, 42, 0.95)), radial-gradient(circle at top right, rgba(56, 189, 248, 0.15), transparent);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 36px 32px;
      margin-bottom: 40px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
      position: relative;
      overflow: hidden;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #38bdf8;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 600;
      margin-bottom: 16px;
    }

    .hero h1 {
      font-size: 2.3rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin-bottom: 12px;
      background: linear-gradient(to right, #ffffff, #cbd5e1);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero p {
      font-size: 1.05rem;
      color: #94a3b8;
      max-width: 800px;
      margin-bottom: 24px;
    }

    .stats-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
      margin-top: 24px;
    }

    .stat-card {
      background: rgba(17, 24, 39, 0.7);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 16px;
      text-align: center;
    }

    .stat-num {
      font-size: 1.8rem;
      font-weight: 800;
      color: #38bdf8;
      font-family: 'Fira Code', monospace;
    }

    .stat-label {
      font-size: 0.8rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Section Styles */
    section {
      margin-bottom: 60px;
      scroll-margin-top: 30px;
    }

    .section-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 24px;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--card-border);
    }

    .section-num {
      width: 36px;
      height: 36px;
      background: rgba(56, 189, 248, 0.15);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 10px;
      display: grid;
      place-items: center;
      font-weight: 800;
      font-size: 1.05rem;
    }

    .section-header h2 {
      font-size: 1.6rem;
      font-weight: 700;
      color: #f8fafc;
    }

    .section-desc {
      color: #94a3b8;
      margin-bottom: 24px;
      font-size: 0.98rem;
    }

    /* Cards */
    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
    }

    .card h3 {
      font-size: 1.25rem;
      font-weight: 600;
      margin-bottom: 12px;
      color: #e2e8f0;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .grid-2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 20px;
    }

    /* Tables */
    .custom-table {
      width: 100%;
      border-collapse: collapse;
      margin: 16px 0;
      font-size: 0.9rem;
    }

    .custom-table th, .custom-table td {
      border: 1px solid var(--card-border);
      padding: 10px 14px;
      text-align: left;
    }

    .custom-table th {
      background: #1e293b;
      color: #f8fafc;
      font-weight: 600;
    }

    .custom-table tr:nth-child(even) {
      background: rgba(30, 41, 59, 0.4);
    }

    /* Code Blocks */
    pre {
      background: var(--code-bg);
      border: 1px solid var(--code-border);
      border-radius: 10px;
      padding: 16px;
      overflow-x: auto;
      font-family: 'Fira Code', monospace;
      font-size: 0.88rem;
      line-height: 1.6;
      color: #e2e8f0;
      margin: 12px 0;
      position: relative;
    }

    code {
      font-family: 'Fira Code', monospace;
      font-size: 0.88em;
      background: rgba(56, 189, 248, 0.1);
      color: #38bdf8;
      padding: 2px 6px;
      border-radius: 4px;
    }

    pre code {
      background: transparent;
      color: inherit;
      padding: 0;
    }

    /* Callouts */
    .callout {
      border-left: 4px solid;
      border-radius: 0 10px 10px 0;
      padding: 14px 18px;
      margin: 16px 0;
      font-size: 0.92rem;
    }

    .callout-warning {
      background: rgba(251, 191, 36, 0.08);
      border-color: var(--accent-amber);
      color: #fde68a;
    }

    .callout-danger {
      background: rgba(251, 113, 133, 0.08);
      border-color: var(--accent-rose);
      color: #fecdd3;
    }

    .callout-tip {
      background: rgba(52, 211, 153, 0.08);
      border-color: var(--accent-emerald);
      color: #a7f3d0;
    }

    .callout-info {
      background: rgba(56, 189, 248, 0.08);
      border-color: var(--accent-blue);
      color: #bae6fd;
    }

    .callout strong {
      display: block;
      margin-bottom: 4px;
      font-weight: 700;
      font-size: 0.95rem;
    }

    /* Interactive Slicing Visualizer */
    .visualizer-container {
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 14px;
      padding: 24px;
      margin: 20px 0;
    }

    .slice-inputs {
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 20px;
    }

    .input-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .input-group label {
      font-size: 0.8rem;
      font-weight: 600;
      color: #94a3b8;
    }

    .input-group input {
      background: #1e293b;
      border: 1px solid #475569;
      color: #fff;
      padding: 8px 12px;
      border-radius: 6px;
      font-family: 'Fira Code', monospace;
      font-size: 0.9rem;
      outline: none;
    }

    .input-group input:focus {
      border-color: #38bdf8;
    }

    .visual-indices {
      display: flex;
      flex-wrap: nowrap;
      overflow-x: auto;
      gap: 6px;
      padding: 16px 0;
      margin-bottom: 16px;
    }

    .char-box {
      min-width: 44px;
      display: flex;
      flex-direction: column;
      align-items: center;
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 8px 4px;
      transition: all 0.2s ease;
    }

    .char-box.selected {
      background: rgba(56, 189, 248, 0.25);
      border-color: #38bdf8;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.3);
    }

    .char-box .char-val {
      font-size: 1.25rem;
      font-weight: 700;
      font-family: 'Fira Code', monospace;
      color: #f8fafc;
      margin: 4px 0;
    }

    .char-box .pos-idx {
      font-size: 0.72rem;
      color: #34d399;
      font-family: 'Fira Code', monospace;
    }

    .char-box .neg-idx {
      font-size: 0.72rem;
      color: #fb7185;
      font-family: 'Fira Code', monospace;
    }

    .slice-result {
      background: #090d16;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 14px 18px;
      font-family: 'Fira Code', monospace;
      font-size: 1.05rem;
      color: #38bdf8;
    }

    /* Bug Accordions */
    .accordion {
      border: 1px solid var(--card-border);
      border-radius: 10px;
      margin-bottom: 12px;
      overflow: hidden;
      background: #111827;
    }

    .accordion-header {
      padding: 16px 20px;
      background: #151e2e;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-weight: 600;
      font-size: 0.95rem;
      user-select: none;
      transition: background 0.2s ease;
    }

    .accordion-header:hover {
      background: #1c273c;
    }

    .accordion-icon {
      font-size: 1.1rem;
      transition: transform 0.25s ease;
      color: #94a3b8;
    }

    .accordion.open .accordion-icon {
      transform: rotate(180deg);
    }

    .accordion-body {
      padding: 20px;
      display: none;
      border-top: 1px solid var(--card-border);
      background: #0d121d;
    }

    .accordion.open .accordion-body {
      display: block;
    }

    /* Flashcard Deck */
    .flashcards-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }

    .flashcard {
      height: 220px;
      perspective: 1000px;
      cursor: pointer;
    }

    .flashcard-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
      transform-style: preserve-3d;
      border-radius: 14px;
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
      border-radius: 14px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      border: 1px solid var(--card-border);
    }

    .flashcard-front {
      background: linear-gradient(145deg, #162032, #101726);
      color: #f1f5f9;
    }

    .flashcard-front h4 {
      font-size: 1.05rem;
      margin-bottom: 8px;
      color: #38bdf8;
    }

    .flashcard-front p {
      font-size: 0.88rem;
      color: #94a3b8;
    }

    .flashcard-back {
      background: linear-gradient(145deg, #0f2744, #0b1a2f);
      color: #e2e8f0;
      transform: rotateY(180deg);
      border-color: #0284c7;
      font-size: 0.88rem;
      line-height: 1.5;
    }

    /* Quiz styles */
    .quiz-card {
      background: #111827;
      border: 1px solid #1f293d;
      border-radius: 14px;
      padding: 24px;
      margin-bottom: 24px;
    }

    .quiz-q {
      font-size: 1.05rem;
      font-weight: 600;
      margin-bottom: 16px;
      color: #f8fafc;
    }

    .quiz-options {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .quiz-opt {
      background: #1a2234;
      border: 1px solid #2d3748;
      padding: 12px 16px;
      border-radius: 8px;
      cursor: pointer;
      font-size: 0.92rem;
      transition: all 0.15s ease;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .quiz-opt:hover {
      background: #232d42;
      border-color: #4b5563;
    }

    .quiz-opt.correct {
      background: rgba(52, 211, 153, 0.15) !important;
      border-color: #34d399 !important;
      color: #34d399;
      font-weight: 600;
    }

    .quiz-opt.incorrect {
      background: rgba(251, 113, 133, 0.15) !important;
      border-color: #fb7185 !important;
      color: #fb7185;
    }

    .quiz-explanation {
      margin-top: 14px;
      padding: 12px 16px;
      background: #0d121f;
      border-left: 3px solid #38bdf8;
      border-radius: 0 8px 8px 0;
      font-size: 0.88rem;
      color: #cbd5e1;
      display: none;
    }

    .quiz-progress-bar {
      height: 8px;
      background: #1e293b;
      border-radius: 4px;
      margin-bottom: 24px;
      overflow: hidden;
    }

    .quiz-progress-fill {
      height: 100%;
      background: linear-gradient(90deg, #38bdf8, #818cf8);
      width: 0%;
      transition: width 0.3s ease;
    }

    .score-banner {
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.1), rgba(129, 140, 248, 0.1));
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 12px;
      padding: 20px;
      text-align: center;
      margin-bottom: 24px;
    }

    /* Print styles */
    @media print {
      aside.sidebar, .mobile-toggle, .visualizer-container, .flashcards-container {
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
        box-shadow: none;
        background: #fff;
        color: #000;
      }
      pre {
        background: #f4f4f4;
        color: #000;
        border: 1px solid #ddd;
      }
    }
  </style>
</head>
<body>

  <!-- Mobile Toggle Button -->
  <button class="mobile-toggle" onclick="toggleSidebar()">☰</button>

  <!-- Sidebar -->
  <aside class="sidebar" id="sidebar">
    <div class="brand">
      <div class="brand-logo">CS</div>
      <div>
        <div class="brand-title">PSUT 11102</div>
        <div class="brand-sub">Intro to Computing</div>
      </div>
    </div>

    <div class="nav-group-title">Pre-Exam Fast Tools</div>
    <a href="#hero" class="nav-link active">⚡ Overview & Plan</a>
    <a href="#slicing-lab" class="nav-link">🔬 Interactive Slicing Lab</a>
    <a href="#traps" class="nav-link">⚠️ 15 Fatal Exam Traps <span class="nav-badge">High Yield</span></a>
    <a href="#flashcards" class="nav-link">🃏 25 Memory Flashcards</a>
    <a href="#mock-exam" class="nav-link">📝 Midterm Mock Exam <span class="nav-badge">25 Qs</span></a>

    <div class="nav-group-title">Full Course Theory</div>
    <a href="#week1" class="nav-link">📁 Week 1: Basics & Operators</a>
    <a href="#week2" class="nav-link">📁 Week 2: Conditionals & Functions 1</a>
    <a href="#week3" class="nav-link">📁 Week 3: Scope, Frames & Loops</a>
    <a href="#week4" class="nav-link">📁 Week 4: Nested Loops & Tracing</a>
    <a href="#week5" class="nav-link">📁 Week 5: Strings & Intro to Lists</a>
    <a href="#week6" class="nav-link">📁 Week 6: Lists in Practice</a>
  </aside>

  <!-- Main Content -->
  <main class="content">

    <!-- Hero -->
    <div class="hero" id="hero">
      <div class="hero-badge">🎓 Princess Sumaya University for Technology · Midterm Prep</div>
      <h1>11102 Introduction to Computing<br><span style="color:#38bdf8;">Complete Midterm Revision Hub</span></h1>
      <p>Master every concept from <strong>Week 1 through Week 6</strong>. Built precisely from your university slides and notes with comprehensive lecture notes, interactive code visualizers, spot-the-bug challenges, flashcards, and a 25-question mock exam to guarantee top marks tomorrow.</p>

      <div class="stats-row">
        <div class="stat-card">
          <div class="stat-num">6</div>
          <div class="stat-label">Full Weeks Covered</div>
        </div>
        <div class="stat-card">
          <div class="stat-num">15</div>
          <div class="stat-label">Classic Exam Traps</div>
        </div>
        <div class="stat-card">
          <div class="stat-num">25</div>
          <div class="stat-label">Mock Exam Questions</div>
        </div>
        <div class="stat-card">
          <div class="stat-num">25</div>
          <div class="stat-label">Active Recall Cards</div>
        </div>
      </div>
    </div>

    <!-- Quick Navigation Highlights Banner -->
    <div class="callout callout-tip" style="margin-bottom: 36px;">
      <strong>🎯 How to use this prep site tonight:</strong>
      <ol style="margin-left: 20px; margin-top: 6px;">
        <li>Review each Week's deep dive theory and key code patterns.</li>
        <li>Test edge-case index slicing in the <strong>Interactive Slicing Lab</strong>.</li>
        <li>Carefully read the <strong>15 Fatal Exam Traps</strong> (these are the exact tricks professors put on midterm questions).</li>
        <li>Test yourself with the <strong>25 Memory Flashcards</strong>.</li>
        <li>Complete the <strong>Full Mock Exam</strong> to lock in your score!</li>
      </ol>
    </div>

    <!-- ========================================================================= -->
    <!-- INTERACTIVE SLICING LAB -->
    <!-- ========================================================================= -->
    <section id="slicing-lab">
      <div class="section-header">
        <div class="section-num">🔬</div>
        <h2>Interactive Slicing & Indexing Lab</h2>
      </div>
      <p class="section-desc">String and list slicing (<code>s[start:stop:step]</code>) is guaranteed to appear in multiple exam questions. Use this live simulator to test any slice combination and see the exact positive/negative index positions and directional step rules.</p>

      <div class="visualizer-container">
        <div class="slice-inputs">
          <div class="input-group" style="flex: 2; min-width: 220px;">
            <label>Input Sequence (String)</label>
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
          Visual Map: <span style="color:#34d399;">Green = Positive Index</span> | <span style="color:#fb7185;">Pink = Negative Index</span> | <span style="color:#38bdf8;">Blue highlight = Selected in Slice</span>
        </div>

        <div class="visual-indices" id="visualBoxes">
          <!-- Populated by JS -->
        </div>

        <div class="slice-result" id="sliceOutput">
          Output: <span id="sliceVal" style="color: #f8fafc; font-weight: 700;">'YTHO'</span> &nbsp; | &nbsp; Length: <span id="sliceLen">4</span>
        </div>
        <div id="sliceExplanation" style="margin-top: 10px; font-size: 0.86rem; color: #94a3b8;"></div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 15 FATAL EXAM TRAPS -->
    <!-- ========================================================================= -->
    <section id="traps">
      <div class="section-header">
        <div class="section-num">⚠️</div>
        <h2>The 15 Classic Midterm Exam Traps & "Spot the Bug"</h2>
      </div>
      <p class="section-desc">Study these 15 traps closely. Midterms at PSUT test your ability to predict output and find subtle bugs under time pressure.</p>

      <!-- Trap 1 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 1: The Accidental <code>None</code> from <code>a = a.sort()</code></span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <div class="callout callout-danger">
            <strong>❌ Buggy Code:</strong>
            <pre><code>nums = [4, 2, 7]
nums = nums.sort()
print(nums)  # What prints?</code></pre>
          </div>
          <p><strong>Result:</strong> Prints <code>None</code>!</p>
          <p><strong>Explanation:</strong> <code>nums.sort()</code> sorts the list <em>in-place</em> and returns <code>None</code>. By reassigning <code>nums = nums.sort()</code>, you overwrite your list with <code>None</code>. Subsequent calls like <code>nums.append(5)</code> will crash with <code>AttributeError: 'NoneType' object has no attribute 'append'</code>.</p>
          <div class="callout callout-tip">
            <strong>✅ Correct Approaches:</strong>
            <pre><code>nums = [4, 2, 7]
nums.sort()            # Method 1: In-place, modifies original list
print(nums)            # [2, 4, 7]

# OR
nums = [4, 2, 7]
new_nums = sorted(nums) # Method 2: Returns a brand new sorted list
print(new_nums)        # [2, 4, 7]</code></pre>
          </div>
        </div>
      </div>

      <!-- Trap 2 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 2: Division <code>/</code> ALWAYS Yields a <code>float</code></span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <p><strong>Question:</strong> What is the type and exact value of <code>10 / 2</code> in Python?</p>
          <p><strong>Result:</strong> <code>5.0</code> (Type: <code>&lt;class 'float'&gt;</code>), NOT <code>5</code> (int)!</p>
          <p>In Python 3, single slash <code>/</code> is true float division. Even if the numbers divide evenly, the output is a float. If you need an integer result, you MUST use floor division <code>//</code> (e.g., <code>10 // 2</code> gives <code>5</code>).</p>
        </div>
      </div>

      <!-- Trap 3 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 3: Negative Floor Division <code>-17 // 5</code></span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <p><strong>Question:</strong> What is <code>17 // 5</code> vs <code>-17 // 5</code>?</p>
          <p><strong>Result:</strong></p>
          <ul>
            <li><code>17 // 5 = 3</code> (since 17 / 5 = 3.4, floored down is 3)</li>
            <li><code>-17 // 5 = -4</code> (since -17 / 5 = -3.4, floored down towards negative infinity is <strong>-4</strong>, NOT -3!)</li>
          </ul>
          <p><strong>Modulus Rule:</strong> <code>a = (a // b) * b + (a % b)</code>. Therefore, <code>-17 % 5 = 3</code> because <code>(-4 * 5) + 3 = -17</code>.</p>
        </div>
      </div>

      <!-- Trap 4 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 4: Right-to-Left Exponentiation <code>2 ** 3 ** 2</code></span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <p><strong>Question:</strong> What does <code>print(2 ** 3 ** 2)</code> evaluate to?</p>
          <p><strong>Result:</strong> <code>512</code>, NOT <code>64</code>!</p>
          <p><strong>Explanation:</strong> Exponentiation <code>**</code> is the ONLY common arithmetic operator with <strong>right-to-left associativity</strong>. Python evaluates it as <code>2 ** (3 ** 2) = 2 ** 9 = 512</code>. If you wanted (2³)², you must explicitly write <code>(2 ** 3) ** 2 = 64</code>.</p>
        </div>
      </div>

      <!-- Trap 5 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 5: <code>print()</code> vs <code>return</code> in Functions</span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <div class="callout callout-danger">
            <strong>❌ Classic Exam Code:</strong>
            <pre><code>def add(a, b):
    print(a + b)

res = add(3, 4)
print(res)</code></pre>
          </div>
          <p><strong>Output:</strong></p>
          <pre><code>7
None</code></pre>
          <p><strong>Explanation:</strong> <code>add(3, 4)</code> executed <code>print(7)</code> on the screen, but returned nothing. When a function has no explicit <code>return</code> statement, it returns <code>None</code> by default. Trying to do <code>res * 2</code> crashes with <code>TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'</code>.</p>
        </div>
      </div>

      <!-- Trap 6 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 6: The Unreachable Branch in <code>if-elif-else</code></span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <div class="callout callout-danger">
            <strong>❌ Faulty Threshold Ordering:</strong>
            <pre><code>temp = 28
if temp > 20:
    print("Warm")
elif temp > 25:
    print("Hot")   # Dead Code!
else:
    print("Cold")</code></pre>
          </div>
          <p><strong>Output:</strong> <code>Warm</code> (Even though 28 > 25!)</p>
          <p><strong>Rule:</strong> In an <code>if / elif / else</code> chain, Python stops at the <strong>first condition that evaluates to True</strong>. Because any number greater than 25 is also greater than 20, the second condition can NEVER be reached! Always test the most restrictive condition first (check > 25 first, then > 20).</p>
        </div>
      </div>

      <!-- Trap 7 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 7: Strings are IMMUTABLE</span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <div class="callout callout-danger">
            <strong>❌ Attempting Item Assignment:</strong>
            <pre><code>s = "hello"
s[0] = "H"  # Crashes! TypeError: 'str' object does not support item assignment</code></pre>
          </div>
          <p>Strings cannot be changed in place! You must construct a new string using concatenation or slicing:</p>
          <pre><code>s = "H" + s[1:]   # "Hello"</code></pre>
          <p>Also remember: <code>s.upper()</code> does NOT modify <code>s</code>! It returns a new string. You must write <code>s = s.upper()</code>.</p>
        </div>
      </div>

      <!-- Trap 8 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 8: Modifying a List WHILE Iterating Over It</span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <div class="callout callout-danger">
            <strong>❌ Deadly Loop Bug:</strong>
            <pre><code>nums = [-1, -2, 3, 4]
for x in nums:
    if x < 0:
        nums.remove(x)
print(nums)  # What prints?</code></pre>
          </div>
          <p><strong>Surprise Output:</strong> <code>[-2, 3, 4]</code> — <code>-2</code> was NOT removed!</p>
          <p><strong>Why:</strong> When <code>-1</code> at index 0 is removed, all subsequent elements shift left by one position. <code>-2</code> moves to index 0. The loop advances its internal index pointer to index 1 (which now holds <code>3</code>), completely skipping <code>-2</code>!</p>
          <p><strong>Fix:</strong> Iterate over a copy <code>for x in nums[:]:</code> or build a filtered list: <code>nums = [x for x in nums if x >= 0]</code>.</p>
        </div>
      </div>

      <!-- Trap 9 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 9: Slicing Direction Mismatch = Empty String / List</span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <p><strong>Question:</strong> What do these output?</p>
          <pre><code>s = "PYTHON"
print(s[0:6:-1])
print(s[-1:-7:1])</code></pre>
          <p><strong>Result:</strong> Both print empty strings <code>""</code>!</p>
          <p><strong>Reason:</strong> If the step is negative (<code>-1</code>), Python moves from right to left (decreasing indices). You cannot start at 0 and go backwards to reach 6! Similarly, if step is <code>+1</code>, you cannot start at index -1 (the end) and move forward to reach -7 (the front).</p>
        </div>
      </div>

      <!-- Trap 10 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 10: Initializing Max to <code>0</code> with Negative Numbers</span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <div class="callout callout-danger">
            <strong>❌ Faulty Max Initialization:</strong>
            <pre><code>nums = [-10, -5, -20, -2]
largest = 0  # BUG!
for n in nums:
    if n > largest:
        largest = n
print(largest)  # Prints 0! But 0 wasn't even in the list!</code></pre>
          </div>
          <p><strong>Fix:</strong> Always initialize <code>largest = nums[0]</code> or read the first user input before the loop: <code>largest = int(input())</code>.</p>
        </div>
      </div>

      <!-- Trap 11 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 11: <code>range(len(a))</code> vs <code>range(len(a) - 1)</code> for Neighbors</span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <div class="callout callout-danger">
            <strong>❌ Index Out of Range:</strong>
            <pre><code>for i in range(len(nums)):
    if nums[i] > nums[i + 1]:  # Crashes on the last iteration!
        return False</code></pre>
          </div>
          <p><strong>Fix:</strong> When inspecting adjacent pairs <code>nums[i]</code> and <code>nums[i + 1]</code>, the loop MUST stop at <code>range(len(nums) - 1)</code>. Otherwise, when <code>i = len(nums) - 1</code>, <code>nums[i + 1]</code> causes an <code>IndexError: list index out of range</code>.</p>
        </div>
      </div>

      <!-- Trap 12 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 12: Short-Circuit Evaluation Guard</span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <p><strong>Code:</strong></p>
          <pre><code>x = 5
if x > 2 or x / 0 > 1:
    print("Safe!")</code></pre>
          <p><strong>Does it crash?</strong> NO! It prints <code>Safe!</code>.</p>
          <p><strong>Explanation:</strong> In an <code>or</code> expression, if the left operand is <code>True</code>, the entire expression is already known to be True. Python does NOT evaluate the right side. Thus <code>x / 0</code> is never computed. Similarly, in <code>and</code>, if the left side is <code>False</code>, the right side is skipped.</p>
        </div>
      </div>

      <!-- Trap 13 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 13: <code>if x == 1 or 2:</code> — Truthiness Trap</span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <p><strong>Code:</strong></p>
          <pre><code>x = 5
if x == 1 or 2:
    print("Match!")</code></pre>
          <p><strong>Output:</strong> Prints <code>Match!</code> even though <code>x = 5</code>!</p>
          <p><strong>Why:</strong> Python parses this as <code>(x == 1) or (2)</code>. <code>x == 1</code> is False, but <code>2</code> is a non-zero number, which is truthy! The condition always evaluates to True. You must write: <code>if x == 1 or x == 2:</code> or <code>if x in [1, 2]:</code>.</p>
        </div>
      </div>

      <!-- Trap 14 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 14: <code>random.randint(a, b)</code> is INCLUSIVE</span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <p>Unlike <code>range(a, b)</code> which excludes <code>b</code>, <strong><code>random.randint(a, b)</code> includes BOTH <code>a</code> and <code>b</code></strong>!</p>
          <p>Example: <code>random.randint(1, 6)</code> can return 1, 2, 3, 4, 5, or 6 (e.g. dice roll). If you need 100 random values between 0 and 1000, <code>random.randint(0, 1000)</code> includes both 0 and 1000.</p>
        </div>
      </div>

      <!-- Trap 15 -->
      <div class="accordion">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>Trap 15: Premature <code>return</code> in Search Loops</span>
          <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-body">
          <div class="callout callout-danger">
            <strong>❌ Deciding after the first element:</strong>
            <pre><code>def is_prime(n):
    for d in range(2, n):
        if n % d == 0:
            return False
        else:
            return True   # FATAL BUG! Returns on d = 2!</code></pre>
          </div>
          <p><strong>Why this fails:</strong> For <code>n = 9</code>, when <code>d = 2</code>, <code>9 % 2 != 0</code>, so it enters the <code>else</code> branch and immediately returns <code>True</code>! But 9 is divisible by 3 and is NOT prime!</p>
          <p><strong>Rule:</strong> You can only conclude a property is True <strong>AFTER the loop finishes completely</strong> without finding any counter-example:</p>
          <pre><code>def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True   # Placed OUTSIDE the loop!</code></pre>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- DETAILED THEORY: WEEK 1 TO WEEK 6 -->
    <!-- ========================================================================= -->

    <!-- WEEK 1 -->
    <section id="week1">
      <div class="section-header">
        <div class="section-num">1</div>
        <h2>Week 1: Introduction to Python, Variables & Expressions</h2>
      </div>

      <div class="card">
        <h3>1. Programming Languages Hierarchy</h3>
        <p>Computers only execute electrical switches (bits). To bridge human thinking and hardware, languages are categorized into 4 tiers:</p>
        <table class="custom-table">
          <tr><th>Level</th><th>Name</th><th>Characteristics & Examples</th></tr>
          <tr><td>1</td><td>Natural Language</td><td>English, Arabic. Ambiguous ("I saw the man with the telescope"), cannot be executed directly by CPU.</td></tr>
          <tr><td>2</td><td>High-Level Language</td><td>Python, C++, Java. Human readable, portable across operating systems, hides memory/hardware details.</td></tr>
          <tr><td>3</td><td>Low-Level / Assembly</td><td>e.g., <code>MOV AL, 61h</code>. Close to hardware, CPU architecture dependent, high control but verbose.</td></tr>
          <tr><td>4</td><td>Machine Code</td><td>Binary strings of <code>0</code>s and <code>1</code>s (e.g. <code>10110000 01100001</code>). Executed directly by the ALU/CPU.</td></tr>
        </table>
      </div>

      <div class="card">
        <h3>2. Compilers vs Interpreters & How Python Runs</h3>
        <div class="grid-2">
          <div>
            <h4 style="color: #38bdf8; margin-bottom: 6px;">Compiler (e.g. C, C++)</h4>
            <p>Translates the entire program into an independent binary executable (<code>.exe</code>) <em>before</em> running. If there is a syntax error anywhere, no code runs.</p>
          </div>
          <div>
            <h4 style="color: #818cf8; margin-bottom: 6px;">Interpreter (e.g. Bash)</h4>
            <p>Translates and executes instructions line by line on the fly without producing a separate machine executable file.</p>
          </div>
        </div>
        <div class="callout callout-info" style="margin-top: 14px;">
          <strong>How Python Runs (Hybrid Model):</strong><br>
          Python combines both! Your source file (<code>.py</code>) is first automatically compiled into an intermediate form called <strong>Bytecode</strong> (<code>.pyc</code>). The <strong>Python Virtual Machine (PVM / Interpreter)</strong> then executes the bytecode instructions one by one.
        </div>
      </div>

      <div class="card">
        <h3>3. The Three Kinds of Errors</h3>
        <table class="custom-table">
          <tr><th>Error Type</th><th>Definition</th><th>Exam Example</th><th>Who Catches It?</th></tr>
          <tr>
            <td><strong>Syntax Error</strong></td>
            <td>Violates Python grammar rules. Program refuses to start running at all.</td>
            <td><code>1 + 2 *</code><br><code>if x = 5:</code></td>
            <td>Python compiler before running</td>
          </tr>
          <tr>
            <td><strong>Semantic / Runtime Error</strong></td>
            <td>Grammar is valid, but the operation is impossible at execution time (crashes).</td>
            <td><code>10 / 0</code> (ZeroDivisionError)<br><code>"Age: " + 20</code> (TypeError)</td>
            <td>Python interpreter while running</td>
          </tr>
          <tr>
            <td><strong>Logic Error</strong></td>
            <td>Program runs and completes without crashing, but produces the wrong answer!</td>
            <td>Average formula: <code>avg = a + b / 2</code> (Divides only <code>b</code> by 2 due to precedence!)</td>
            <td>Only the programmer through thorough testing!</td>
          </tr>
        </table>
      </div>

      <div class="card">
        <h3>4. Operators, Precedence & Classic Modulus/Division Tricks</h3>
        <p>Operator Precedence: <strong>PEMDAS</strong> (Parentheses <code>()</code> &rarr; Exponent <code>**</code> &rarr; Multiplicative <code>* / // %</code> &rarr; Additive <code>+ -</code>).</p>
        <div class="callout callout-tip">
          <strong>The Two Master Algorithms for Week 1:</strong>
          <pre><code># Algorithm A: Extracting and stripping digits of an integer
n = 1234
last_digit = n % 10          # 4
without_last = n // 10       # 123
tens_digit = (n // 10) % 10  # 3

# Algorithm B: Splitting total seconds into h:m:s
total_seconds = 7384
hours = total_seconds // 3600             # 2 hours
remainder = total_seconds % 3600          # 184 seconds left
minutes = remainder // 60                 # 3 minutes
seconds = remainder % 60                  # 4 seconds</code></pre>
        </div>
      </div>
    </section>

    <!-- WEEK 2 -->
    <section id="week2">
      <div class="section-header">
        <div class="section-num">2</div>
        <h2>Week 2: Conditionals & Functions (Part 1)</h2>
      </div>

      <div class="card">
        <h3>1. Boolean Expressions & Logical Operators</h3>
        <p>Comparison operators: <code>==</code>, <code>!=</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&lt;=</code>, <code>&gt;=</code>. Note: <code>=</code> is assignment, <code>==</code> is comparison.</p>
        <p>Logical Precedence: <code>not</code> has highest precedence, then <code>and</code>, then <code>or</code>.</p>
        <pre><code># Evaluation Example:
not False and True or False
# Step 1: not False -> True
# Step 2: True and True -> True
# Step 3: True or False -> True</code></pre>
      </div>

      <div class="card">
        <h3>2. Structure of Conditionals</h3>
        <div class="grid-2">
          <div>
            <h4 style="color: #38bdf8;">Chained: <code>if / elif / else</code></h4>
            <p><strong>Mutually exclusive:</strong> At most ONE branch runs. Once a condition is True, all subsequent branches are skipped.</p>
          </div>
          <div>
            <h4 style="color: #818cf8;">Separate: Multiple <code>if</code> statements</h4>
            <p><strong>Independent checks:</strong> Every single <code>if</code> is evaluated. Multiple blocks can execute.</p>
          </div>
        </div>
      </div>

      <div class="card">
        <h3>3. Finding the Maximum of Three Numbers: 3 Approaches</h3>
        <pre><code># Approach 1: Compound Conditions
if a >= b and a >= c:
    m = a
elif b >= a and b >= c:
    m = b
else:
    m = c

# Approach 2: Running Maximum (Most elegant and expandable)
m = a
if b > m:
    m = b
if c > m:
    m = c

# Approach 3: Nested ifs
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
        <h3>4. Functions, Parameters vs Arguments & Leap Year Predicate</h3>
        <p><strong>Definition vs Calling:</strong> <code>def f(x):</code> defines parameters. <code>f(5)</code> supplies arguments. Defining a function never runs it!</p>
        <p><strong>Leap Year Rule:</strong> A year is a leap year if divisible by 4, EXCEPT century years (divisible by 100), which must be divisible by 400.</p>
        <pre><code>def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# One-liner version:
def is_leap_year_compact(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)</code></pre>
      </div>
    </section>

    <!-- WEEK 3 -->
    <section id="week3">
      <div class="section-header">
        <div class="section-num">3</div>
        <h2>Week 3: Functions (Part 2), Scope & Loops</h2>
      </div>

      <div class="card">
        <h3>1. Call Frames, Call Stack & Scope</h3>
        <ul>
          <li><strong>Activation Record (Frame):</strong> Whenever a function is invoked, Python allocates a new stack frame holding its parameters and local variables.</li>
          <li><strong>Frame Destruction:</strong> When <code>return</code> executes, the frame is destroyed and local variables vanish from memory.</li>
          <li><strong>Variable Shadowing:</strong> If a local variable inside a function shares the same name as a global variable, the local variable shadows (hides) the global variable within the function body without altering the global variable.</li>
        </ul>
      </div>

      <div class="card">
        <h3>2. <code>for</code> Loops & <code>range()</code> Variations</h3>
        <table class="custom-table">
          <tr><th>Form</th><th>Range Call</th><th>Values Generated</th><th>Notes</th></tr>
          <tr><td>1 Argument</td><td><code>range(5)</code></td><td><code>0, 1, 2, 3, 4</code></td><td>Starts at 0, stops before 5</td></tr>
          <tr><td>2 Arguments</td><td><code>range(2, 6)</code></td><td><code>2, 3, 4, 5</code></td><td>Starts at 2, stops before 6</td></tr>
          <tr><td>3 Arguments</td><td><code>range(1, 10, 2)</code></td><td><code>1, 3, 5, 7, 9</code></td><td>Steps by 2</td></tr>
          <tr><td>Negative Step</td><td><code>range(5, 0, -1)</code></td><td><code>5, 4, 3, 2, 1</code></td><td>Counts down; stops before 0!</td></tr>
        </table>
      </div>

      <div class="card">
        <h3>3. Essential Loop Patterns</h3>
        <pre><code># Pattern 1: Accumulator (Sum & Factorial)
total = 0                 # Neutral value for + is 0
for i in range(1, n + 1):
    total += i

fact = 1                  # Neutral value for * is 1
for i in range(1, n + 1):
    fact *= i

# Pattern 2: While loop with Sentinel (-1 to stop)
count = 0
total = 0
val = int(input("Enter score (-1 to stop): ")) # Read BEFORE loop
while val != -1:
    total += val
    count += 1
    val = int(input("Enter score (-1 to stop): ")) # Read at BOTTOM of body

# Pattern 3: Right-aligned Triangle
n = 4
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)</code></pre>
      </div>
    </section>

    <!-- WEEK 4 -->
    <section id="week4">
      <div class="section-header">
        <div class="section-num">4</div>
        <h2>Week 4: Nested Loops & Code Reading / Tracing</h2>
      </div>

      <div class="card">
        <h3>1. Mechanics of Nested Loops</h3>
        <p>For every <strong>single iteration</strong> of the outer loop, the inner loop executes from start to finish. If outer runs $R$ times and inner runs $C$ times, the inner loop body runs $R \times C$ times.</p>
        <p><strong>Nesting multiplies work, sequential loops add work:</strong></p>
        <pre><code># Nested: 1,000 * 1,000 = 1,000,000 executions
for i in range(1000):
    for j in range(1000):
        print(j)

# Sequential: 1,000 + 1,000 = 2,000 executions
for i in range(1000):
    print(i)
for j in range(1000):
    print(j)</code></pre>
      </div>

      <div class="card">
        <h3>2. Prime Number Algorithms: Flag vs Counter</h3>
        <div class="grid-2">
          <div>
            <h4 style="color: #38bdf8;">Approach A: Boolean Flag (Fast, with break)</h4>
            <pre><code>def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False  # Early exit!
    return True</code></pre>
          </div>
          <div>
            <h4 style="color: #818cf8;">Approach B: Divisor Counter (Exhaustive)</h4>
            <pre><code>def is_prime(n):
    if n < 2:
        return False
    count = 0
    for d in range(1, n + 1):
        if n % d == 0:
            count += 1
    return count == 2</code></pre>
          </div>
        </div>
      </div>

      <div class="card">
        <h3>3. 2D Coordinate Grids & Diagonals</h3>
        <pre><code># Main Diagonal: row == col (i == j)
# Anti-Diagonal: row + col == n - 1 (i + j == n - 1)
n = 4
for i in range(n):
    for j in range(n):
        if i == j:
            print("X", end="")
        else:
            print("-", end="")
    print()

# Output:
# X---
# -X--
# --X-
# ---X</code></pre>
      </div>

      <div class="card">
        <h3>4. Tracing Mystery Functions with Trace Tables</h3>
        <p><strong>Slide Mystery Example: Second Largest</strong></p>
        <pre><code>def mystery(count):
    largest = int(input("Number: "))
    second = None
    for _ in range(count - 1):
        n = int(input("Number: "))
        if n > largest:
            second = largest
            largest = n
        elif second is None or n > second:
            second = n
    return second</code></pre>
        <table class="custom-table">
          <tr><th>Iteration</th><th>Input <code>n</code></th><th>Condition Met</th><th><code>largest</code></th><th><code>second</code></th></tr>
          <tr><td>Start</td><td>5</td><td>—</td><td>5</td><td><code>None</code></td></tr>
          <tr><td>1</td><td>9</td><td><code>n > largest</code> (9 > 5)</td><td>9</td><td>5</td></tr>
          <tr><td>2</td><td>3</td><td>None (3 < 5)</td><td>9</td><td>5</td></tr>
          <tr><td>3</td><td>7</td><td><code>n > second</code> (7 > 5)</td><td>9</td><td>7</td></tr>
        </table>
        <p><strong>Final Return:</strong> <code>7</code> (The second largest value).</p>
      </div>
    </section>

    <!-- WEEK 5 -->
    <section id="week5">
      <div class="section-header">
        <div class="section-num">5</div>
        <h2>Week 5: Strings & Sequences (Basics of Lists)</h2>
      </div>

      <div class="card">
        <h3>1. Sequence Indexing & The Complete Slicing Rules</h3>
        <p>For string <code>s = "PYTHON"</code> (Length = 6):</p>
        <table class="custom-table">
          <tr><th>Char</th><th>P</th><th>Y</th><th>T</th><th>H</th><th>O</th><th>N</th></tr>
          <tr><th>Positive Index</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr>
          <tr><th>Negative Index</th><td>-6</td><td>-5</td><td>-4</td><td>-3</td><td>-2</td><td>-1</td></tr>
        </table>
        <div class="callout callout-tip">
          <strong>Master Slicing Summary: <code>s[start:stop:step]</code></strong>
          <ul>
            <li><code>start</code> is <strong>included</strong>; <code>stop</code> is <strong>excluded</strong>.</li>
            <li>Default step is <code>1</code> (left-to-right).</li>
            <li>If step is positive: default start is <code>0</code>, default stop is <code>len(s)</code>.</li>
            <li>If step is negative: default start is <code>-1</code> (end of string), default stop is before the beginning (index -1 in concept).</li>
            <li><code>s[::-1]</code> reverses the sequence completely.</li>
            <li>Slices <strong>never throw an IndexError</strong>! <code>s[0:100]</code> smoothly clips at string boundary.</li>
          </ul>
        </div>
      </div>

      <div class="card">
        <h3>2. String Methods Cheat Sheet</h3>
        <table class="custom-table">
          <tr><th>Method</th><th>Example</th><th>Output</th><th>Key Note</th></tr>
          <tr><td><code>.upper() / .lower()</code></td><td><code>"Hi".upper()</code></td><td><code>'HI'</code></td><td>Returns a new string; doesn't mutate</td></tr>
          <tr><td><code>.strip()</code></td><td><code>"  cat  ".strip()</code></td><td><code>'cat'</code></td><td>Removes leading and trailing whitespace</td></tr>
          <tr><td><code>.find(sub)</code></td><td><code>"banana".find("na")</code></td><td><code>2</code></td><td>Index of <strong>first</strong> occurrence; returns <strong>-1</strong> if not found</td></tr>
          <tr><td><code>.count(sub)</code></td><td><code>"banana".count("a")</code></td><td><code>3</code></td><td>Counts non-overlapping occurrences</td></tr>
          <tr><td><code>.replace(old, new)</code></td><td><code>"banana".replace("a", "o")</code></td><td><code>'bonono'</code></td><td>Replaces all occurrences</td></tr>
          <tr><td><code>.split(sep)</code></td><td><code>"a,b,c".split(",")</code></td><td><code>['a', 'b', 'c']</code></td><td>Splits into a list of strings</td></tr>
          <tr><td><code>sep.join(list)</code></td><td><code>"-".join(['a', 'b'])</code></td><td><code>'a-b'</code></td><td>Joins list of strings by delimiter</td></tr>
          <tr><td><code>in / not in</code></td><td><code>"na" in "banana"</code></td><td><code>True</code></td><td>Boolean substring membership check</td></tr>
        </table>
      </div>

      <div class="card">
        <h3>3. Palindromes & Email Parsing Case Studies</h3>
        <pre><code># Case Study 1: Palindrome Check (Two Pointers vs Slicing)
def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

# Case Study 2: Parsing Jordanian Emails (.jo)
email = "sara@psut.edu.jo".lower()
pos_at = email.find('@')
if pos_at > 0:
    domain = email[pos_at + 1:]
    pos_dot = domain.find('.jo')
    if pos_dot > 0:
        print("Valid domain:", domain[:pos_dot])  # psut.edu</code></pre>
      </div>

      <div class="card">
        <h3>4. Introduction to Lists: Mutability & Methods</h3>
        <p>Lists are <strong>ordered, mutable</strong> collections written with square brackets <code>[1, 2, 3]</code>.</p>
        <table class="custom-table">
          <tr><th>Operation</th><th>Code (<code>a = [3, 1, 2]</code>)</th><th>Result</th><th>Mutates <code>a</code>?</th></tr>
          <tr><td>Append</td><td><code>a.append(5)</code></td><td><code>[3, 1, 2, 5]</code></td><td>Yes</td></tr>
          <tr><td>Insert</td><td><code>a.insert(0, 99)</code></td><td><code>[99, 3, 1, 2]</code></td><td>Yes</td></tr>
          <tr><td>Remove</td><td><code>a.remove(1)</code></td><td><code>[3, 2]</code> (removes first occurrence)</td><td>Yes</td></tr>
          <tr><td>Pop</td><td><code>x = a.pop()</code></td><td>Returns <code>2</code>, <code>a</code> is <code>[3, 1]</code></td><td>Yes</td></tr>
          <tr><td>Sort In-Place</td><td><code>a.sort()</code></td><td>Returns <code>None</code>, <code>a</code> is <code>[1, 2, 3]</code></td><td>Yes</td></tr>
          <tr><td>Sorted Copy</td><td><code>b = sorted(a)</code></td><td>Returns new list <code>[1, 2, 3]</code></td><td>No (<code>a</code> unchanged)</td></tr>
        </table>
      </div>
    </section>

    <!-- WEEK 6 -->
    <section id="week6">
      <div class="section-header">
        <div class="section-num">6</div>
        <h2>Week 6: Lists in Practice & Advanced Algorithms</h2>
      </div>

      <div class="card">
        <h3>1. Generating Unique Random Numbers</h3>
        <p>Why use a <code>while</code> loop instead of <code>for _ in range(100)</code>? Because duplicate random numbers might be drawn and skipped! We keep generating until the list length hits 100.</p>
        <pre><code>import random
nums = []
while len(nums) < 100:
    r = random.randint(0, 1000)
    if r not in nums:  # Skip duplicates
        nums.append(r)
nums.sort()</code></pre>
      </div>

      <div class="card">
        <h3>2. List Equivalence & Sublist Sliding Window</h3>
        <pre><code># Are two lists equivalent (same elements, frequency/order ignored)?
def is_equivalent(a, b):
    for x in a:
        if x not in b:
            return False
    for x in b:
        if x not in a:
            return False
    return True

# Sliding Window Sublist Check: Does 'a' appear consecutively in 'b'?
def is_sublist(a, b):
    n = len(a)
    for i in range(len(b) - n + 1):  # Number of possible window starts
        if b[i:i + n] == a:
            return True
    return False</code></pre>
      </div>

      <div class="card">
        <h3>3. Frequency Counter List (Histograms)</h3>
        <p>Using list values as indices to count occurrences without a dictionary:</p>
        <pre><code># Assume nums only contains integers 0, 1, 2
counts = [0] * 3
for n in [0, 1, 1, 2, 1]:
    counts[n] += 1
# counts[0] = 1, counts[1] = 3, counts[2] = 1 -> [1, 3, 1]

# Dice roll simulation (faces 1 to 6):
dice_counts = [0] * 7  # indices 0..6
# If roll is 4: dice_counts[4] += 1</code></pre>
      </div>

      <div class="card">
        <h3>4. In-Place Reversal & Aliasing vs Slicing</h3>
        <p>To reverse a list in-place inside a function so the caller's list updates:</p>
        <pre><code># Option A: Two Pointers Swap
def reverse_in_place(a):
    i = 0
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

# Option B: Slice Assignment
def reverse_in_place_slice(a):
    a[:] = a[::-1]  # Overwrites caller's list memory

# ⚠️ FATAL TRAP:
def buggy_reverse(a):
    a = a[::-1]  # Rebinds local variable 'a' only! Caller's list NOT modified!</code></pre>
      </div>

      <div class="card">
        <h3>5. Debugging Search & Unequal List Merging</h3>
        <div class="grid-2">
          <div>
            <h4 style="color: #38bdf8;">Linear Search (Fixing UnboundLocalError)</h4>
            <pre><code>def find_index(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i   # Exit immediately
    return -1          # Not found</code></pre>
          </div>
          <div>
            <h4 style="color: #818cf8;">Merging Unequal Lists Safely</h4>
            <pre><code>def merge_lists(a, b):
    merged = []
    n = min(len(a), len(b))
    for i in range(n):
        merged.append(a[i])
        merged.append(b[i])
    # Append leftover elements from longer list
    merged += a[n:] + b[n:]
    return merged</code></pre>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 25 INTERACTIVE FLASHCARDS -->
    <!-- ========================================================================= -->
    <section id="flashcards">
      <div class="section-header">
        <div class="section-num">🃏</div>
        <h2>25 Active Recall Exam Flashcards</h2>
      </div>
      <p class="section-desc">Click any card to flip it. Review these right before the exam to drill the most commonly tested rules into memory.</p>

      <div class="flashcards-container" id="cardsDeck">
        <!-- Populated by JS -->
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 25-QUESTION MOCK EXAM -->
    <!-- ========================================================================= -->
    <section id="mock-exam">
      <div class="section-header">
        <div class="section-num">📝</div>
        <h2>Midterm Mock Exam (25 Questions)</h2>
      </div>
      <p class="section-desc">Test your real exam readiness with instant feedback and complete step-by-step explanations for every question.</p>

      <div class="quiz-progress-bar">
        <div class="quiz-progress-fill" id="quizProgress"></div>
      </div>

      <div class="score-banner" id="scoreBanner">
        <h3 style="font-size: 1.4rem; color: #f8fafc; margin-bottom: 6px;">Current Score: <span id="userScore" style="color:#38bdf8;">0</span> / 25</h3>
        <p style="font-size: 0.88rem; color: #94a3b8;" id="scoreComment">Answer the questions below to test your knowledge.</p>
      
        <button onclick="resetQuiz()" style="margin-top:12px; background:rgba(56, 189, 248, 0.1); color:#38bdf8; border:1px solid rgba(56, 189, 248, 0.3); padding:8px 16px; border-radius:8px; font-weight:600; cursor:pointer; font-size:0.88rem; transition:all 0.2s;">🔄 Reset / Retake Mock Exam</button></div>

      <div id="quizContainer">
        <!-- Populated by JS -->
      </div>
    </section>

  </main>

  <script>
    // --- Mobile Sidebar Toggle ---
    function toggleSidebar() {
      document.getElementById('sidebar').classList.toggle('open');
    }

    // --- Accordion Logic ---
    function toggleAccordion(header) {
      const parent = header.parentElement;
      parent.classList.toggle('open');
    }

    // --- Interactive Slicing Visualizer ---
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

      // Step verification
      let step = stepVal === '' ? 1 : parseInt(stepVal);
      if (isNaN(step)) step = 1;

      if (step === 0) {
        document.getElementById('sliceVal').textContent = 'ValueError: slice step cannot be zero';
        document.getElementById('sliceVal').style.color = '#fb7185';
        document.getElementById('sliceLen').textContent = 0;
        document.getElementById('sliceExplanation').innerHTML = '<span style="color:#fb7185; font-weight:600;">⚠️ Python ValueError:</span> Slice step cannot be zero (<code>text[' + (startVal||'') + ':' + (stopVal||'') + ':0]</code> crashes in Python).';
        return;
      } else {
        document.getElementById('sliceVal').style.color = '';
      }

      let start, stop;
      if (step > 0) {
        if (startVal === '') {
          start = 0;
        } else {
          start = parseInt(startVal);
          if (isNaN(start)) start = 0;
          else if (start < 0) {
            start = n + start;
            if (start < 0) start = 0;
          } else if (start > n) {
            start = n;
          }
        }

        if (stopVal === '') {
          stop = n;
        } else {
          stop = parseInt(stopVal);
          if (isNaN(stop)) stop = n;
          else if (stop < 0) {
            stop = n + stop;
            if (stop < 0) stop = 0;
          } else if (stop > n) {
            stop = n;
          }
        }
      } else {
        // step < 0
        if (startVal === '') {
          start = n - 1;
        } else {
          start = parseInt(startVal);
          if (isNaN(start)) start = n - 1;
          else if (start < 0) {
            start = n + start;
            if (start < -1) start = -1;
          } else if (start >= n) {
            start = n - 1;
          }
        }

        if (stopVal === '') {
          stop = -1;
        } else {
          stop = parseInt(stopVal);
          if (isNaN(stop)) stop = -1;
          else if (stop < 0) {
            stop = n + stop;
            if (stop < -1) stop = -1;
          } else if (stop >= n) {
            stop = n - 1;
          }
        }
      }

      let resultChars = [];
      let selectedIndices = [];

      if (step > 0) {
        for (let i = start; i < stop; i += step) {
          resultChars.push(text[i]);
          selectedIndices.push(i);
        }
      } else {
        for (let i = start; i > stop; i += step) {
          resultChars.push(text[i]);
          selectedIndices.push(i);
        }
      }

      selectedIndices.forEach(idx => {
        const box = document.getElementById(`char-box-${idx}`);
        if (box) box.classList.add('selected');
      });

      const resStr = resultChars.join('');
      document.getElementById('sliceVal').textContent = `'${resStr}'`;
      document.getElementById('sliceLen').textContent = resStr.length;

      let exp = `Slice representation: text[${startVal === '' ? '' : startVal}:${stopVal === '' ? '' : stopVal}:${stepVal === '' ? '' : stepVal}] &rarr; Selected ${selectedIndices.length} character(s).`;
      if (resStr.length === 0) {
        exp += ` (Warning: Slice yielded empty string due to step direction or out-of-range bounds)`;
      }
      document.getElementById('sliceExplanation').innerHTML = exp;
    }

    // --- Flashcards Data ---
    const flashcardsData = [
      { q: "What does 17 // 5 and -17 // 5 evaluate to?", a: "17 // 5 = 3\n-17 // 5 = -4 (Floor division always rounds DOWN toward negative infinity)" },
      { q: "What is the associativity of 2 ** 3 ** 2?", a: "Right-to-left! Evaluates as 2 ** (3 ** 2) = 2 ** 9 = 512, NOT 64." },
      { q: "What does a = a.sort() do to list a?", a: "It sets a = None! sort() works in-place and returns None. Use a.sort() alone or b = sorted(a)." },
      { q: "What is the difference between print() and return?", a: "print() only displays text on screen. return sends a value back to caller and ends the function. Functions without return yield None." },
      { q: "Why is s[0] = 'H' an error for string s?", a: "Strings are IMMUTABLE in Python. You cannot modify them in place; you must build a new string: 'H' + s[1:]." },
      { q: "What does s[0:6:-1] evaluate to for 'PYTHON'?", a: "Empty string ''! You cannot start at 0 and go backwards (-1 step) to reach 6." },
      { q: "Is random.randint(1, 6) inclusive or exclusive?", a: "INCLUSIVE of both endpoints! It can generate 1, 2, 3, 4, 5, or 6." },
      { q: "In an if / elif / else chain, how many branches run?", a: "At most ONE. Python executes the first True condition and skips the rest." },
      { q: "What does s.find('xyz') return if 'xyz' is not found?", a: "Returns -1 (it does NOT crash or raise an error)." },
      { q: "What happens when you delete elements in a list while looping over it?", a: "It shifts subsequent elements left and skips elements! Always iterate over a copy or build a new list." },
      { q: "Why initialize max with nums[0] instead of 0?", a: "If all numbers in nums are negative (e.g. [-5, -2]), 0 would wrongly win even though it was never in the list." },
      { q: "What is short-circuit evaluation?", a: "Python stops evaluating logical expressions as soon as the result is certain: 'True or X' skips X, 'False and X' skips X." },
      { q: "What is the difference between a Compiler and an Interpreter?", a: "Compiler translates the whole program before running. Interpreter translates and runs line-by-line. Python compiles to bytecode then interprets." },
      { q: "What is a Logic Error?", a: "Program runs without crashing but gives the wrong result due to flawed reasoning (e.g. a + b / 2)." },
      { q: "What does range(5, 0, -1) generate?", a: "5, 4, 3, 2, 1 (Stops before 0!)." },
      { q: "How many times does the inner body run in: for i in range(5): for j in range(i): ?", a: "0 + 1 + 2 + 3 + 4 = 10 times." },
      { q: "What is variable shadowing?", a: "When a local variable inside a function shares the same name as a global variable, hiding the global variable within the function." },
      { q: "How to check if two lists contain the same elements ignoring order & frequency?", a: "Check every x in a is in b AND every x in b is in a (2-way membership test)." },
      { q: "What range should you use when comparing neighbors a[i] and a[i+1]?", a: "range(len(a) - 1) to avoid an IndexError on the last element." },
      { q: "What does 'banana'.replace('a', 'o') return and does it modify 'banana'?", a: "Returns 'bonono'. The original string 'banana' remains completely unchanged." },
      { q: "What does c = [0] * 3 create?", a: "[0, 0, 0] — a list of 3 zeros, commonly used as a frequency counter histogram." },
      { q: "What is the leap year rule?", a: "Divisible by 4, except century years (divisible by 100), which must be divisible by 400." },
      { q: "How to reverse list 'nums' in-place without using .reverse()?", a: "nums[:] = nums[::-1] (Slice assignment alters caller's list)." },
      { q: "What error occurs when accessing an index >= len(s)?", a: "IndexError: string index out of range (Note: slices never raise IndexError)." },
      { q: "What does str.split() with no arguments split by?", a: "Any whitespace (spaces, tabs, newlines) and removes empty strings." }
    ];

    function renderFlashcards() {
      const container = document.getElementById('cardsDeck');
      container.innerHTML = '';
      flashcardsData.forEach((card, idx) => {
        const el = document.createElement('div');
        el.className = 'flashcard';
        el.onclick = () => el.classList.toggle('flipped');
        el.innerHTML = `
          <div class="flashcard-inner">
            <div class="flashcard-front">
              <h4>Card #${idx + 1}</h4>
              <p>${card.q}</p>
              <span style="font-size:0.75rem; color:#64748b; margin-top:12px;">(Click to reveal answer)</span>
            </div>
            <div class="flashcard-back">
              <strong style="color:#38bdf8; margin-bottom:8px; display:block;">Answer:</strong>
              <div style="white-space: pre-line;">${card.a}</div>
            </div>
          </div>
        `;
        container.appendChild(el);
      });
    }

    // --- 25-Question Mock Exam Data ---
    const quizData = [
      {
        q: "1. Which of the following errors is caught by the programmer through testing, rather than by Python?",
        opts: ["Syntax Error", "TypeError", "ZeroDivisionError", "Logic Error"],
        ans: 3,
        exp: "Logic errors produce syntactically valid code that runs without crashing, but yields an incorrect answer (e.g. avg = a + b / 2). Only careful testing catches them."
      },
      {
        q: "2. What is the output of: print(2 + 3 * 4 ** 2)?",
        opts: ["50", "400", "80", "146"],
        ans: 0,
        exp: "PEMDAS: 4 ** 2 = 16. Then 3 * 16 = 48. Then 2 + 48 = 50."
      },
      {
        q: "3. What is the exact value and type of 10 / 2 in Python?",
        opts: ["5 (int)", "5.0 (float)", "5.0 (int)", "5 (str)"],
        ans: 1,
        exp: "In Python 3, single slash / is true float division, so 10 / 2 produces 5.0 of type float."
      },
      {
        q: "4. What is the output of print(-17 // 5)?",
        opts: ["-3", "-3.4", "-4", "-3.0"],
        ans: 2,
        exp: "Floor division // rounds DOWN towards negative infinity. -17 / 5 = -3.4, so floored down is -4."
      },
      {
        q: "5. What is the output of: print(2 ** 3 ** 2)?",
        opts: ["64", "512", "36", "128"],
        ans: 1,
        exp: "Exponentiation is right-to-left: 3 ** 2 = 9, then 2 ** 9 = 512."
      },
      {
        q: "6. Consider: x = 5; if x > 2 or x / 0 > 1: print('OK'). What happens?",
        opts: ["Crashes with ZeroDivisionError", "Prints 'OK'", "Prints False", "SyntaxError"],
        ans: 1,
        exp: "Short-circuit evaluation: Since x > 2 is True, the 'or' operator does not evaluate the right operand (x / 0), avoiding any crash and printing 'OK'."
      },
      {
        q: "7. What does the following function return?\ndef mystery(a, b):\n    print(a + b)\nx = mystery(3, 4)",
        opts: ["7", "None", "0", "TypeError"],
        ans: 1,
        exp: "The function prints 7 to the console, but has no return statement. Therefore, x is assigned None."
      },
      {
        q: "8. What prints?\ntemp = 28\nif temp > 20:\n    print('Warm')\nelif temp > 25:\n    print('Hot')\nelse:\n    print('Cold')",
        opts: ["Warm", "Hot", "Warm and Hot", "Cold"],
        ans: 0,
        exp: "In an if/elif chain, only the first True condition executes. Since 28 > 20 is True, 'Warm' prints and the rest of the chain is skipped."
      },
      {
        q: "9. How many times will print('*') execute?\nfor i in range(1, 4):\n    for j in range(2):\n        print('*')",
        opts: ["5", "6", "8", "12"],
        ans: 1,
        exp: "Outer loop range(1, 4) runs 3 times (i = 1, 2, 3). Inner loop range(2) runs 2 times. Total prints = 3 * 2 = 6."
      },
      {
        q: "10. How many times does this loop run?\nfor i in range(5):\n    for j in range(i):\n        pass",
        opts: ["10", "15", "25", "20"],
        ans: 0,
        exp: "When i=0 (0 times), i=1 (1 time), i=2 (2 times), i=3 (3 times), i=4 (4 times). Total = 0 + 1 + 2 + 3 + 4 = 10."
      },
      {
        q: "11. What is the output of print('PYTHON'[4:1:-1])?",
        opts: ["'OHT'", "'YTHO'", "'NOTHY'", "'OHTY'"],
        ans: 0,
        exp: "Indices: P(0), Y(1), T(2), H(3), O(4), N(5). Starting at 4 ('O'), stepping -1 down to but excluding 1: indices 4, 3, 2 &rarr; 'O', 'H', 'T'."
      },
      {
        q: "12. What does 'PYTHON'[0:6:-1] evaluate to?",
        opts: ["'NOHTYP'", "'' (empty string)", "IndexError", "'PYTHON'"],
        ans: 1,
        exp: "With a negative step (-1), Python expects start > stop. You cannot start at 0 and decrease to reach 6, so it produces an empty string."
      },
      {
        q: "13. What is the result of 'banana'.find('na')?",
        opts: ["2", "4", "True", "3"],
        ans: 0,
        exp: "find() returns the index of the first occurrence. The first 'na' starts at index 2."
      },
      {
        q: "14. If s = 'hello', what happens when you execute s[0] = 'H'?",
        opts: ["s becomes 'Hello'", "TypeError", "IndexError", "ValueError"],
        ans: 1,
        exp: "Strings are immutable in Python. Modifying a character via item assignment raises TypeError."
      },
      {
        q: "15. What is the output of:\nnums = [1, 2, 3]\nnums = nums.sort()\nprint(nums)",
        opts: ["[1, 2, 3]", "None", "[3, 2, 1]", "AttributeError"],
        ans: 1,
        exp: "nums.sort() modifies the list in place and returns None. Assigning nums = nums.sort() destroys the list with None."
      },
      {
        q: "16. What is the output of print(list(range(5, 0, -1)))?",
        opts: ["[5, 4, 3, 2, 1, 0]", "[5, 4, 3, 2, 1]", "[4, 3, 2, 1, 0]", "[5, 4, 3, 2]"],
        ans: 1,
        exp: "range(start, stop, step) stops strictly before the stop value. Thus it stops before 0, producing [5, 4, 3, 2, 1]."
      },
      {
        q: "17. What will this code print?\ndef mystery(nums):\n    c = [0] * 3\n    for n in nums:\n        c[n] += 1\n    return c\nprint(mystery([0, 1, 1, 2, 1]))",
        opts: ["[1, 3, 1]", "[0, 1, 2]", "[3, 1, 1]", "IndexError"],
        ans: 0,
        exp: "This is a frequency counter. 0 appears once (c[0]=1), 1 appears 3 times (c[1]=3), and 2 appears once (c[2]=1). Output: [1, 3, 1]."
      },
      {
        q: "18. What does is_equivalent([1, 1, 2], [2, 1]) return under the slides definition?",
        opts: ["False", "True", "IndexError", "None"],
        ans: 1,
        exp: "Slide Week 6 Example 4: is_equivalent checks that every element of a is in b and vice versa. It ignores duplicates/frequency, so [1, 1, 2] and [2, 1] are equivalent (True)."
      },
      {
        q: "19. What is wrong with: for i in range(len(a)): if a[i] > a[i+1]: return False ?",
        opts: ["range should start at 1", "IndexError on the final iteration a[i+1]", "Syntax error in if", "Nothing, it's correct"],
        ans: 1,
        exp: "When i reaches len(a) - 1, a[i+1] attempts to access an index out of bounds, causing IndexError. The range must be range(len(a) - 1)."
      },
      {
        q: "20. What is the value of result after:\ns = 'Hello World 2025'\nresult = len(s.split())",
        opts: ["16", "3", "2", "4"],
        ans: 1,
        exp: "s.split() splits on whitespace into ['Hello', 'World', '2025']. The length of this list is 3."
      },
      {
        q: "21. What happens when random.randint(1, 6) is called?",
        opts: ["Returns 1 to 5 only", "Returns 1 to 6 inclusive", "Returns float between 1.0 and 6.0", "SyntaxError"],
        ans: 1,
        exp: "Unlike range(), random.randint(a, b) includes BOTH endpoints (1 and 6)."
      },
      {
        q: "22. In the slide code:\ndef mystery(a, b):\n    n = len(a)\n    for i in range(len(b) - n + 1):\n        if b[i:i+n] == a:\n            return True\n    return False\nWhat does this function do?",
        opts: ["Checks if a and b have the same length", "Checks if a is a contiguous sublist of b", "Reverses list b into a", "Sorts list a using b"],
        ans: 1,
        exp: "It slides a window of size len(a) across list b to check if sequence a appears consecutively within b (is_sublist)."
      },
      {
        q: "23. If nums = [-1, -2, 3] and we run: for x in nums: if x < 0: nums.remove(x). What is nums afterwards?",
        opts: ["[3]", "[-2, 3]", "[]", "[-1, 3]"],
        ans: 1,
        exp: "Deleting during iteration shifts elements left. When -1 is removed, -2 shifts into index 0 and is skipped on the next step. So -2 remains: [-2, 3]."
      },
      {
        q: "24. What does the expression [0] * 4 produce?",
        opts: ["0", "[0, 0, 0, 0]", "SyntaxError", "[0]"],
        ans: 1,
        exp: "List repetition with * repeats the elements inside the list, producing [0, 0, 0, 0]."
      },
      {
        q: "25. Which year is NOT a leap year according to the standard algorithm?",
        opts: ["2000", "2024", "1900", "2016"],
        ans: 2,
        exp: "Century years (like 1900) must be divisible by 400. 1900 % 400 != 0, so 1900 is NOT a leap year (unlike 2000)."
      }
    ];

    let userAnswers = {};

    function renderQuiz() {
      const container = document.getElementById('quizContainer');
      container.innerHTML = '';

      quizData.forEach((item, qIdx) => {
        const qCard = document.createElement('div');
        qCard.className = 'quiz-card';
        qCard.id = `q-card-${qIdx}`;

        let optsHtml = '';
        item.opts.forEach((opt, optIdx) => {
          optsHtml += `
            <div class="quiz-opt" id="opt-${qIdx}-${optIdx}" onclick="handleAnswer(${qIdx}, ${optIdx})">
              <span style="font-weight:700; width:22px;">${String.fromCharCode(65 + optIdx)})</span>
              <span>${opt}</span>
            </div>
          `;
        });

        qCard.innerHTML = `
          <div class="quiz-q">${item.q}</div>
          <div class="quiz-options">${optsHtml}</div>
          <div class="quiz-explanation" id="exp-${qIdx}">
            <strong>💡 Explanation:</strong> ${item.exp}
          </div>
        `;
        container.appendChild(qCard);
      });
    }

    function handleAnswer(qIdx, optIdx) {
      if (userAnswers[qIdx] !== undefined) return; // Prevent changing after answered
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
      const answeredCount = Object.keys(userAnswers).length;
      let score = 0;
      Object.keys(userAnswers).forEach(qIdx => {
        if (userAnswers[qIdx] === quizData[qIdx].ans) {
          score++;
        }
      });

      document.getElementById('userScore').textContent = score;
      const pct = (answeredCount / quizData.length) * 100;
      document.getElementById('quizProgress').style.width = `${pct}%`;

      const commentEl = document.getElementById('scoreComment');
      if (answeredCount === quizData.length) {
        if (score >= 23) {
          commentEl.textContent = '🌟 Outstanding! You are 100% prepared for an A+ on tomorrow’s midterm!';
          commentEl.style.color = '#34d399';
        } else if (score >= 18) {
          commentEl.textContent = '👍 Great job! Review the questions you missed and the 15 traps above.';
          commentEl.style.color = '#38bdf8';
        } else {
          commentEl.textContent = '⚠️ Keep reviewing! Pay special attention to Slicing, Operators, and Return vs Print.';
          commentEl.style.color = '#fbbf24';
        }
      } else {
        commentEl.textContent = `Answered ${answeredCount} of ${quizData.length} questions.`;
      }
    }

    // Initialize on page load
    function resetQuiz() {
      userAnswers = {};
      renderQuiz();
      updateQuizProgress();
      const commentEl = document.getElementById('scoreComment');
      commentEl.textContent = 'Answer the questions below to test your knowledge.';
      commentEl.style.color = '#94a3b8';
    }

    window.onload = function() {
      updateVisualizer();
      renderFlashcards();
      renderQuiz();
    };
  </script>
</body>
</html>
'''

with open(r'c:\Users\Fadi\Desktop\loops cs\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Website generated successfully at c:\\Users\\Fadi\\Desktop\\loops cs\\index.html")
