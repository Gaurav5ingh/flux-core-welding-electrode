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
        label = tk.Label(self, text="Grades", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="E81T1",
                           command=lambda: controller.show_frame(E81T1Page))
        button.pack()
        button = tk.Button(self, text="E91T1",
                           command=lambda: controller.show_frame(E91T1Page))
        button.pack()
        label = tk.Label(self, text="Mechanical Properties", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Tensile Strength",
                           command=lambda: controller.show_frame(TensilePage))
        button.pack()

        button2 = tk.Button(self, text="Ductility Strength",
                            command=lambda: controller.show_frame(DuctilityPage))
        button2.pack()
        button2 = tk.Button(self, text="CSE Strength",
                            command=lambda: controller.show_frame(CSEPage))
        button2.pack()
        button2 = tk.Button(self, text="Yield Strength",
                            command=lambda: controller.show_frame(YieldPage))
        button2.pack()


class E91T1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="E91T1", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text="The grade of electrode is decided by Tensile Strength.In E91T1,91 denotes the Tensile Strength.91 corresponds to 91000 Psi which is equivalent "
                                    "to 627 Mpa.For selection of Tensile Strength in case of E81T1 grade,we will consider range from 600-650.", font=LARGE_FONT,wraplength=320)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class E81T1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="E81T1", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text="The grade of electrode is decided by Tensile Strength.In E81T1,81 denotes the Tensile Strength.81 corresponds to 81000 Psi which is equivalent "
                                    "to 558 Mpa.For selection of Tensile Strength in case of E81T1 grade,we will consider range from 523-593.", font=LARGE_FONT,wraplength=320)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class TensilePage(tk.Frame):
    def tstrength(self,si,Nf,fe,su,d):
        labelText6 = Label(self, text="Tensile strength = ").pack()   
        ans = ((fe ** float(0.33)) * (246 + 1140 * (Nf ** float(0.5)) + 18.2 * d)) + (1 - (fe ** float(0.33))) * (720 + 3.5 * (su ** float(0.5))) + 97 * si
        Tensile=Entry(self)
        Tensile.pack()
        Tensile.delete(0, "end")
        Tensile.insert(0, ans)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        l_c = Label(self, text='Carbon in Wt%:')
        l_rec_f = Label(self, text="Ferrite recommended value in wt%:")
        l_rec_p = Label(self, text="Pearlite recommended value in wt%:")
        l_gsize = Label(self, text="Grainsize dia in ASTM:")
        l_si = Label(self, text="Silicon in Wt%:")
        l_s = Label(self, text="Sulphur in Wt%:")
        l_n = Label(self, text="Nitrogen in Ferrite:")

        e_c = Entry(self, textvariable=IntVar())
        e_rec_f = Entry(self, textvariable=IntVar())
        e_rec_p = Entry(self, textvariable=IntVar())
        e_gsize = Entry(self, textvariable=IntVar())
        e_si = Entry(self, textvariable=IntVar())
        e_s = Entry(self, textvariable=IntVar())
        e_n = Entry(self, textvariable=IntVar())


        main = Label(self, font=('25'), text="TENSILE STRENGTH", fg='BLUE')
        main.pack()
        
        l_c.pack()
        e_c.pack()
        c=float(e_c.get())
        fer=(0.8-c)/(0.78)*100

        l_rec_f.pack()
        e_rec_f.pack()
        e_rec_f.insert(0, fer)  #Entering recommended value into the entry field
        
        l_rec_p.pack()
        e_rec_p.pack()
        e_rec_p.insert(0, 100-fer) #Entering recommended value into the entry field

        l_gsize.pack()
        e_gsize.pack()
        l_si.pack()
        e_si.pack()
        l_s.pack()
        e_s.pack()
        l_n.pack()
        e_n.pack()
    
        si =float(e_si.get())
        Nf = float(e_n.get())
        fe = float(e_rec_f.get())
        su = float(e_s.get())
        d = float(e_gsize.get())
        b1 = Button(self, text="CALCULATE", command=self.tstrength(si,Nf,fe,su,d))
        b1.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class DuctilityPage(tk.Frame):
    def dstrength(self,ferrite,mangenese,nf,si):        
        pearlite = (1 - ferrite) * 100
        dus = 0.27 - 0.016 * pearlite - 0.025 * mangenese - 0.044 * si - 0.039 * 0 - 1.2 * nf
        Ductility = Entry(self,textvariable=IntVar())
        Ductility.pack()
        Ductility.delete(0, "end")
        Ductility.insert(0, dus)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        main1 = Label(self, font=('25'), text="Ductility STRENGTH CALCULATION", fg='BLUE')
        main1.pack()
        labeltext = Label(self, text="Ferrite").pack()
        num1Entry = Entry(self,textvariable=IntVar())
        num1Entry.pack()

        labeltext2 = Label(self, text="Mangenese").pack()
        num2Entry = Entry(self,textvariable=IntVar())
        num2Entry.pack()

        labeltext3 = Label(self, text="Nitrogen in Ferrite").pack()
        num3Entry = Entry(self,textvariable=IntVar())
        num3Entry.pack()

        labeltext4 = Label(self, text="Silicon").pack()
        num4Entry = Entry(self,textvariable=IntVar())
        num4Entry.pack()

        labelText5 = Label(self, text="Ductility = ").pack()
       
        ferrite = float(num1Entry.get())
        mangenese = float(num2Entry.get())
        nf = float(num3Entry.get())
        si = float(num4Entry.get())
        
        b1 = Button(self, text="CALCULATE", command=self.dstrength(ferrite,mangenese,nf,si))
        b1.pack()
     
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class CSEPage(tk.Frame):
    def CSEstrength(self,grainsize,S,Al,carbon,Zr):
        ferrite=(0.8-carbon)/(0.78)*100
        cse = 112 - 2.8 * grainsize - 0.18 * 300 - 832 * S - 43 * Al - 0.76 * (1 - ferrite) * 100 + 107 * Zr
        labelText7 = Label(self, text="CSE = ").pack()
        Cse = Entry(self)
        Cse.pack()
        Cse.delete(0,"end")
        Cse.insert(0,cse)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lab1 = Label(self, text="Grainsize dia in ASTM:")
        lab2 = Label(self, text="Sulphur in Wt%:")
        lab3 = Label(self, text="Aluminium in Wt%:")
        lab4 = Label(self, text="Carbon in Wt%:")
        lab5 = Label(self, text="Zirconium in Wt%:")

        ent1 = Entry(self, textvariable=IntVar())

        ent2 = Entry(self, textvariable=IntVar())
        ent3 = Entry(self, textvariable=IntVar())
        ent4 = Entry(self, textvariable=IntVar())
        ent5 = Entry(self, textvariable=IntVar())

        main = Label(self, font=('25'), text="CHARPY SHELF NOTCH ENERGY", fg='blue')

        grain=float(ent1.get())
        s=float(ent2.get())
        al=float(ent3.get())
        carbon=float(ent4.get())
        zr=float(ent5.get())

        ferrite=(0.8-carbon)/(0.78)*100
        per=1-ferrite
        labf=Label(self,text="Recommended value of Ferrite in Wt%:")
        entf=Entry(self, textvariable=IntVar())
        entf.insert(0,ferrite)
        labp=Label(self,text="Recommended value of Pearlite in Wt%:")
        entp=Entry(self, textvariable=IntVar())
        entp.insert(0,per)
        main.pack()
        lab4.pack()
        ent4.pack()
        labf.pack()
        entf.pack()
        labp.pack()
        entp.pack()
        lab1.pack()
        ent1.pack()
        lab2.pack()
        ent2.pack()
        lab3.pack()
        ent3.pack()

        lab5.pack()
        ent5.pack()

        b1 = Button(self, text="CALCULATE", command=self.CSEstrength(grain, s, al, carbon, zr))
        b1.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

