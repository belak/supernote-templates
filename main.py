import svg

PPI = 300
MM = PPI / 25.4


def generate_grid(x: float, y: float, size: float, width: int, height: int, **kwargs):
    elements = []
    for x_pos in range(width + 1):
        elements.append(
            svg.Path(
                stroke="#000000",
                stroke_width=1,
                d=[
                    svg.M(x + x_pos * size, y),
                    svg.v(size * height),
                ],
                **kwargs,
            )
        )

    for y_pos in range(height + 1):
        elements.append(
            svg.Path(
                stroke="#000000",
                stroke_width=1,
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


def generate_dot_grid(x: float, y: float, size: float, width: int, height: int):
    elements = []

    for x_pos in range(width + 1):
        for y_pos in range(height + 1):
            elements.append(
                svg.Circle(
                    fill="#000000",
                    cx=x + x_pos * size,
                    cy=y + y_pos * size,
                    r=1,
                )
            )

    return svg.G(
        fill="none",
        elements=elements,
    )


canvas = svg.SVG(
    width=1404,
    height=1872,
    elements=[
        # Top Bar
        svg.Rect(width=1404, height=99, fill="#ff00ff"),
        # Side Bar
        svg.Rect(width=99, height=1872, fill="#ff00ff"),
        # Outer line
        svg.Path(
            stroke="#000000",
            fill="none",
            stroke_width=1,
            d=[
                svg.M(0, 0),
                svg.L(1404, 0),
                svg.L(1404, 1872),
                svg.L(0, 1872),
                svg.Z(),
            ],
        ),
        generate_grid(
            10.0*MM, 10.0*MM, 4.0*MM, 27, 37, stroke_dasharray=[0.375 * MM, 0.25 * MM, 0.375 * MM, 0 * MM]
        ),
        # generate_dot_grid(10.0*MM, 10.0*MM, 4.0*MM, 27, 37),
    ],
)

print(canvas)
