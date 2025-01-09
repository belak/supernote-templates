from textwrap import dedent

import svg

from utils import MM, SCREEN_WIDTH, SCREEN_HEIGHT, generate_grid, generate_dot_grid, border


grid_size = 4.0 * MM
grid_width = int(SCREEN_WIDTH // grid_size) + 1
grid_height = int(SCREEN_HEIGHT // grid_size) + 1
offset_line = 10
dash_unit = grid_size / 18

top_corner = (
    (SCREEN_WIDTH - grid_width * 4.0 * MM) / 2,
    (SCREEN_HEIGHT - grid_height * 4.0 * MM) / 2,
)


canvas = svg.SVG(
    width=1404,
    height=1872,
    elements=[
        # border(),
        generate_grid(
            top_corner[0],
            top_corner[1],
            grid_size,
            grid_width,
            grid_height,
            stroke="#888888",
            # stroke_dasharray=[0.375 * MM, 0.25 * MM, 0.375 * MM, 0 * MM],
            # stroke_dasharray=[0.5 * MM, 0.25 * MM, 0.5 * MM, 0 * MM],
            stroke_dasharray=[dash_unit * 2, dash_unit * 2, dash_unit * 2, 0],
        ),
        svg.Path(
            stroke="#000000",
            fill="none",
            stroke_width=2,
            d=[
                svg.M(
                    x=top_corner[0] + offset_line * grid_size,
                    y=top_corner[1],
                ),
                svg.v(grid_size * grid_height),
            ],
        ),
    ],
)

print(canvas)
