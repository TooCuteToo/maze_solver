from cell import Cell
from point import Point
from window import Window
import time
import random


class Maze:
    def __init__(
        self,
        maze_start_point,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed=None,
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

        self._cells = [[] for _ in range(num_rows)]
        self._create_cells()
        self._break_entrance_and_exit()

        if seed is not None:
            random.seed(seed)

        self._break_walls_r(0, 0)

    def _create_cells(self) -> None:
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                cell = self._create_cell(i, j)
                self._cells[i].append(cell)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _create_cell(self, i, j) -> Cell:
        start_point = Point(
            self.maze_start_point.x + j * self.cell_size_x,
            self.maze_start_point.y + i * self.cell_size_y,
        )

        end_point = Point(
            start_point.x + self.cell_size_x,
            start_point.y + self.cell_size_y,
        )

        cell = Cell(start_point, end_point, self.__win)
        return cell

    def _break_entrance_and_exit(self):
        # start cell
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        # end cell
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)

    def _draw_cell(self, i, j) -> None:
        self._cells[i][j].draw()
        self._animate()

    def _animate(self) -> None:
        self.__win.redraw()
        time.sleep(0.05)

    def _break_walls_r(self, i, j) -> None:
        self._cells[i][j].visited = True

        # Define the possible directions: up, down, left, right to check the adjecent
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while True:
            indexes = []
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni < self.num_rows and 0 <= nj < self.num_cols
                ):  # Check boundaries
                    if not self._cells[ni][nj].visited:
                        indexes.append([ni, nj])

            if len(indexes) == 0:
                self._draw_cell(i, j)
                return

            current_idx = [i, j]
            next_idx = random.choice(indexes)

            self._break_wall(current_idx, next_idx)
            self._break_walls_r(next_idx[0], next_idx[1])

    def _break_wall(self, current_idx, next_idx) -> None:
        print(f"current idx: {current_idx} -- next idx: {next_idx}")
        if current_idx[0] > next_idx[0]:
            self._cells[current_idx[0]][current_idx[1]].has_top_wall = False
            self._cells[next_idx[0]][next_idx[1]].has_bottom_wall = False

        if current_idx[0] < next_idx[0]:
            self._cells[current_idx[0]][current_idx[1]].has_bottom_wall = False
            self._cells[next_idx[0]][next_idx[1]].has_top_wall = False

        if current_idx[1] > next_idx[1]:
            self._cells[current_idx[0]][current_idx[1]].has_left_wall = False
            self._cells[next_idx[0]][next_idx[1]].has_right_wall = False

        if current_idx[1] < next_idx[1]:
            self._cells[current_idx[0]][current_idx[1]].has_right_wall = False
            self._cells[next_idx[0]][next_idx[1]].has_left_wall = False
