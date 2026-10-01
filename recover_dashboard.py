import json
import re
import os

transcript_path = r"C:\Users\Yug Pathak\.gemini\antigravity-ide\brain\e3423523-92ea-4085-b334-2e7beb4f4a7f\.system_generated\logs\transcript_full.jsonl"
dashboard_path = r"C:\Users\Yug Pathak\Desktop\PRAVAH\SIH_2026_PLANNS\NLP\nlp_task_ddr\dashboard\templates\dashboard.html"

blocks = []

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('type') == 'TOOL_RESPONSE' and data.get('tool_name') == 'default_api:view_file':
                content = data.get('content', '')
                if 'dashboard.html' in content and 'Showing lines' in content:
                    blocks.append(content)
        except Exception as e:
            pass

# Process the blocks to extract lines
all_lines = {}
for b in blocks:
    lines = b.split('\n')
    for l in lines:
        match = re.match(r'^(\d+):\s(.*)$', l)
        if match:
            line_num = int(match.group(1))
            content = match.group(2)
            all_lines[line_num] = content

if all_lines:
    print(f"Recovered {len(all_lines)} lines!")
    max_line = max(all_lines.keys())
    with open(dashboard_path, 'w', encoding='utf-8') as f:
        for i in range(1, max_line + 1):
            f.write(all_lines.get(i, "") + "\n")
    print("Recovery successful!")
else:
    print("Failed to find lines in transcript.")
