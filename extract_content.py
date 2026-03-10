#!/usr/bin/env python3
"""Extract structured text content from each slide in deck.html"""
import re, html

with open('deck.html', 'r') as f:
    content = f.read()

# Remove style and script blocks
clean = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
clean = re.sub(r'<script[^>]*>.*?</script>', '', clean, flags=re.DOTALL)

# Split by slide sections
slides = re.split(r'<section[^>]*data-slide="(\d+)"[^>]*>', clean)

output = []
output.append("=" * 60)
output.append("SMARTR DECK — FULL SLIDE CONTENT")
output.append("=" * 60)

i = 1
while i < len(slides):
    slide_num = slides[i]
    slide_html = slides[i + 1] if i + 1 < len(slides) else ""
    # Cut at next section
    slide_html = slide_html.split('</section>')[0]
    
    # Extract SVG text elements before stripping SVGs
    svg_texts = re.findall(r'<text[^>]*>(.*?)</text>', slide_html)
    
    # Remove SVG but keep the text we found
    slide_clean = re.sub(r'<svg[^>]*>.*?</svg>', '', slide_html, flags=re.DOTALL)
    
    # Strip HTML tags
    slide_clean = re.sub(r'<[^>]+>', ' ', slide_clean)
    slide_clean = html.unescape(slide_clean)
    slide_clean = re.sub(r'[ \t]+', ' ', slide_clean)
    slide_clean = re.sub(r'\n\s*\n+', '\n', slide_clean)
    slide_clean = slide_clean.strip()
    
    output.append(f"\n{'—' * 60}")
    output.append(f"SLIDE {slide_num}")
    output.append(f"{'—' * 60}")
    
    if svg_texts:
        output.append(f"\n[Map labels: {', '.join(svg_texts)}]")
    
    output.append(f"\n{slide_clean}")
    
    i += 2

result = '\n'.join(output)
with open('deck_content.txt', 'w') as f:
    f.write(result)

print(result)
