from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title("MazeSolver Py")
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.window_is_running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.window_is_running = True
        while self.window_is_running:
            self.redraw()

    def close(self) -> None:
        self.window_is_running = False

    def draw_line(self, line: 'Line', fill_color: str) -> None:
        line.draw(self.canvas, fill_color)

class Point():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
class Line():
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end
    
    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)