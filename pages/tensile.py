import tkinter as tk
from tkinter import Label, Entry, IntVar, Button
import pages.start

class TensilePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.l_c = Label(self, text='Carbon in Wt%:')
        self.l_rec_f = Label(self, text="Ferrite recommended value in wt%:")
        self.l_rec_p = Label(self, text="Pearlite recommended value in wt%:")
        self.l_gsize = Label(self, text="Grainsize dia in ASTM:")
        self.l_si = Label(self, text="Silicon in Wt%:")
        self.l_s = Label(self, text="Sulphur in Wt%:")
        self.l_n = Label(self, text="Nitrogen in Ferrite:")

        self.e_c = Entry(self, textvariable=IntVar())
        self.e_rec_f = Entry(self, textvariable=IntVar())
        self.e_rec_p = Entry(self, textvariable=IntVar())
        self.e_gsize = Entry(self, textvariable=IntVar())
        self.e_si = Entry(self, textvariable=IntVar())
        self.e_s = Entry(self, textvariable=IntVar())
        self.e_n = Entry(self, textvariable=IntVar())
    
        main = Label(self, font=('25'), text="TENSILE STRENGTH",width=40, fg='BLUE', bg='lightblue')
        main.grid(row=0, column=0, columnspan=2, padx=10,pady=10)
            
        self.l_c.grid(row=1, column=0,padx=10,pady=10, sticky='e')
        self.e_c.grid(row=1, column=1)
        tk.Button(self, text="Show Recommended Values", command=self.enterRecValues).grid(row=3, column=0, columnspan=2, padx=5,pady=5)
        
        self.l_rec_f.grid(row=4, column=0,padx=10,pady=10, sticky='e')
        self.e_rec_f.grid(row=4, column=1)
        
        self.l_rec_p.grid(row=5, column=0, padx=10,pady=10, sticky='e')
        self.e_rec_p.grid(row=5, column=1)

        self.l_gsize.grid(row=6, column=0,padx=10,pady=10, sticky='e')
        self.e_gsize.grid(row=6, column=1)
        
        self.l_si.grid(row=7, column=0, padx=10,pady=10, sticky='e')
        self.e_si.grid(row=7, column=1)
        
        self.l_s.grid(row=8, column=0, padx=10,pady=10, sticky='e')
        self.e_s.grid(row=8, column=1)
        
        self.l_n.grid(row=9, column=0, padx=10,pady=10, sticky='e')
        self.e_n.grid(row=9, column=1)
        
        self.labelText5 = Label(self, text="Tensile Strength =")
        self.labelText5.grid(row=10, column=0, padx=10,pady=10, sticky='e')
        self.Tensile=Entry(self)
        self.Tensile.grid(row=10, column=1)

        b1 = Button(self, text="CALCULATE", command=self.textEntries)
        b1.grid(row=11, column=0, columnspan=2, padx=10,pady=10)
        
        button1 = tk.Button(self, text="Back to Home",
                        command=lambda: controller.show_frame(pages.start.StartPage))
        button1.grid(row=12, column=0, columnspan=2, padx=10,pady=10)

    def enterRecValues(self):
        carbon=float(self.e_c.get())
        ferrite=(0.8-carbon)/(0.78)*100
        
        self.e_rec_f.delete(0,"end")
        self.e_rec_f.insert(0, ferrite)  #Entering recommended value into the self.entry field
        
        self.e_rec_p.delete(0,"end")
        self.e_rec_p.insert(0, 100-ferrite) #Entering recommended value into the self.entry field

    def textEntries(self):
        c=float(self.e_c.get())
        fer=(0.8-c)/(0.78)*100
        si =float(self.e_si.get())
        Nf = float(self.e_n.get())
        fe = float(self.e_rec_f.get())
        su = float(self.e_s.get())
        d = float(self.e_gsize.get())
        
        ans = ((fe ** float(0.33)) * (246 + 1140 * (Nf ** float(0.5)) + 18.2 * d)) + (1 - (fe ** float(0.33))) * (720 + 3.5 * (su ** float(0.5))) + 97 * si
        self.Tensile.delete(0,"end")
        self.Tensile.insert(0, ans)
