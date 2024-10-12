from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze
import constant


def main() -> None:
    win = Window(constant.WIDTH, constant.HEIGHT)
    assert isinstance(win, Window), f"win should be instance of Window"
    maze = Maze(Point(10, 10), 10, 10, 50, 50, win)
    win.wait_for_close()


if __name__ == "__main__":
    main()
