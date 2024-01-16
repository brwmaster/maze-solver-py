from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.title = "MazeSolver Py"
        self.canvas = Canvas(width=self.width, height=self.height)
        self.canvas.pack()
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
    