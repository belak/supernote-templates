from textwrap import dedent

import svg

from utils import MM, SCREEN_WIDTH, SCREEN_HEIGHT, generate_grid, generate_dot_grid, border


grid_width = 30
grid_height = 40
offset_line = 10

top_corner = (
    (SCREEN_WIDTH - grid_width * 4.0 * MM) / 2,
    (SCREEN_HEIGHT - grid_height * 4.0 * MM) / 2,
)

grid_size = 4.0 * MM


canvas = svg.SVG(
    width=1404,
    height=1872,
    elements=[
        #border(),
        generate_grid(
            top_corner[0],
            top_corner[1],
            grid_size,
            grid_width,
            grid_height,
            # stroke_dasharray=[0.375 * MM, 0.25 * MM, 0.375 * MM, 0 * MM],
            # stroke_dasharray=[0.5 * MM, 0.25 * MM, 0.5 * MM, 0 * MM],
            stroke_dasharray=[3, 3],
        ),
        svg.Path(
            stroke="#000000",
            fill="none",
            stroke_width=1,
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
