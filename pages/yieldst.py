import tkinter as tk
from tkinter import Label, Entry, IntVar, Button
import pages.start

class YieldPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.l_c = Label(self,text="Carbon in Wt%:")
        self.l_rec_c = Label(self, text="Recommended:The range should lie within 0.05-0.07.",wraplength=500)
        self.l_rec_f = Label(self, text="Ferrite recommended value in Wt%:")
        self.l_rec_p = Label(self, text="Pearlite recommended value in Wt%:")
        self.l_rec_mn=Label(self,text="Mangenese recommended value:")
        self.l_gsize = Label(self, text="Grainsize dia in ASTM:")
        self.l_s = Label(self, text="Sulphur in Wt%:")
        self.l_si = Label(self, text="Silicon in Wt%:")
        self.l_nf = Label(self,text="Nitrogen in Ferrite in Wt%")
        main = Label(self, font=('25'), text="YIELD STRENGTH", fg='blue', bg='lightblue')

        self.e_c = Entry(self, textvariable=IntVar())
        self.e_rec_f = Entry(self, textvariable=IntVar())
        self.e_rec_p = Entry(self, textvariable=IntVar())
        self.e_rec_mn = Entry(self, textvariable=IntVar())
        self.e_gsize = Entry(self, textvariable=IntVar())
        self.e_s = Entry(self, textvariable=IntVar())
        self.e_si = Entry(self, textvariable=IntVar())
        self.e_nf = Entry(self, textvariable=IntVar())

        main.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')

        self.l_c.grid(row=2, column=0, sticky='e')
        self.l_rec_c.grid(row=1, column=0, columnspan=2)
        self.e_c.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        
        tk.Button(self, text="Show Recommended Values", command=self.enterRecValues) \
            .grid(row=4, column=0, columnspan=2, padx=5,pady=5)

        self.l_rec_f.grid(row=5, column=0, sticky='e')
        self.e_rec_f.grid(row=5, column=1, padx=5, pady=5, sticky='w')

        self.l_rec_p.grid(row=6, column=0, sticky='e')
        self.e_rec_p.grid(row=6, column=1, padx=5, pady=5, sticky='w')

        self.l_rec_mn.grid(row=7, column=0, sticky='e')
        self.e_rec_mn.grid(row=7, column=1, padx=5, pady=5, sticky='w')        

        self.l_gsize.grid(row=8, column=0, sticky='e')
        self.e_gsize.grid(row=8, column=1, padx=5, pady=5, sticky='w')

        self.l_s.grid(row=9, column=0, sticky='e')
        self.e_s.grid(row=9, column=1, padx=5, pady=5, sticky='w')

        self.l_si.grid(row=10, column=0, sticky='e')
        self.e_si.grid(row=10, column=1, padx=5, pady=5, sticky='w')

        self.l_nf.grid(row=11, column=0, sticky='e')
        self.e_nf.grid(row=11, column=1, padx=5, pady=5, sticky='w')

        self.labelText = Label(self, text="Yield strength =")
        self.labelText.grid(row=12, column=0, sticky='e')

        self.Yield = Entry(self)
        self.Yield.grid(row=12, column=1, padx=5, pady=5, sticky='w')
        
        bt = Button(self, text="CALCULATE", command=self.textEntries)
        bt.grid(row=13, column=0, columnspan=2, padx=10, pady=10)

        button1 = tk.Button(self, text="Back to Home",
                    command=lambda: controller.show_frame(pages.start.StartPage))
        button1.grid(row=14, column=0, columnspan=2, padx=10, pady=10)

    def enterRecValues(self):          # shows recommended amounts on the basis of carbon content entered by the user
        carbon = float(self.e_c.get())
        ferrite=(0.8-carbon)/(0.78)*100

        self.e_rec_f.delete(0,"end")  # clears previous value(if any) from the bar
        self.e_rec_f.insert(0,ferrite)# inserts new value

        mn = (0.35-carbon)*6

        self.e_rec_mn.delete(0,"end")
        self.e_rec_mn.insert(0,mn)

        self.e_rec_p.delete(0,"end")
        self.e_rec_p.insert(0,100-ferrite)
    
    def textEntries(self):              # takes the values entered by the user
        carbon = float(self.e_c.get())
        ferrite=(0.8-carbon)/(0.78)*100
        mn = (0.35-carbon)*6
        grainsize=float(self.e_gsize.get())
        sulphur=float(self.e_s.get())
        silicon=float(self.e_si.get())
        nf=float(self.e_nf.get())

        pearlite=100-ferrite
        x=ferrite/100

        result = None
        try:
            yieldst=x**(0.33)*(35+58*(mn)+17.4*(1.0/(grainsize**(0.5))))+(1-x**0.33)*(178+3.8*(1.0/(sulphur**(0.5))))+63*(silicon)+425*nf
        except ZeroDivisionError:
            result = 'div by 0 exception!'
        else:
            result = yieldst
        
        self.Yield.delete(0,"end") 
        self.Yield.insert(0, result)
    
    #def check_entry(
