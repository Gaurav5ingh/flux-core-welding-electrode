class DuctilityPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        main1 = Label(self, font=('25'), text="DUCTILITY STRENGTH", fg='BLUE')
        main1.pack(padx=10,pady=10)
        self.labeltext = Label(self, text="Ferrite").pack()
        self.num1Entry = Entry(self,textvariable=IntVar())
        self.num1Entry.pack(padx=10,pady=10)

        self.labeltext2 = Label(self, text="Mangenese").pack()
        self.num2Entry = Entry(self,textvariable=IntVar())
        self.num2Entry.pack(padx=10,pady=10)

        self.labeltext3 = Label(self, text="Nitrogen in Ferrite").pack()
        self.num3Entry = Entry(self,textvariable=IntVar())
        self.num3Entry.pack(padx=10,pady=10)

        self.labeltext4 = Label(self, text="Silicon").pack()
        self.num4Entry = Entry(self,textvariable=IntVar())
        self.num4Entry.pack(padx=10,pady=10)

        self.labelText5 = Label(self, text="Ductility = ").pack()
        self.Ductility = Entry(self)
        self.Ductility.pack(padx=10,pady=10)           
        
        b1 = Button(self, text="CALCULATE", command=self.textEntries)
        b1.pack(padx=10,pady=10)
  
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(padx=10,pady=10)

    def textEntries(self):
        ferrite = float(self.num1Entry.get())
        mangenese = float(self.num2Entry.get())
        nf = float(self.num3Entry.get())
        si = float(self.num4Entry.get())
        
        pearlite = (1 - ferrite) * 100
        dus = 0.27 - 0.016 * pearlite - 0.025 * mangenese - 0.044 * si - 0.039 * 0 - 1.2 * nf
        
        self.Ductility.delete(0,"end") 
        self.Ductility.insert(0, dus)
