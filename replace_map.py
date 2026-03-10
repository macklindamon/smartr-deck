#!/usr/bin/env python3
"""Replace continent path outlines with dot-grid in deck.html."""
import re

with open('/Users/damonmacklin/smartr-deck/deck.html', 'r') as f:
    html = f.read()

with open('/Users/damonmacklin/smartr-deck/dots_output.txt', 'r') as f:
    dots_svg = f.read().strip()

# Replace everything between the continent outlines comment and the flight arcs comment
old_pattern = r'      <!-- ====== Continent outlines \(proper simplified paths\) ====== -->.*?(?=      <!-- ====== Flight arcs)'
new_content = dots_svg + '\n\n'

html_new = re.sub(old_pattern, new_content, html, flags=re.DOTALL)

if html_new == html:
    print("ERROR: Pattern not found!")
else:
    with open('/Users/damonmacklin/smartr-deck/deck.html', 'w') as f:
        f.write(html_new)
    print("SUCCESS: Replaced continent paths with dot grid")
