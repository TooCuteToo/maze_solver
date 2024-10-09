from window import Window
from line import Line
from point import Point


def main() -> None:
    win = Window(800, 600)
    assert isinstance(win, Window), f"win should be instance of Window"
    win.wait_for_close()


if __name__ == "__main__":
    main()