class YieldPage(tk.Frame):
    def YLD(self,carbon,mn,grainsize,sulphur,ferrite,silicon,nf):
        ferrite=(0.8-carbon)/(0.78)*100
        pearlite=100-ferrite
        x=ferrite/100
        
        yieldst=0
        if sulphur !=0 and grainsize !=0: 
            yieldst=x**(0.33)*(35+58*(mn)+17.4*(1.0/(grainsize**(0.5))))+(1-x**0.33)*(178+3.8*(1.0/(sulphur**(0.5))))+63*(silicon)+425*nf
        Yield = Entry(self)
        Yield.pack()
        Yield.delete(0, "end")
        Yield.insert(0, yieldst)
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        l_c = Label(self,text="Carbon in Wt%:")
        l_rec_c = Label(self, text="Recommended:The range should lie within 0.05-0.07.Generally the value of carbon in Wt%\ used for tensile strength is preferred.",wraplength=500)
        l_rec_f = Label(self, text="Ferrite recommended value in Wt%:")
        l_rec_p = Label(self, text="Pearlite recommended value in Wt%:")
        l_rec_mn=Label(self,text="Mangenese recommended value:")
        l_gsize = Label(self, text="Grainsize dia in ASTM:")
        l_s = Label(self, text="Sulphur in Wt%:")
        l_si = Label(self, text="Silicon in Wt%:")
        l_nf = Label(self,text="Nitrogen in Ferrite in Wt%")
        main = Label(self, font=('25'), text="YIELD STRENGTH", fg='blue')
 
        e_c = Entry(self, textvariable=IntVar())
        e_rec_f = Entry(self, textvariable=IntVar())
        e_rec_p = Entry(self, textvariable=IntVar())
        e_rec_mn = Entry(self, textvariable=IntVar())
        e_gsize = Entry(self, textvariable=IntVar())
        e_s = Entry(self, textvariable=IntVar())
        e_si = Entry(self, textvariable=IntVar())
        e_nf = Entry(self, textvariable=IntVar())

        main.pack()

        l_c.pack(pady=10,padx=10)
        l_rec_c.pack(pady=10,padx=10)
        e_c.pack(pady=10,padx=10)
        carbon = float(e_c.get())

        l_rec_f.pack(pady=10,padx=10)
        e_rec_f.pack(pady=10,padx=10)
        fer=(0.8-carbon)/(0.78)*100
        e_rec_f.insert(0,fer)

        l_rec_p.pack(pady=10,padx=10)
        e_rec_p.pack(pady=10,padx=10)
        e_rec_p.insert(0,100-fer)

        l_rec_mn.pack(pady=10,padx=10)
        e_rec_mn.pack(pady=10,padx=10)
        mn = (0.35-carbon)*6
        e_rec_mn.insert(0,mn)

        l_gsize.pack(pady=10,padx=10)
        e_gsize.pack(pady=10,padx=10)
        
        l_s.pack(pady=10,padx=10)
        e_s.pack(pady=10,padx=10)
        
        l_si.pack()
        e_si.pack()
        
        grainsize = float(e_gsize.get())
        sulphur = float(e_s.get())
        ferrite = float(e_rec_f.get())
        silicon = float(e_si.get())
        nf = float(e_nf.get())

        labelText7 = Label(self, text="Yield strength = ").pack()
        
        bt = Button(self, text="CALCULATE", command=self.YLD(carbon,mn,grainsize,sulphur,ferrite,silicon,nf))
        bt.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

app = SeaofBTCapp()
app.mainloop()
