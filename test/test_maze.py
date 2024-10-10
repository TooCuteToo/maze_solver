import unittest
from maze import Maze
from point import Point
from window import Window
import constant


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(constant.WIDTH, constant.HEIGHT)
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
