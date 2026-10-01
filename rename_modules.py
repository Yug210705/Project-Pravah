import os
import glob

# Search directory
base_dir = r"c:\Users\Yug Pathak\Desktop\PRAVAH\SIH_2026_PLANNS\NLP\nlp_task_ddr"

# HTML files to update
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

replacements = {
    "nwis@sentinel": "pravah@command-center",
    "NWIS-Sentinel": "PRAVAH",
    
    "Module 1": "Data Foundation",
    "Module 2": "Geospatial Engine",
    "Module 3": "Live Drilling Engine",
    "Module 4": "Knowledge Graph",
    "Module 5": "Pravah Copilot",
    
    "module 1": "data foundation",
    "module 2": "geospatial engine",
    "module 3": "live drilling engine",
    "module 4": "knowledge graph",
    "module 5": "pravah copilot",
    
    "module1": "data_foundation",
    "module2": "geospatial_engine",
    "module3": "live_drilling",
    "module4": "knowledge_graph",
    "module5": "pravah_copilot",

    # For any generic remaining user-facing references
    "All modules": "All systems",
    "all modules": "all systems",
    "Modules": "Engines",
    "modules": "engines",
    "Module": "Engine",
    
    # Do not break paths, so we will ONLY replace specific known terminal text or user facing titles.
    # Wait, the simple replace might break Javascript routes like `/module3/monitor` if I blindly replace "module3" with "live_drilling".
    # So I must be careful!
}

# Safe targeted replacements for HTML content (not breaking paths)
safe_replacements = [
    ("nwis@sentinel", "pravah@command"),
    ("NWIS-Sentinel", "PRAVAH"),
    ("NWIS", "PRAVAH"),
    ("Module 1", "Data Foundation"),
    ("Module 2", "Geospatial Engine"),
    ("Module 3", "Live Drilling Engine"),
    ("Module 4", "Knowledge Graph"),
    ("Module 5", "Pravah Copilot"),
    ("MODULE 1", "DATA FOUNDATION"),
    ("MODULE 2", "GEOSPATIAL ENGINE"),
    ("MODULE 3", "LIVE DRILLING ENGINE"),
    ("MODULE 4", "KNOWLEDGE GRAPH"),
    ("MODULE 5", "PRAVAH COPILOT"),
    ("~/module3", "~/live-drilling"),
    ("~/module4", "~/knowledge-graph"),
    ("~/module5", "~/pravah-copilot"),
    ("~/module2", "~/geospatial-engine"),
    ("~/module1", "~/data-foundation"),
    ("module3-telemetry-monitor", "live-drilling-engine"),
    ("module4-graphrag-studio", "knowledge-graph-studio"),
    ("module2-geospatial-engine", "geospatial-engine"),
    ("module3_telemetry_monitor", "live_drilling_engine"),
    ("module4_knowledge_graph", "knowledge_graph_engine"),
    ("module2_geospatial_engine", "geospatial_engine"),
    ("All modules online", "All systems online"),
    ("all modules", "all systems")
]

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    for old, new in safe_replacements:
        content = content.replace(old, new)
        
    # Also replace isolated "module" in user text (careful with tags and urls)
    # We'll just stick to the safe replacements which covers 99% of visible text.
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {file_path}")
