from textwrap import dedent

import svg

from supernote_nomad import MM, SCREEN_WIDTH, SCREEN_HEIGHT, border
from utils import generate_grid, generate_dot_grid


grid_size = 4.0 * MM
grid_width = int(SCREEN_WIDTH // grid_size)
grid_height = int(SCREEN_HEIGHT // grid_size)
offset_line = 10
dash_unit = grid_size / 18

top_corner = (
    (SCREEN_WIDTH - grid_width * grid_size) / 2,
    (SCREEN_HEIGHT - grid_height * grid_size) / 2,
)

text_spacing = 10 * grid_size / 7


canvas = svg.SVG(
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT,
    elements=[
        # border(),
        generate_grid(
            top_corner[0],
            top_corner[1] + 4 * grid_size,
            grid_size,
            grid_width,
            grid_height - 4,
            enable_border=False,
            stroke="#888888",
            # stroke_dasharray=[0.375 * MM, 0.25 * MM, 0.375 * MM, 0 * MM],
            # stroke_dasharray=[0.5 * MM, 0.25 * MM, 0.5 * MM, 0 * MM],
            stroke_dasharray=[dash_unit * 2, dash_unit * 2, dash_unit * 2, 0],
        ),
        generate_grid(
            top_corner[0] + 10 * grid_size,
            top_corner[1],
            grid_size,
            1,
            4,
            stroke_width=2,
            # stroke_dasharray=[0.375 * MM, 0.25 * MM, 0.375 * MM, 0 * MM],
            # stroke_dasharray=[0.5 * MM, 0.25 * MM, 0.5 * MM, 0 * MM],
            # stroke_dasharray=[dash_unit * 1, dash_unit * 1, dash_unit * 1, 0],
        ),
        generate_grid(
            top_corner[0] + 11 * grid_size,
            top_corner[1],
            grid_size,
            grid_width - 11,
            4,
            enable_border=False,
            stroke="#888888",
            # stroke_dasharray=[0.375 * MM, 0.25 * MM, 0.375 * MM, 0 * MM],
            # stroke_dasharray=[0.5 * MM, 0.25 * MM, 0.5 * MM, 0 * MM],
            stroke_dasharray=[dash_unit * 2, dash_unit * 2, dash_unit * 2, 0],
        ),
        svg.Path(
            stroke="#000000",
            fill="none",
            stroke_width=1,
            d=[
                svg.M(
                    x=top_corner[0],
                    y=top_corner[1] + 4 * grid_size,
                ),
                svg.h(grid_size * grid_width),
            ],
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
        svg.Rect(
            x=top_corner[0],
            y=top_corner[1] + 3 * grid_size,
            width=10 * grid_size,
            height=1 * grid_size,
            fill="none",
            stroke="#000000",
            stroke_width=2,
        ),
        svg.Rect(
            x=top_corner[0],
            y=top_corner[1],
            width=grid_width * grid_size,
            height=grid_height * grid_size,
            fill="none",
            stroke="#000000",
            stroke_width=2,
        ),
        svg.Text(
            y=top_corner[1] + 3.575 * grid_size,
            font_size=3.5 * MM,
            font_family="Monaco",
            dominant_baseline="middle",
            elements=[
                svg.TSpan(
                    text_anchor="middle",
                    x=top_corner[0] + (i + 0.5) * text_spacing,
                    text=day,
                )
                for (i, day) in enumerate("MTWTFSS")
            ],
        ),
    ],
)

print(canvas)
