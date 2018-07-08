class E91T1Page(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="E91T1", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)
        self.label = tk.Label(self, text="The grade of electrode is decided by Tensile Strength.In E91T1,91 denotes the Tensile Strength.91 corresponds to 91000 Psi which is equivalself.ent "
                                    "to 627 Mpa.For selection of Tensile Strength in case of E81T1 grade,we will consider range from 600-650.", font=LARGE_FONT,wraplength=320)
        self.label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
