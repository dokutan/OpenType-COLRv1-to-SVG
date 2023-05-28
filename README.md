# OpenType-COLRv1-to-SVG
Convert OpenType COLR or COLRv1 fonts to SVG

## Converting the font

### 0. Install dependencies and obtain a font
```
pip install opentypesvg blackrenderer
```

Obtain a COLR(v1) font from e.g. https://fonts.google.com/?coloronly=true.

### 1. create monochrome svgs for all glyphs
Use fonts2svg to obtain a list of glyphs.
```
mkdir glyphs
fonts2svg -o glyphs font.ttf
```

### 2. replace the monochrome svgs
Use blackrenderer to replace the monochrome svgs with color svgs. Edit ``glyph-to-svg.py`` to set the font options.
```
python glyphs-to-svg.py
```

### 3. add the color svgs to the font
```
addsvg glyphs/ font.subset.ttf
```
