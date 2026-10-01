import json
import re

transcript_path = r"C:\Users\Yug Pathak\.gemini\antigravity-ide\brain\e3423523-92ea-4085-b334-2e7beb4f4a7f\.system_generated\logs\transcript_full.jsonl"
dashboard_path = r"C:\Users\Yug Pathak\Desktop\PRAVAH\SIH_2026_PLANNS\NLP\nlp_task_ddr\dashboard\templates\dashboard.html"

extracted_lines = {}

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        if 'Showing lines' in line and 'dashboard.html' in line:
            # We found a potential hit, it might be in 'content' string of a TOOL_RESPONSE
            try:
                data = json.loads(line)
                content = data.get('content', '')
                if 'Showing lines' in content and 'dashboard.html' in content and 'Total Lines: 707' in content:
                    lines = content.split('\n')
                    for l in lines:
                        match = re.match(r'^(\d+):\s(.*)$', l)
                        if match:
                            line_num = int(match.group(1))
                            extracted_lines[line_num] = match.group(2)
            except Exception as e:
                pass

if extracted_lines:
    print(f"Recovered {len(extracted_lines)} lines!")
    max_line = max(extracted_lines.keys())
    with open(dashboard_path, 'w', encoding='utf-8') as f:
        for i in range(1, max_line + 1):
            f.write(extracted_lines.get(i, "") + "\n")
    print("Success!")
else:
    print("No lines extracted.")
