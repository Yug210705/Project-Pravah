import os

patch = """
  <!-- PRAVAH HIGH-TECH LIGHT THEME OVERRIDES -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style>
    :root {
      --bg-desktop: #F4F6F9 !important;
      --bg-bar: rgba(255, 255, 255, 0.85) !important;
      --border-bar: rgba(203, 213, 225, 0.6) !important;
      --bg-terminal: #FFFFFF !important;
      --bg-card: #FFFFFF !important;
      --bg-card-hover: #F8FAFC !important;
      --bg-input: #FFFFFF !important;
      --border-neon: rgba(203, 213, 225, 0.6) !important;
      --border-neon-subtle: rgba(226, 232, 240, 0.6) !important;
      --border-muted: rgba(203, 213, 225, 0.6) !important;
      --cyan-bright: #0F172A !important;
      --cyan-glow: #1E293B !important;
      --cyan-dim: #475569 !important;
      --text-main: #0F172A !important;
      --text-secondary: #475569 !important;
      --text-muted: #94A3B8 !important;
      --accent-green: #10B981 !important;
      --accent-yellow: #F59E0B !important;
      --accent-orange: #F97316 !important;
      --accent-red: #EF4444 !important;
      --accent-purple: #8B5CF6 !important;
      --shadow-premium: 0 4px 12px rgba(0, 0, 0, 0.04) !important;
      --brand-gradient: linear-gradient(135deg, #8B1A1A 0%, #DC2626 100%) !important;
      --brand-primary: #B22222 !important;
    }
    
    body, html {
      background: var(--bg-desktop) !important;
      font-family: 'Inter', sans-serif !important;
      color: var(--text-main) !important;
    }
    
    /* Hide old standalone wrappers since we run in iframe */
    .bar, .titlebar, #matrixCanvas { display: none !important; }
    .desktop-wrap, .desktop { 
      padding: 0 !important; 
      margin: 0 !important; 
      height: 100vh !important; 
      width: 100vw !important; 
      background: var(--bg-desktop) !important; 
      overflow: hidden !important;
    }
    
    .terminal { 
      border: none !important; 
      border-radius: 0 !important; 
      box-shadow: none !important; 
      background: var(--bg-desktop) !important;
      animation: none !important;
      max-width: none !important;
      backdrop-filter: none !important;
      width: 100% !important;
      height: 100% !important;
      margin: 0 !important;
      display: flex !important;
      flex-direction: column !important;
    }
    
    /* Panels (Sidebar, Map Container, Main) */
    .left-panel, .right-panel, main, .monitor-wrap, .layout, .panel, .module-container, #map-container, .graph-sidebar, .sidebar, .panel-header, #graphContainer, #nodeInfo {
      background: var(--bg-desktop) !important;
      border-color: var(--border-muted) !important;
    }
    
    /* Extreme Professional Sidebar UI */
    #sidebar {
      order: 2 !important;
      background: #FFFFFF !important;
      border-left: 1px solid var(--border-muted) !important;
      border-right: none !important;
      box-shadow: -4px 0 20px rgba(0, 0, 0, 0.03) !important;
      z-index: 10 !important;
    }
    #map-container {
      order: 1 !important;
    }
    
    /* Sliding Right Panel for Well Data */
    #panel {
      position: absolute !important;
      top: 0 !important;
      right: -450px !important; /* hidden by default */
      width: 420px !important;
      height: 100% !important;
      background: #FFFFFF !important;
      border-left: 1px solid var(--border-muted) !important;
      box-shadow: -10px 0 30px rgba(0, 0, 0, 0.06) !important;
      z-index: 1000 !important;
      transition: right 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
      overflow-y: auto !important;
      padding: 24px 28px !important;
      border-radius: 0 !important;
    }
    #panel.open {
      right: 0 !important;
    }
    .panel-close-btn {
      position: absolute;
      top: 14px;
      right: 14px;
      background: #F4F6F9;
      border: 1px solid var(--border-muted);
      border-radius: 50%;
      width: 32px;
      height: 32px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: var(--text-secondary);
      transition: all 0.2s;
    }
    .panel-close-btn:hover { background: #E2E8F0; color: #0F172A; }
    
    #legend, #controls, #hazard-section {
      background: transparent !important;
      border: none !important;
      border-bottom: 1px solid var(--border-neon-subtle) !important;
      box-shadow: none !important;
      border-radius: 0 !important;
      padding: 24px 28px !important;
      transform: none !important;
    }
    #legend:hover, #controls:hover, #hazard-section:hover {
      transform: none !important;
      box-shadow: none !important;
    }
    
    #legend h3, #controls label, #hazard-section h3, .panel-title {
      color: var(--text-muted) !important;
      font-size: 10.5px !important;
      letter-spacing: 0.15em !important;
      margin-bottom: 14px !important;
      font-weight: 700 !important;
      text-transform: uppercase !important;
    }
    
    .custom-select-btn {
      background: #F8FAFC !important;
      border: 1px solid var(--border-neon-subtle) !important;
      border-radius: 8px !important;
      padding: 10px 16px !important;
      font-size: 13px !important;
      color: var(--text-main) !important;
      font-family: 'Inter', sans-serif !important;
      font-weight: 500 !important;
      box-shadow: 0 1px 2px rgba(0,0,0,0.02) !important;
    }
    
    .radius-row input[type=range] {
      -webkit-appearance: none !important;
      height: 4px !important;
      background: var(--border-neon-subtle) !important;
      border-radius: 2px !important;
    }
    .radius-row input[type=range]::-webkit-slider-thumb {
      -webkit-appearance: none !important;
      width: 16px !important;
      height: 16px !important;
      border-radius: 50% !important;
      background: #0F172A !important;
      cursor: pointer !important;
      border: 3px solid #FFFFFF !important;
      box-shadow: 0 2px 5px rgba(0,0,0,0.2) !important;
    }
    #radius-val { font-size: 13px !important; color: var(--text-main) !important; font-weight: 600 !important; }
    
    .stat-chip {
      background: transparent !important;
      border: none !important;
      box-shadow: none !important;
      padding: 4px 0 !important;
      border-radius: 0 !important;
      text-align: left !important;
    }
    .stat-chip .val { font-size: 24px !important; color: var(--text-main) !important; font-family: 'Inter', sans-serif !important; font-weight: 700 !important; }
    .stat-chip .lbl { font-size: 10.5px !important; color: var(--text-muted) !important; letter-spacing: 0.05em !important; font-weight: 600 !important; margin-top: 4px !important; }
    .stat-row { gap: 24px !important; border-top: 1px solid var(--border-neon-subtle) !important; padding-top: 20px !important; margin-top: 24px !important; display: flex !important; }
    
    .prompt-deck {
      background: var(--bg-desktop) !important;
      border-bottom: 1px solid var(--border-muted) !important;
      box-shadow: none !important;
      padding: 14px 24px !important;
    }
    
    /* Premium Cards & Containers */
    .section-card, .metric-card, .agent-card, .scenario-trigger-box, .stat-box, .alert-card, .map-overlay, .panel-content, .well-card, #layer-bar, #map-stats, .custom-select-dropdown, .term-card, .chart-container, .viz-container, .plot-frame, .kpi-card, .stat-card, .deliv-card, .alert-item, .risk-card, .t-step, .backtest-banner {
      background: var(--bg-card) !important;
      border-color: var(--border-muted) !important;
      color: var(--text-main) !important;
      box-shadow: var(--shadow-premium) !important;
      border-radius: 12px !important;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* Card Hover Animations */
    .section-card:hover, .stat-box:hover, .well-card:hover, .term-card:hover, .agent-card:hover, .scenario-trigger-box:hover, .kpi-card:hover, .stat-card:hover, .deliv-card:hover, .alert-item:hover, .risk-card:hover {
      transform: translateY(-2px) !important;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.06) !important;
      border-color: rgba(178,34,34,0.2) !important;
    }
    
    /* Inputs & Toolbars */
    .field-input, .search-bar, .timeline-container, .citations-box, .chat-bottom-bar, .analog-item, .chat-input, .prompts-bar, .custom-select-btn, .lpill, .csd-search, .tab-btn, .t-depth, .well-search, .well-select, .well-select option, .rag-input, .rag-card, .rag-rank {
      background: #FFFFFF !important;
      border-color: var(--border-muted) !important;
      color: var(--text-main) !important;
      border-radius: 8px !important;
      box-shadow: inset 0 1px 2px rgba(0,0,0,0.02) !important;
    /* Copilot & Knowledge Graph Clean UI */
    .left-panel, .right-panel, .chat-bottom-bar, .prompts-bar, .sidebar, .rag-section, .briefing-section, .panel-header {
      background: #FFFFFF !important;
      border-color: var(--border-neon-subtle) !important;
    }
    .panel-header {
      flex-wrap: wrap !important;
      gap: 12px !important;
      border-bottom: 1px solid var(--border-muted) !important;
      padding: 12px 16px !important;
      box-shadow: 0 2px 8px rgba(0,0,0,0.02) !important;
      z-index: 5 !important;
    }
    .terminal-body {
      grid-template-columns: 260px 1.6fr 1fr !important;
      transition: grid-template-columns 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .terminal-body.right-collapsed {
      grid-template-columns: 260px 1fr 0px !important;
    }
    .terminal-body.right-collapsed .right-panel {
      display: none !important;
    }
    .right-panel {
      overflow: hidden !important;
      min-width: 0 !important;
    }
    .collapse-btn {
      background: #F4F6F9 !important;
      border: 1px solid var(--border-muted) !important;
      border-radius: 50% !important;
      width: 28px !important;
      height: 28px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      cursor: pointer !important;
      color: var(--text-secondary) !important;
      transition: all 0.2s !important;
      font-size: 10px !important;
    }
    .collapse-btn:hover {
      background: #E2E8F0 !important;
      color: #0F172A !important;
    }
    .prompt-deck {
      background: #FFFFFF !important;
      border-bottom: 1px solid var(--border-muted) !important;
    }
    .scenario-trigger-box, .stat-card, .rag-input-row {
      background: #FFFFFF !important;
      border: 1px solid var(--border-muted) !important;
      box-shadow: var(--shadow-premium) !important;
      border-radius: 8px !important;
    }
    .st-icon {
      background: rgba(178, 34, 34, 0.1) !important;
      color: var(--brand-primary) !important;
      border: none !important;
    }
    .st-title, .prompt-user, .panel-title, .sidebar-label, .modal-title {
      color: #0F172A !important;
      font-weight: 700 !important;
      letter-spacing: 0.5px !important;
    }
    .panel-title { font-size: 14px !important; display: block !important; white-space: nowrap !important; }
    .node-legend-bar {
      background: #F8FAFC !important;
      border-bottom: 1px solid var(--border-muted) !important;
      box-shadow: inset 0 -1px 3px rgba(0,0,0,0.01) !important;
    }
    .chat-input-wrapper, .rag-input, .well-search, .well-select {
      background: #FFFFFF !important;
      border: 1px solid var(--border-muted) !important;
      box-shadow: inset 0 1px 3px rgba(0,0,0,0.02) !important;
      border-radius: 8px !important;
    }
    .chat-input-wrapper:focus-within, .rag-input:focus, .well-search:focus {
      border-color: var(--brand-primary) !important;
      box-shadow: 0 0 0 3px rgba(178, 34, 34, 0.1) !important;
    }
    .chat-msg.assistant .agent-body, .bs-text {
      color: #0F172A !important;
    }
    .chat-msg.assistant .msg-header .msg-name {
      color: var(--brand-primary) !important;
    }
    .chat-msg.assistant, .briefing-sentence {
      border-left: 3px solid var(--brand-primary) !important;
      background: #FFFFFF !important;
      border-radius: 8px !important;
      box-shadow: var(--shadow-premium) !important;
      padding: 12px 16px !important;
      margin-left: 0 !important;
    }
    
    /* Buttons & Interactive Elements */
    .btn-send, .btn-primary, .hazard-pill.active, .hpill.active, .hero-badge, .send-btn, #btnLoadGraph, #btnBriefing, #btnRAG {
      background: var(--brand-gradient) !important;
      color: white !important;
      border: none !important;
      box-shadow: 0 4px 12px rgba(220, 38, 38, 0.25) !important;
      font-weight: 600 !important;
    }
    
    /* Professional Tabs & Toggles */
    .lpill.active, .tab-btn.active, .p-badge.cyan, .bar-tag.live, .timeline-chip {
      background: #0F172A !important;
      color: white !important;
      border: 1px solid #0F172A !important;
      box-shadow: 0 4px 10px rgba(15, 23, 42, 0.2) !important;
      font-weight: 600 !important;
    }
    .btn-send:hover, .btn-primary:hover, .send-btn:hover {
      transform: translateY(-1px) !important;
      box-shadow: 0 6px 16px rgba(220, 38, 38, 0.35) !important;
    }
    
    /* Pills & Badges (Neutral inactive) */
    .st-btn, .prompt-chip, .hazard-pill, .citation-chip, .btn-return, .badge, .hpill, .prompt-tag, .lpill, .btn, .p-badge, .btn-sm {
      background: #F8FAFC !important;
      border: 1px solid var(--border-muted) !important;
      color: var(--text-secondary) !important;
      border-radius: 6px !important;
      font-weight: 600 !important;
      transition: all 0.2s ease !important;
    }
    .timeline-chip:hover, .st-btn:hover, .prompt-chip:hover, .hazard-pill:hover, .citation-chip:hover, .btn-return:hover, .hpill:hover, .lpill:hover {
      border-color: var(--brand-primary) !important;
      color: var(--brand-primary) !important;
      background: rgba(178,34,34,0.04) !important;
    }
    .st-icon {
      background: rgba(178,34,34, 0.1) !important;
      border: 1px solid rgba(178,34,34, 0.3) !important;
      color: #B22222 !important;
      border-radius: 8px !important;
    }
    
    /* Specific Component Fixes */
    .msg-bubble-user {
      background: var(--bg-desktop) !important;
      border: 1px solid var(--border-muted) !important;
      color: var(--text-main) !important;
      box-shadow: none !important;
      border-radius: 12px 12px 2px 12px !important;
    }
    .agent-card {
      border-left: 4px solid #B22222 !important;
      border-radius: 12px 12px 12px 2px !important;
    }
    .prompt-deck, .prompt-box {
      background: #FFFFFF !important;
      border-bottom: 1px solid var(--border-light) !important;
      border-radius: 12px !important;
      box-shadow: var(--shadow-premium) !important;
    }
    .evidence-card, .weights-card {
      background: var(--bg-surface-secondary) !important;
      border-color: var(--border-light) !important;
      border-radius: 8px !important;
    }
    
    /* Typography Overrides */
    .agent-body { color: var(--text-main) !important; }
    .agent-meta-left { color: var(--text-secondary) !important; }
    .prompt-cmd, .prompt-user { color: var(--text-main) !important; }
    .alert-hazard, .deliv-title, .risk-hazard-name { color: var(--brand-primary) !important; }
    .alert-expl, .alert-depth, .deliv-desc, .t-desc, .kpi-sub, .risk-meta { color: var(--text-secondary) !important; }
    
    /* Table Fixes */
    th { background: #F8FAFC !important; color: var(--text-main) !important; border-bottom: 1px solid var(--border-light) !important; }
    td { color: var(--text-secondary) !important; border-bottom: 1px solid var(--border-light) !important; }
    tr:hover td { background: var(--bg-surface-secondary) !important; color: var(--text-primary) !important; }
    
    /* Typography Highlights */
    .kpi-value, .stat-card .value, .card-header-title {
      background: var(--brand-gradient) !important;
      -webkit-background-clip: text !important;
      -webkit-text-fill-color: transparent !important;
      text-shadow: none !important;
    }
    
    /* Map & Graph fixes */
    #mynetwork { background-color: var(--bg-desktop) !important; }
    .dark-tiles { filter: none !important; }
    .leaflet-container { background: #E5E7EB !important; border-radius: 12px !important; }
    .leaflet-popup-content-wrapper, .leaflet-popup-tip {
      background: var(--bg-card) !important;
      border: 1px solid var(--border-muted) !important;
      color: var(--text-main) !important;
      border-radius: 8px !important;
      box-shadow: var(--shadow-premium) !important;
    }
    .leaflet-bar a {
      background: var(--bg-card) !important;
      color: var(--text-main) !important;
      border-color: var(--border-muted) !important;
    }
    .leaflet-bar a:hover {
      background: var(--bg-surface-secondary) !important;
      color: var(--cyan-bright) !important;
    }
    
    /* Legacy Dashboard overrides */
    .terminal-body { 
      background: var(--bg-desktop) !important;
      position: relative !important;
      overflow: hidden !important;
    }
    .term-body { background: var(--bg-desktop) !important; }
    .hero-banner { 
      background: #FFFFFF !important; 
      border: 1px solid var(--border-muted) !important; 
      box-shadow: var(--shadow-premium) !important; 
      border-radius: 12px !important;
    }
    .hero-title { color: var(--text-main) !important; }
    .t-step { background: #FFFFFF !important; border-color: var(--border-muted) !important; border-radius: 8px !important; box-shadow: 0 1px 3px rgba(0,0,0,0.02) !important; }
  </style>
</head>
"""

files_to_patch = [
    r"NLP\nlp_task_ddr\module2\templates\map.html",
    r"NLP\nlp_task_ddr\module3\monitor.html",
    r"NLP\nlp_task_ddr\module4\templates\module4.html",
    r"NLP\nlp_task_ddr\module5_engineering_agent\templates\module5.html"
]

import re

for fp in files_to_patch:
    path = os.path.join(r"c:\Users\Yug Pathak\Desktop\PRAVAH\SIH_2026_PLANNS", fp)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "<!-- PRAVAH HIGH-TECH LIGHT THEME OVERRIDES -->" in content:
            content = re.sub(r'<!-- PRAVAH HIGH-TECH LIGHT THEME OVERRIDES -->.*?</head>', patch.strip(), content, flags=re.DOTALL)
        else:
            content = content.replace("</head>", patch)
            
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"High-Tech Patched: {fp}")
