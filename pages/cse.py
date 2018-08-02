import tkinter as tk
from tkinter import Label, Entry, IntVar, Button
import pages.start

class CSEPage(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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

        main = Label(self, font=('25'), text="CHARPY SHELF NOTCH ENERGY(CSE)", fg='blue')

        self.labf=Label(self,text="Recommended value of Ferrite in Wt%:")
        self.entf=Entry(self, textvariable=IntVar())
        
        self.labp=Label(self,text="Recommended value of Pearlite in Wt%:")
        self.entp=Entry(self, textvariable=IntVar())
        
        main.pack(padx=10,pady=10)
        self.lab4.pack()
        self.ent4.pack(padx=10,pady=10)
        self.labelText = Label(self, text="Click 'Enter' to show Recommended Values")
        self.labelText.pack(padx=10,pady=10)
        tk.Button(self, text="Enter", command=self.enterRecValues).pack(padx=5,pady=5)

        self.labf.pack()
        self.entf.pack(padx=10,pady=10)

        self.labp.pack()
        self.entp.pack(padx=10,pady=10)

        self.lab1.pack()
        self.ent1.pack(padx=10,pady=10)

        self.lab2.pack()
        self.ent2.pack(padx=10,pady=10)

        self.lab3.pack()
        self.ent3.pack(padx=10,pady=10)

        self.lab5.pack()
        self.ent5.pack(padx=10,pady=10)
         
        self.labelText5 = Label(self, text="CSE = ")
        self.labelText5.pack(padx=10,pady=10)
        
        self.Cse = Entry(self)
        self.Cse.pack()
        
        b1 = Button(self, text="CALCULATE", command=self.textEntries)
        b1.pack(padx=10,pady=10)
        
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(pages.start.StartPage))
        button1.pack(padx=10,pady=10)

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
        self.labelText.pack()
        
        self.Cse.delete(0,"end") 
        self.Cse.insert(0,cse)
