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
        # self.resizable(False, False)
        self.container = tk.Frame(self)
        # canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        # frame = tk.Frame(canvas, background="#ffffff")
        #container.pack(side="top", fill="both", expand=True)
        self.container.grid(row=0, column=0, columnspan=2, sticky='nswe')
        self.container.grid_propagate(True)

        # self.container.grid_rowconfigure(0, weight=1)
        # self.container.columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)

        self.frames = {}

        for F in (pages.start.StartPage,
                    pages.tensile.TensilePage,
                    pages.ductility.DuctilityPage,
                    pages.e81t1.E81T1Page,
                    pages.e91t1.E91T1Page,
                    pages.cse.CSEPage,
                    pages.yieldst.YieldPage):
            
            frame = F(parent=self.container, controller=self)

            self.frames[F] = frame
            # frame.columnconfigure(0, weight=1)
            # frame.grid_columnconfigure(0, weight=1)

            frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.show_frame(pages.start.StartPage)



    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
