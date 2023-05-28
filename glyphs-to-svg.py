#!/usr/bin/env python3

from blackrenderer.font import BlackRendererFont
from blackrenderer.backends import getSurfaceClass
from pathlib import Path


glyph_dir = "glyphs" # the directory containing all glyph svgs
font = BlackRendererFont("font.ttf") # the font file
font.setLocation({"EDPT": 200}) # if the font is variable, set the axis values
palette = font.getPalette(1)  # set the palette


def replace_svg(path):
    glyphname = path.stem
    bounding_box = font.getGlyphBounds(glyphname)
    surfaceClass = getSurfaceClass("svg")
    surface = surfaceClass()
    with surface.canvas(bounding_box) as canvas:
        font.drawGlyph(glyphname, canvas, palette=palette)
    surface.saveImage(path)


for f in Path(glyph_dir).glob('**/*'):
    if not f.is_file() and f.suffix != "svg":
        continue
    replace_svg(f)
