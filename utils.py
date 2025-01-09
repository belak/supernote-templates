from textwrap import dedent

import svg


def generate_grid(x: float, y: float, size: float, width: int, height: int, enable_border=True, stroke: str="#000000", stroke_width=1, **kwargs):
    elements = []

    start = 0 if enable_border else 1
    end_offset = 1 if enable_border else 0

    for x_pos in range(start, width + end_offset):
        elements.append(
            svg.Path(
                stroke=stroke,
                stroke_width=stroke_width,
                d=[
                    svg.M(x + x_pos * size, y),
                    svg.v(size * height),
                ],
                **kwargs,
            )
        )

    for y_pos in range(start, height + end_offset):
        elements.append(
            svg.Path(
                stroke=stroke,
                stroke_width=stroke_width,
                d=[
                    svg.M(x, y + y_pos * size),
                    svg.h(size * width),
                ],
                **kwargs,
            )
        )

    return svg.G(
        fill="none",
        elements=elements,
    )


def generate_dot_grid(x: float, y: float, size: float, width: int, height: int, fill="#000000"):
    elements = []

    for x_pos in range(width + 1):
        for y_pos in range(height + 1):
            elements.append(
                svg.Circle(
                    fill=fill,
                    cx=x + x_pos * size,
                    cy=y + y_pos * size,
                    r=2,
                )
            )

    return svg.G(
        fill="none",
        elements=elements,
    )
