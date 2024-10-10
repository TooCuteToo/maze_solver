from cell import Cell
from point import Point
from window import Window
import time


class Maze:
    def __init__(
        self, maze_start_point, num_rows, num_cols, cell_size_x, cell_size_y, win
    ) -> None:
        assert isinstance(
            maze_start_point, Point
        ), f"maze_start_point should be instance of Point"
        self.maze_start_point = maze_start_point

        assert num_rows > 0, f"num_rows should be positive"
        self.num_rows = num_rows

        assert num_cols > 0, f"num_cols should be positive"
        self.num_cols = num_cols

        assert cell_size_x > 0, f"cell_size_x should be positive"
        self.cell_size_x = cell_size_x

        assert cell_size_y > 0, f"cell_size_y should be positive"
        self.cell_size_y = cell_size_y

        assert isinstance(win, Window), f"win should be instance of Window"
        self.__win = win

        self.__cells = [[] for _ in range(num_rows)]
        self._create_cells()

    def _create_cells(self) -> None:
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                cell = self._draw_cell(i, j)
                self.__cells[i].append(cell)

    def _draw_cell(self, i, j) -> Cell:
        start_point = Point(
            self.maze_start_point.x + j * self.cell_size_x,
            self.maze_start_point.y + i * self.cell_size_y,
        )

        end_point = Point(
            start_point.x + self.cell_size_x,
            start_point.y + self.cell_size_y,
        )
        cell = Cell(start_point, end_point, self.__win)
        cell.draw()
        self._animate()
        return cell

    def _animate(self) -> None:
        self.__win.redraw()
        time.sleep(0.05)
