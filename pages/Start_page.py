class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Grades", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)
        button = tk.Button(self, text="E81T1",
                           command=lambda: controller.show_frame(E81T1Page))
        button.pack(padx=10,pady=10)
        button = tk.Button(self, text="E91T1",
                           command=lambda: controller.show_frame(E91T1Page))
        button.pack(padx=10,pady=10)
        self.label = tk.Label(self, text="Mechanical Properties", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Tensile Strength",
                           command=lambda: controller.show_frame(TensilePage))
        button.pack(padx=10,pady=10)

        button2 = tk.Button(self, text="Ductility Strength",
                            command=lambda: controller.show_frame(DuctilityPage))
        button2.pack(padx=10,pady=10)
        button2 = tk.Button(self, text="CSE Strength",
                            command=lambda: controller.show_frame(CSEPage))
        button2.pack(padx=10,pady=10)
        button2 = tk.Button(self, text="Yield Strength",
                            command=lambda: controller.show_frame(YieldPage))
        button2.pack(padx=10,pady=10)
