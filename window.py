from tkinter import Tk, BOTH, Canvas
from line import Line


class Window:
    def __init__(self, width=800, height=600) -> None:
        assert width > 0, f"width should be positve number"
        assert height > 0, f"height should be positve number"
        self.width = width
        self.height = height

        # init root widget
        self.__root = Tk()
        self.__root.minsize(self.width, self.height)
        self.__root.wm_title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        # init canvas widget
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack()

        # tracking window is running
        self.isrunning = False

    def redraw(self) -> None:
        assert self.__root != None, f"self.__root should not be None"
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        assert self.isrunning != None, f"self.isrunning should not be None"
        self.isrunning = True

        while self.isrunning:
            self.redraw()

    def close(self) -> None:
        assert self.isrunning != None, f"self.isrunning should not be None"
        self.isrunning = False

    def draw_line(self, line, fill_color) -> None:
        assert isinstance(line, Line), f"line should be a instance of Line"
        assert type(fill_color) == str, f"fill_color should be a string"
        line.draw(self.__canvas, fill_color)
