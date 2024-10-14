from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze
import constant


def main() -> None:
    win = Window(constant.WIDTH, constant.HEIGHT)
    assert isinstance(win, Window), f"win should be instance of Window"
    maze = Maze(Point(20, 20), 25, 25, 30, 30, win, 10)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
