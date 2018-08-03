import tkinter as tk
from pages import LARGE_FONT
import pages.start

class E81T1Page(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="E81T1", font=LARGE_FONT)
        self.label.grid(row=0, column=0, pady=10, padx=10)
        self.label = tk.Label(self, text="The grade of electrode is decided by Tensile Strength.In E81T1,81 denotes the Tensile Strength.81 corresponds to 81000 Psi which is equivalself.ent "
                                    "to 558 Mpa.For selection of Tensile Strength in case of E81T1 grade,we will consider range from 523-593.", font=LARGE_FONT,wraplength=320)
        self.label.grid(row=1, column=0, pady=10, padx=10)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(pages.start.StartPage))
        button1.grid(row=2, column=0)
