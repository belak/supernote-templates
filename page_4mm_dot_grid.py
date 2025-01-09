from textwrap import dedent

import svg

from supernote_nomad import MM, SCREEN_WIDTH, SCREEN_HEIGHT, border
from utils import generate_grid, generate_dot_grid


grid_size = 4.0 * MM
grid_width = int(SCREEN_WIDTH // grid_size) - 1
grid_height = int(SCREEN_HEIGHT // grid_size) - 1

top_corner = (
    (SCREEN_WIDTH - grid_width * 4.0 * MM) / 2,
    (SCREEN_HEIGHT - grid_height * 4.0 * MM) / 2,
)


canvas = svg.SVG(
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT,
    elements=[
        # border(),
        generate_dot_grid(
            top_corner[0],
            top_corner[1],
            grid_size,
            grid_width,
            grid_height,
            fill="#888888",
        ),
    ],
)

print(canvas)
