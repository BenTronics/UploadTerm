from terminal import Terminal
from uploader import Uploader
import tkinter

fenster = tkinter.Tk()
terminal_frame = tkinter.Frame(fenster)
uploader_frame = tkinter.Frame(fenster)
terminal = Terminal(terminal_frame)
uploader = Uploader(uploader_frame)
terminal_frame.pack(side = "left")
uploader_frame.pack(side = "right")

while True:
    fenster.update()
    terminal.update()
