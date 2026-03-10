#!/usr/bin/env python3
"""Replace inline dot-grid circles with an <image> referencing the SVG file."""

with open('deck.html', 'r') as f:
    lines = f.readlines()

# Find the dot-grid comment line and the Total dots comment line
start_idx = None
end_idx = None
for i, line in enumerate(lines):
    if '<!-- Dot-grid world map' in line:
        start_idx = i
    if '<!-- Total dots:' in line:
        end_idx = i
        break

print(f'Dot grid: lines {start_idx+1} to {end_idx+1}')

# Replace lines start_idx through end_idx (inclusive) with the image reference
replacement = '      <!-- World map from external SVG -->\n'
replacement += '      <image href="World_map_blue_dots.svg" x="0" y="0" width="1200" height="600" opacity="0.35" style="filter:saturate(0) brightness(2)"/>\n'

new_lines = lines[:start_idx] + [replacement] + lines[end_idx+1:]

with open('deck.html', 'w') as f:
    f.writelines(new_lines)

print(f'Removed {end_idx - start_idx + 1} lines, replaced with image tag')
print(f'New file: {len(new_lines)} lines')
