# Upgrade script to make index.html ultra-pro and 100% mobile accessible
import re

with open('build_master_hub.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update viewport meta tag for mobile web app capability & safe areas
old_viewport = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
new_viewport = '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">\n  <meta name="theme-color" content="#070a13">\n  <meta name="apple-mobile-web-app-capable" content="yes">\n  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">'
code = code.replace(old_viewport, new_viewport)

# 2. Add Mobile Dock, Copy Code button styles, Back-to-Top, and Touch CSS
pro_css = """
    /* Mobile Safe Areas & Touch Enhancements */
    html {
      scroll-behavior: smooth;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      padding-bottom: env(safe-area-inset-bottom, 20px);
    }

    /* Mobile Bottom Navigation Bar (Pro App Dock) */
    .mobile-dock {
      display: none;
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      height: 64px;
      background: rgba(13, 18, 32, 0.88);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-top: 1px solid rgba(56, 189, 248, 0.2);
      z-index: 999;
      justify-content: space-around;
      align-items: center;
      padding: 0 10px calc(env(safe-area-inset-bottom, 0px) + 2px);
      box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.5);
    }

    .dock-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 3px;
      color: #94a3b8;
      text-decoration: none;
      font-size: 0.68rem;
      font-weight: 700;
      transition: all 0.2s ease;
      cursor: pointer;
      padding: 6px 10px;
      border-radius: 10px;
    }

    .dock-item .dock-icon {
      font-size: 1.15rem;
    }

    .dock-item:hover, .dock-item.active {
      color: #38bdf8;
      transform: translateY(-2px);
    }

    @media (max-width: 960px) {
      .mobile-dock {
        display: flex;
      }
      main.content {
        padding-bottom: 100px !important;
      }
      .mobile-toggle {
        bottom: 80px !important;
      }
    }

    /* Floating Back-To-Top Button */
    .back-to-top {
      position: fixed;
      bottom: 84px;
      left: 20px;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid #334155;
      color: #38bdf8;
      display: grid;
      place-items: center;
      font-size: 1.2rem;
      cursor: pointer;
      z-index: 120;
      opacity: 0;
      visibility: hidden;
      transition: all 0.25s ease;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4);
    }

    .back-to-top.show {
      opacity: 1;
      visibility: visible;
    }

    .back-to-top:hover {
      background: #1e293b;
      border-color: #38bdf8;
      transform: translateY(-2px);
    }

    /* Pro Code Blocks with Copy Button */
    .code-wrapper {
      position: relative;
      margin: 14px 0;
    }

    .code-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #141b2d;
      border: 1px solid var(--code-border);
      border-bottom: none;
      border-radius: 10px 10px 0 0;
      padding: 6px 14px;
      font-size: 0.75rem;
      font-family: 'Fira Code', monospace;
      color: #94a3b8;
    }

    .code-header .code-lang {
      font-weight: 700;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .code-header .btn-copy {
      background: #1c263c;
      border: 1px solid #2d3b55;
      color: #cbd5e1;
      padding: 3px 9px;
      border-radius: 6px;
      font-size: 0.72rem;
      cursor: pointer;
      transition: all 0.15s ease;
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .code-header .btn-copy:hover {
      background: #25334e;
      color: #fff;
      border-color: #38bdf8;
    }

    .code-header .btn-copy.copied {
      background: rgba(16, 185, 129, 0.2);
      border-color: #10b981;
      color: #34d399;
    }

    .code-wrapper pre {
      margin: 0 !important;
      border-radius: 0 0 10px 10px !important;
    }

    /* Mobile Table Scroll Wrappers */
    .table-container {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      margin: 14px 0;
      border: 1px solid var(--border);
      border-radius: 12px;
      background: #0f1523;
    }

    .table-container .custom-table {
      margin: 0;
      border: none;
    }

    /* Touch optimizations for quiz options and flashcards */
    .quiz-opt {
      min-height: 48px;
      user-select: none;
      -webkit-user-select: none;
    }

    .flashcard {
      min-height: 220px;
    }

    @media (max-width: 640px) {
      .hero h1 {
        font-size: 1.8rem;
      }
      .section-header h2 {
        font-size: 1.35rem;
      }
      .card {
        padding: 18px 14px;
      }
      .slice-inputs {
        flex-direction: column;
        gap: 10px;
      }
      .stats-row {
        grid-template-columns: repeat(2, 1fr);
      }
    }
"""

# Insert pro_css before </style>
code = code.replace('</style>', pro_css + '\n  </style>')

# 3. Add Mobile Bottom Dock & Back-to-Top HTML right before </main>
mobile_dock_html = """
    <!-- Floating Back to Top -->
    <button class="back-to-top" id="backToTop" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" title="Back to top">↑</button>

    <!-- Mobile App Bottom Dock -->
    <nav class="mobile-dock" id="mobileDock">
      <a class="dock-item" onclick="jumpSection('cram-sheet')">
        <span class="dock-icon">📋</span>
        <span>Cram</span>
      </a>
      <a class="dock-item" onclick="jumpSection('functions-directory')">
        <span class="dock-icon">📚</span>
        <span>Functions</span>
      </a>
      <a class="dock-item" onclick="jumpSection('slicing-lab')">
        <span class="dock-icon">🔬</span>
        <span>Slicing</span>
      </a>
      <a class="dock-item" onclick="jumpSection('traps')">
        <span class="dock-icon">⚠️</span>
        <span>Traps</span>
      </a>
      <a class="dock-item" onclick="jumpSection('flashcards')">
        <span class="dock-icon">🃏</span>
        <span>Cards</span>
      </a>
      <a class="dock-item" onclick="jumpSection('mock-exam')">
        <span class="dock-icon">📝</span>
        <span>Quiz</span>
      </a>
    </nav>
"""

code = code.replace('</main>', mobile_dock_html + '\n  </main>')

# 4. Add JavaScript for Copy Code Buttons and Scroll Listener
pro_js = """
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
"""

# Insert pro_js before </script>
code = code.replace('</script>', pro_js + '\n  </script>')

with open('build_master_hub.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_master_hub.py upgraded with Pro Mobile & UI features!")
