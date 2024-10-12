from window import Window
from point import Point
from line import Line
import constant


class Cell:
    def __init__(self, fpoint, spoint, win) -> None:
        assert isinstance(fpoint, Point), f"fpoint should be instance of Point"
        assert isinstance(spoint, Point), f"spoint should be instance of Point"

        # init x1, y1
        self.__x1 = fpoint.x
        self.__y1 = fpoint.y

        # init x2, y2
        self.__x2 = spoint.x
        self.__y2 = spoint.y

        assert isinstance(win, Window), f"window should be instance of Window"
        self.__win = win

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self) -> None:
        assert self.__win != None, f"self.__win should not be None"

        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line, constant.CELL_COLOR)
        else:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line, constant.CELL_REMOVE_COLOR)

        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, constant.CELL_COLOR)
        else:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, constant.CELL_REMOVE_COLOR)

        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line, constant.CELL_COLOR)
        else:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line, constant.CELL_REMOVE_COLOR)

        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, constant.CELL_COLOR)
        else:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, constant.CELL_REMOVE_COLOR)

    def draw_move(self, to_cell, undo=False) -> None:
        assert isinstance(to_cell, Cell), f"to_cell should be instance of Cell"
        assert type(undo) == bool, f"undo should be boolean"
        if not undo:
            # center point of current cell
            fpoint = self.calculate_center()

            # center point of to cell
            spoint = to_cell.calculate_center()

            line = Line(Point(fpoint.x, fpoint.y), Point(spoint.x, spoint.y))
            self.__win.draw_line(line, constant.CELL_MOVE_COLOR)

    def calculate_center(self) -> Point:
        x = (self.__x1 + self.__x2) / 2
        y = (self.__y1 + self.__y2) / 2
        return Point(x, y)
