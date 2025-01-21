# Remarkable 2
# Resolution: 1872x1404
# PPI: 226
#
# Screen Size: 6.4in x 8.53in
# Screen Size: 162.56mm x 216.75mm
#
# PPmm = PPI / 25.4, or about 8.8976378
# Additionally, when scaled using PPmm, 1px is roughly 0.11238938mm.

SCREEN_WIDTH = 1404.0
SCREEN_HEIGHT = 1872.0
PPI = 226.0
MM = PPI / 25.4


def side_bar():
    return svg.Rect(width=104, height=SCREEN_HEIGHT, fill="#ff00ff")


def border():
    # Note: the border when screen sharing is 7px. This is not that.
    return svg.Rect(
        x=0,
        y=0,
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT,
        fill="none",
        stroke="#000000",
        stroke_width=1,
    )
