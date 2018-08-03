import tkinter as tk
import pages.start

class DuctilityPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
    
        main1 = tk.Label(self, font=('25'), text="DUCTILITY STRENGTH", fg='BLUE', bg='lightblue')
        main1.grid(row=0, column=0, columnspan=2, pady=10, sticky='nwe')
        self.labeltext = tk.Label(self, text="Ferrite:")
        self.labeltext.grid(row=1, column=0, sticky='e')
        self.num1Entry = tk.Entry(self,textvariable=tk.IntVar())
        self.num1Entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        self.labeltext2 = tk.Label(self, text="Mangenese:")
        self.labeltext2.grid(row=2, column=0, sticky='e')
        self.num2Entry = tk.Entry(self,textvariable=tk.IntVar())
        self.num2Entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        self.labeltext3 = tk.Label(self, text="Nitrogen in Ferrite:")
        self.labeltext3.grid(row=3, column=0, sticky='e')
        self.num3Entry = tk.Entry(self,textvariable=tk.IntVar())
        self.num3Entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        self.labeltext4 = tk.Label(self, text="Silicon:")
        self.labeltext4.grid(row=4, column=0, sticky='e')
        self.num4Entry = tk.Entry(self,textvariable=tk.IntVar())
        self.num4Entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        self.labelText5 = tk.Label(self, text="Ductility =")
        self.labelText5.grid(row=5, column=0, sticky='e')
        self.Ductility = tk.Entry(self)
        self.Ductility.grid(row=5, column=1, padx=5, pady=5, sticky='w')           
        
        b1 = tk.Button(self, text="CALCULATE", command=self.textEntries)
        b1.grid(row=6, column=0, columnspan=2, padx=10,pady=10)
  
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(pages.start.StartPage))
        button1.grid(row=7, column=0, columnspan=2, padx=10,pady=10)

    def textEntries(self):
        ferrite = float(self.num1Entry.get())
        mangenese = float(self.num2Entry.get())
        nf = float(self.num3Entry.get())
        si = float(self.num4Entry.get())
        
        pearlite = (1 - ferrite) * 100
        dus = 0.27 - 0.016 * pearlite - 0.025 * mangenese - 0.044 * si - 0.039 * 0 - 1.2 * nf
        
        self.Ductility.delete(0,"end") 
        self.Ductility.insert(0, dus)
