import os

patch = """
  <!-- PRAVAH GLOBAL LIGHT THEME OVERRIDES -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style>
    :root {
      --bg-desktop: #F6F7F9 !important;
      --bg-bar: #FFFFFF !important;
      --border-bar: #EAECF0 !important;
      --bg-terminal: #FFFFFF !important;
      --bg-card: #FFFFFF !important;
      --bg-card-hover: #F9FAFB !important;
      --bg-input: #FFFFFF !important;
      --border-neon: #D9DDE3 !important;
      --border-neon-subtle: #EAECF0 !important;
      --border-muted: #D9DDE3 !important;
      --cyan-bright: #B22222 !important;
      --cyan-glow: #B22222 !important;
      --cyan-dim: #8B1A1A !important;
      --text-main: #1B1F24 !important;
      --text-secondary: #667085 !important;
      --text-muted: #98A2B3 !important;
      --accent-green: #059669 !important;
      --accent-yellow: #D97706 !important;
      --accent-orange: #D97706 !important;
      --accent-red: #DC2626 !important;
      --accent-purple: #4F46E5 !important;
    }
    
    body, html {
      background: var(--bg-desktop) !important;
      font-family: 'Inter', sans-serif !important;
      color: var(--text-main) !important;
    }
    
    /* Hide old standalone wrappers since we run in iframe */
    .bar { display: none !important; }
    .titlebar { display: none !important; }
    .desktop-wrap, .desktop { padding: 0 !important; height: 100vh !important; background: var(--bg-desktop) !important; }
    #matrixCanvas { display: none !important; }
    .terminal { 
      border: none !important; 
      border-radius: 0 !important; 
      box-shadow: none !important; 
      background: var(--bg-desktop) !important;
      animation: none !important;
      max-width: none !important;
      backdrop-filter: none !important;
    }
    
    /* Override hardcoded dark RGBA colors */
    .left-panel, .right-panel, main, .monitor-wrap, .layout, .panel, .module-container, #map-container, .graph-sidebar, #sidebar {
      background: var(--bg-desktop) !important;
      border-color: var(--border-muted) !important;
    }
    .section-card, .metric-card, .agent-card, .scenario-trigger-box, .stat-box, .alert-card, .map-overlay, .panel-content, #legend, #controls, #panel, .well-card, #layer-bar, #map-stats, .custom-select-dropdown, .term-card {
      background: var(--bg-card) !important;
      border-color: var(--border-muted) !important;
      color: var(--text-main) !important;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
    }
    .field-input, .search-bar, .timeline-container, .citations-box, .chat-bottom-bar, .analog-item, .chat-input, .prompts-bar, .custom-select-btn, .lpill, .csd-search, .tab-btn {
      background: var(--bg-input) !important;
      border-color: var(--border-muted) !important;
      color: var(--text-main) !important;
    }
    
    /* Specific element fixes */
    .msg-bubble-user {
      background: #F0F4F8 !important;
      border: 1px solid #D9DDE3 !important;
      color: #1B1F24 !important;
      box-shadow: none !important;
    }
    .agent-card {
      background: #FFFFFF !important;
      border: 1px solid var(--border-muted) !important;
      border-left: 3px solid #B22222 !important;
      box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
    }
    .prompt-deck, .prompt-box {
      background: #FFFFFF !important;
      border-bottom: 1px solid #EAECF0 !important;
    }
    .timeline-chip, .st-btn, .prompt-chip, .hazard-pill, .citation-chip, .btn-return, .badge, .hpill, .prompt-tag {
      background: rgba(178,34,34, 0.08) !important;
      border: 1px solid rgba(178,34,34, 0.3) !important;
      color: #B22222 !important;
    }
    .hazard-pill.active, .hpill.active, .lpill.active, .tab-btn.active {
      background: #B22222 !important;
      color: white !important;
    }
    .evidence-card, .weights-card {
      background: #F9FAFB !important;
      border-color: #EAECF0 !important;
    }
    .btn-send, .btn-primary {
      background: #B22222 !important;
      color: white !important;
      border: none !important;
    }
    .agent-body {
      color: #1B1F24 !important;
    }
    .agent-meta-left {
      color: #667085 !important;
    }
    #mynetwork {
      background-color: var(--bg-desktop) !important;
    }
    .chart-container, .viz-container, .plot-frame {
      background: #FFFFFF !important;
      border-color: #EAECF0 !important;
    }
    .st-icon {
      background: rgba(178,34,34, 0.1) !important;
      border: 1px solid rgba(178,34,34, 0.3) !important;
      color: #B22222 !important;
    }
    .prompt-cmd, .prompt-user {
      color: #1B1F24 !important;
    }
    /* Map fixes */
    .dark-tiles { filter: none !important; }
    .leaflet-container { background: #E5E7EB !important; }
    .leaflet-popup-content-wrapper, .leaflet-popup-tip {
      background: var(--bg-card) !important;
      border: 1px solid var(--border-muted) !important;
      color: var(--text-main) !important;
    }
    .leaflet-bar a {
      background: var(--bg-card) !important;
      color: var(--text-main) !important;
      border-color: var(--border-muted) !important;
    }
    .leaflet-bar a:hover {
      background: var(--bg-input) !important;
      color: var(--cyan-bright) !important;
    }
    .terminal-body, .term-body { background: var(--bg-desktop) !important; }
    /* Dashboard 3 specific overrides */
    .kpi-card { background: var(--bg-card) !important; border-color: var(--border-muted) !important; }
    .kpi-value { color: #B22222 !important; text-shadow: none !important; }
    .stat-card { background: var(--bg-card) !important; border-color: var(--border-muted) !important; }
    .stat-card .value { color: #B22222 !important; text-shadow: none !important; }
    .hero-banner { background: var(--bg-card) !important; border-color: var(--border-muted) !important; box-shadow: none !important; }
    .hero-title { color: var(--text-main) !important; }
    .t-step { background: var(--bg-card) !important; border-color: var(--border-muted) !important; }
  </style>
</head>
"""

files_to_patch = [
    r"NLP\nlp_task_ddr\module2\templates\map.html",
    r"NLP\nlp_task_ddr\module3\monitor.html",
    r"NLP\nlp_task_ddr\module4\templates\module4.html",
    r"NLP\nlp_task_ddr\module5_engineering_agent\templates\module5.html"
]

for fp in files_to_patch:
    path = os.path.join(r"c:\Users\Yug Pathak\Desktop\PRAVAH\SIH_2026_PLANNS", fp)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if "<!-- PRAVAH GLOBAL LIGHT THEME OVERRIDES -->" not in content:
            content = content.replace("</head>", patch)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Patched safely: {fp}")
        else:
            print(f"Already patched: {fp}")
