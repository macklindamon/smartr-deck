#!/usr/bin/env python3
"""Replace old dot-grid with new denser dot-grid in deck.html"""

html_path = 'deck.html'
dots_path = 'dots.txt'

with open(html_path, 'r') as f:
    lines = f.readlines()

with open(dots_path, 'r') as f:
    new_dots = f.read()

# Find start and end markers
start_marker = '<!-- Dot-grid world map (875 dots) -->'
end_marker = '<!-- Total dots: 875 -->'

start_idx = None
end_idx = None

for i, line in enumerate(lines):
    if start_marker in line:
        start_idx = i
    if end_marker in line:
        end_idx = i

if start_idx is None or end_idx is None:
    print(f"ERROR: Could not find markers. start={start_idx}, end={end_idx}")
    exit(1)

print(f"Found dots section: lines {start_idx+1} to {end_idx+1}")

# Build new content: replace the dot comment line + all dots + total comment
new_dot_section = f'<!-- Dot-grid world map (2989 dots) -->\n{new_dots}\n'

# Replace: keep everything before start_idx, insert new dots, keep end_idx+1 onwards
new_lines = lines[:start_idx] + [new_dot_section] + lines[end_idx+1:]

with open(html_path, 'w') as f:
    f.writelines(new_lines)

print(f"Done! Replaced {end_idx - start_idx + 1} old lines with new dot content.")
print(f"New file has {len(new_lines)} lines")
