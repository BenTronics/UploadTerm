from terminal import Terminal
import tkinter

fenster = tkinter.Tk()
terminal_frame = tkinter.Frame(fenster)
terminal = Terminal(terminal_frame)
terminal_frame.pack()

while True:
    fenster.update()
    terminal.update()
