from window import Window
from line import Line
from point import Point
from cell import Cell
import constant


def main() -> None:
    win = Window(constant.WIDTH, constant.HEIGHT)
    assert isinstance(win, Window), f"win should be instance of Window"

    cell1 = Cell(Point(10, 10), Point(50, 50), win)
    cell2 = Cell(Point(50, 10), Point(90, 50), win)
    cell3 = Cell(Point(90, 10), Point(130, 50), win)

    cell1.draw()
    cell2.draw()
    cell3.draw()

    # cell1.draw_move(cell2)
    # cell2.draw_move(cell3)
    cell1.draw_move(cell3)

    win.wait_for_close()


if __name__ == "__main__":
    main()
