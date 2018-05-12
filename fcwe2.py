import tkinter as tk
from tkinter import *
from tkinter import  ttk
LARGE_FONT = ("Verdana", 12)



class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        frame = tk.Frame(canvas, background="#ffffff")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, TensilePage, DuctilityPage,E81T1Page,E91T1Page,CSEPage,YieldPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)



    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


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


class E81T1Page(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="E81T1", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)
        self.label = tk.Label(self, text="The grade of electrode is decided by Tensile Strength.In E81T1,81 denotes the Tensile Strength.81 corresponds to 81000 Psi which is equivalself.ent "
                                    "to 558 Mpa.For selection of Tensile Strength in case of E81T1 grade,we will consider range from 523-593.", font=LARGE_FONT,wraplength=320)
        self.label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


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
    
        main = Label(self, font=('25'), text="TENSILE STRENGTH", fg='BLUE')
        main.pack(padx=10,pady=10)
            
        self.l_c.pack(padx=10,pady=10)
        self.e_c.pack()
        self.labelText = Label(self, text="Click 'Enter' to show Recommended Values").pack(padx=10,pady=10)
        tk.Button(self, text="Enter", command=self.enterRecValues).pack(padx=5,pady=5)
        
        self.l_rec_f.pack(padx=10,pady=10)
        self.e_rec_f.pack()
        
        self.l_rec_p.pack(padx=10,pady=10)
        self.e_rec_p.pack()

        self.l_gsize.pack(padx=10,pady=10)
        self.e_gsize.pack()
        
        self.l_si.pack(padx=10,pady=10)
        self.e_si.pack()
        
        self.l_s.pack(padx=10,pady=10)
        self.e_s.pack()
        
        self.l_n.pack(padx=10,pady=10)
        self.e_n.pack()
        
        self.labelText5 = Label(self, text="Tensile Strength = ").pack(padx=10,pady=10)    
        self.Tensile=Entry(self)
        self.Tensile.pack()

        b1 = Button(self, text="CALCULATE", command=self.textEntries)
        b1.pack(padx=10,pady=10)
        
        button1 = tk.Button(self, text="Back to Home",
                        command=lambda: controller.show_frame(StartPage))
        button1.pack(padx=10,pady=10)

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
        self.labelText = Label(self, text="Click 'Enter' to show Recommended Values").pack(padx=10,pady=10)
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
         
        self.labelText5 = Label(self, text="CSE = ").pack(padx=10,pady=10)
        
        self.Cse = Entry(self)
        self.Cse.pack()
        
        b1 = Button(self, text="CALCULATE", command=self.textEntries)
        b1.pack(padx=10,pady=10)
        
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
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
        self.labelText = Label(self, text="CSE = ").pack()
        
        self.Cse.delete(0,"end") 
        self.Cse.insert(0,cse)

class YieldPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.l_c = Label(self,text="Carbon in Wt%:")
        self.l_rec_c = Label(self, text="Recommended:The range should lie within 0.05-0.07.",wraplength=500)
        self.l_rec_f = Label(self, text="Ferrite recommended value in Wt%:")
        self.l_rec_p = Label(self, text="Pearlite recommended value in Wt%:")
        self.l_rec_mn=Label(self,text="Mangenese recommended value:")
        self.l_gsize = Label(self, text="Grainsize dia in ASTM:")
        self.l_s = Label(self, text="Sulphur in Wt%:")
        self.l_si = Label(self, text="Silicon in Wt%:")
        self.l_nf = Label(self,text="Nitrogen in Ferrite in Wt%")
        main = Label(self, font=('25'), text="YIELD STRENGTH", fg='blue')

        self.e_c = Entry(self, textvariable=IntVar())
        self.e_rec_f = Entry(self, textvariable=IntVar())
        self.e_rec_p = Entry(self, textvariable=IntVar())
        self.e_rec_mn = Entry(self, textvariable=IntVar())
        self.e_gsize = Entry(self, textvariable=IntVar())
        self.e_s = Entry(self, textvariable=IntVar())
        self.e_si = Entry(self, textvariable=IntVar())
        self.e_nf = Entry(self, textvariable=IntVar())

        main.pack(padx=10,pady=10)

        self.l_c.pack()
        self.l_rec_c.pack()
        self.e_c.pack(padx=10,pady=10)
        
        self.labelText = Label(self, text="Click 'Enter' to show Recommended Values").pack(padx=10,pady=10)
        tk.Button(self, text="Enter", command=self.enterRecValues).pack(padx=5,pady=5)

        self.l_rec_f.pack()
        self.e_rec_f.pack(padx=10,pady=10)

        self.l_rec_p.pack()
        self.e_rec_p.pack(padx=10,pady=10)

        self.l_rec_mn.pack()
        self.e_rec_mn.pack(padx=10,pady=10)        

        self.l_gsize.pack()
        self.e_gsize.pack(padx=10,pady=10)

        self.l_s.pack()
        self.e_s.pack(padx=10,pady=10)

        self.l_si.pack()
        self.e_si.pack(padx=10,pady=10)

        self.l_nf.pack()
        self.e_nf.pack(padx=10,pady=10)

        self.labelText = Label(self, text="Yield strength = ").pack(padx=10,pady=10)

        self.Yield = Entry(self)
        self.Yield.pack()
        
        bt = Button(self, text="CALCULATE", command=self.textEntries)
        bt.pack()

        button1 = tk.Button(self, text="Back to Home",
                    command=lambda: controller.show_frame(StartPage))
        button1.pack()

    def enterRecValues(self):
        carbon = float(self.e_c.get())
        ferrite=(0.8-carbon)/(0.78)*100

        self.e_rec_f.delete(0,"end")
        self.e_rec_f.insert(0,ferrite)

        mn = (0.35-carbon)*6

        self.e_rec_mn.delete(0,"end")
        self.e_rec_mn.insert(0,mn)

        self.e_rec_p.delete(0,"end")
        self.e_rec_p.insert(0,100-ferrite)

    def textEntries(self):
        carbon = float(self.e_c.get())
        ferrite=(0.8-carbon)/(0.78)*100
        mn = (0.35-carbon)*6
        grainsize=float(self.e_gsize.get())
        sulphur=float(self.e_s.get())
        silicon=float(self.e_si.get())
        nf=float(self.e_nf.get())

        pearlite=100-ferrite
        x=ferrite/100

        yieldst=x**(0.33)*(35+58*(mn)+17.4*(1.0/(grainsize**(0.5))))+(1-x**0.33)*(178+3.8*(1.0/(sulphur**(0.5))))+63*(silicon)+425*nf
        self.Yield.delete(0,"end") 
        self.Yield.insert(0, yieldst)


if __name__ == '__main__':
    app = SeaofBTCapp()
    app.mainloop()
