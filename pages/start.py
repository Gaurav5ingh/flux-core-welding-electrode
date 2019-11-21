import tkinter as tk
from pages import LARGE_FONT

import pages.tensile
import pages.ductility
import pages.e81t1
import pages.e91t1
import pages.cse
import pages.yieldst

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        buttonwidth = 15
        tk.Frame.__init__(self, parent, relief=tk.RAISED, bd=5)

        # self.grid_propagate(True)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.label = tk.Label(self, text="Grades", font=LARGE_FONT, bg='lightblue')
        self.label.grid(row=0, column=0, columnspan=2, sticky='we')
        
        button = tk.Button(self, text="E81T1", width=buttonwidth,
                           command=lambda: controller.show_frame(pages.e81t1.E81T1Page))
        button.grid(row=1, column=0, padx=10,pady=10)
        button = tk.Button(self, text="E91T1", width=buttonwidth,
                           command=lambda: controller.show_frame(pages.e91t1.E91T1Page))
        button.grid(row=1, column=1, padx=10,pady=10)

        self.label = tk.Label(self, text="Mechanical Properties", font=LARGE_FONT, bg='lightblue')
        self.label.grid(row=3, column=0, columnspan=2, sticky='nswe')
        button = tk.Button(self, text="Tensile Strength", width=buttonwidth,
                           command=lambda: controller.show_frame(pages.tensile.TensilePage))
        button.grid(row=4, column=0, columnspan=2, padx=10,pady=10)

        button2 = tk.Button(self, text="Ductility Strength", width=buttonwidth,
                            command=lambda: controller.show_frame(pages.ductility.DuctilityPage))
        button2.grid(row=5, column=0, columnspan=2, padx=10,pady=10)
        button2 = tk.Button(self, text="CSE Strength", width=buttonwidth,
                            command=lambda: controller.show_frame(pages.cse.CSEPage))
        button2.grid(row=6, column=0, columnspan=2, padx=10,pady=10)
        button2 = tk.Button(self, text="Yield Strength", width=buttonwidth,
                            command=lambda: controller.show_frame(pages.yieldst.YieldPage))
        button2.grid(row=7, column=0, columnspan=2, padx=10,pady=10)
