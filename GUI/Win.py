from tkinter import *


class Win:
    def __init__(self, title="Video Editor", resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.resizable(resizable[0], resizable[1])
