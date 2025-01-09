# Supernote Nomad
# Resolution: 1404x1872
# PPI: 300
#
# This means we can calculate the screen size by taking the resolution, dividing
# by the PPI and multiplying by how many mm per inch (25.4).
#
# Screen Size: 4.68in x 6.24in
# Screen Size: 118.872mm x 158.496mm
#
# PPmm = PPI / 25.4, or about 11.81102362
# Additionally, when scaled using PPmm, 1px is roughly 0.08466667mm.

SCREEN_WIDTH = 1404.0
SCREEN_HEIGHT = 1872.0
PPI = 300.0
MM = PPI / 25.4


def top_bar():
    return svg.Rect(width=1404, height=99, fill="#ff00ff")


def side_bar():
    return svg.Rect(width=99, height=1872, fill="#ff00ff")


def border():
    return svg.Rect(
        x=0,
        y=0,
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT,
        fill="none",
        stroke="#000000",
        stroke_width=1,
    )
