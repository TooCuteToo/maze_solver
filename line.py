from tkinter import Canvas
from point import Point


class Line:
    def __init__(self, fpoint, spoint) -> None:
        assert isinstance(fpoint, Point), f"first point should be instance of Point"
        assert isinstance(spoint, Point), f"second point should be instance of Point"
        self.fpoint = fpoint
        self.spoint = spoint

    def draw(self, canvas, fill_color) -> None:
        assert isinstance(
            canvas, Canvas
        ), f"canvas should be instance of tkinter Canvas"
        assert type(fill_color) == str, f"fill_color should be a string"
        canvas.create_line(
            self.fpoint.x,
            self.fpoint.y,
            self.spoint.x,
            self.spoint.y,
            fill=fill_color,
            width=2,
        )
