import tkinter as tk
from tkinter import Label, Entry, IntVar, Button
import pages.start

class CSEPage(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.lab1 = Label(self, text="Grainsize dia in ASTM:")
        self.lab2 = Label(self, text="Sulphur in Wt%:")
        self.lab3 = Label(self, text="Aluminium in Wt%:")
        self.lab4 = Label(self, text="Carbon in Wt%:")
        self.lab5 = Label(self, text="Zirconium in Wt%:")

        self.ent1 = Entry(self, textvariable=IntVar())
        self.ent2 = Entry(self, textvariable=IntVar())
        self.ent3 = Entry(self, textvariable=IntVar())
        self.ent4 = Entry(self, textvariable=IntVar())
        self.ent5 = Entry(self, textvariable=IntVar())

        main = Label(self, font=('25'), text="CHARPY SHELF NOTCH ENERGY(CSE)", fg='blue', bg='lightblue')

        self.labf=Label(self,text="Recommended value of Ferrite in Wt%:")
        self.entf=Entry(self, textvariable=IntVar())
        
        self.labp=Label(self,text="Recommended value of Pearlite in Wt%:")
        self.entp=Entry(self, textvariable=IntVar())
        
        main.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
        self.lab4.grid(row=1, column=0, sticky='e')
        self.ent4.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        tk.Button(self, text="Show Recommended Values", command=self.enterRecValues).grid(row=3, column=0, columnspan=2, padx=5,pady=5)

        self.labf.grid(row=4, column=0, sticky='e')
        self.entf.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        self.labp.grid(row=5, column=0, sticky='e')
        self.entp.grid(row=5, column=1, padx=5, pady=5, sticky='w')

        self.lab1.grid(row=6, column=0, sticky='e')
        self.ent1.grid(row=6, column=1, padx=5, pady=5, sticky='w')

        self.lab2.grid(row=7, column=0, sticky='e')
        self.ent2.grid(row=7, column=1, padx=5, pady=5, sticky='w')

        self.lab3.grid(row=8, column=0, sticky='e')
        self.ent3.grid(row=8, column=1, padx=5, pady=5, sticky='w')

        self.lab5.grid(row=9, column=0, sticky='e')
        self.ent5.grid(row=9, column=1, padx=5, pady=5, sticky='w')
         
        self.labelText5 = Label(self, text="CSE =")
        self.labelText5.grid(row=10, column=0, sticky='e')
        
        self.Cse = Entry(self)
        self.Cse.grid(row=10, column=1, padx=5, pady=5, sticky='w')
        
        b1 = Button(self, text="CALCULATE", command=self.textEntries)
        b1.grid(row=11, column=0, columnspan=2, padx=10,pady=10)
        
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(pages.start.StartPage))
        button1.grid(row=12, column=0, columnspan=2, padx=10,pady=10)

    def enterRecValues(self):
        carbon=float(self.ent4.get())
        ferrite=(0.8-carbon)/(0.78)*100
        per=100-ferrite
     
        self.entf.delete(0,"end") 
        self.entf.insert(0,ferrite)
        
        self.entp.delete(0,"end")
        self.entp.insert(0,per)
    
    def textEntries(self):
        grainsize=float(self.ent1.get())
        s=float(self.ent2.get())
        al=float(self.ent3.get())
        carbon=float(self.ent4.get())
        zr=float(self.ent5.get())

        ferrite=(0.8-carbon)/(0.78)*100
        per=1-ferrite
        
        cse = 112 - 2.8 * grainsize - 0.18 * 300 - 832 * s - 43 * al - 0.76 * (1 - ferrite) * 100 + 107 * zr
        self.labelText = Label(self, text="CSE = ")
        self.labelText.grid(row=13, column=0)
        
        self.Cse.delete(0,"end") 
        self.Cse.insert(0,cse)
