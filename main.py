from graphics import Window, Point, Line

def main():
    window = Window(800, 600)
    window.draw_line(Line(Point(0, 0), Point(800, 600)), "white")
    window.wait_for_close()

main()