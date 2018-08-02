import tkinter as tk

import pages.start
import pages.tensile
import pages.ductility
import pages.e81t1
import pages.e91t1
import pages.cse
import pages.yieldst

class PageController(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        frame = tk.Frame(canvas, background="#ffffff")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (pages.start.StartPage,
                    pages.tensile.TensilePage,
                    pages.ductility.DuctilityPage,
                    pages.e81t1.E81T1Page,
                    pages.e91t1.E91T1Page,
                    pages.cse.CSEPage,
                    pages.yieldst.YieldPage):
            
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(pages.start.StartPage)



    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
