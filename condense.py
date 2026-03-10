#!/usr/bin/env python3
"""Remove slides 15, 16, 17 and renumber slide 18 -> 15 to condense to 15 slides."""

with open('deck.html', 'r') as f:
    content = f.read()

# Markers
s15_comment = '<!-- SLIDE 15'
s18_comment = '<!-- SLIDE 18'

# Find the separator line before SLIDE 15
# The pattern is: \n\n<!-- === ... === -->\n<!-- SLIDE 15
s15_pos = content.find(s15_comment)
# Walk backwards to find the separator line start
sep_start = content.rfind('\n', 0, s15_pos - 2)  # find newline before separator
# Actually let's find the full comment block: 3 lines (separator, slide comment, separator)
# Go back to the blank line before the comment block
block_start = content.rfind('\n\n', 0, s15_pos)
if block_start == -1:
    block_start = content.rfind('\n', 0, s15_pos)

# Find start of SLIDE 18 comment block
s18_pos = content.find(s18_comment)
block_end = content.rfind('\n\n', 0, s18_pos)
if block_end == -1:
    block_end = content.rfind('\n', 0, s18_pos)

print(f"Removing from position {block_start} to {block_end}")
print(f"Removing {block_end - block_start} characters")

# Preview boundaries
print(f"\n--- BEFORE CUT (last 100 chars) ---")
print(repr(content[block_start-50:block_start+50]))
print(f"\n--- AFTER CUT (first 100 chars) ---")  
print(repr(content[block_end:block_end+100]))

# Count sections being removed
removed = content[block_start:block_end]
section_count = removed.count('<section')
print(f"\nRemoving {section_count} sections")

# Perform removal
new_content = content[:block_start] + content[block_end:]

# Renumber slide 18 -> 15
new_content = new_content.replace('data-slide="18"', 'data-slide="15"')
new_content = new_content.replace('SLIDE 18', 'SLIDE 15')

# Update counter display "1 / 11" or "1 / 18" to "1 / 15"
# The counter is set dynamically via JS using total=slides.length, so no change needed there

# Verify final slide count
final_count = new_content.count('<section class="slide')
print(f"\nFinal slide count: {final_count}")

with open('deck.html', 'w') as f:
    f.write(new_content)

print("Done! Saved deck.html")
