from tkinter import *

class Kanvas:
    def __init__(self, raiz):
        self.canvas1 = Canvas(raiz, width=400, height=400, cursor='fleur',bd=10, bg='red')
        xy = 20, 20, 300, 180
        self.canvas1.create_arc(xy, start=0, extent=270, fill='red')
        self.canvas1.create_arc(xy, start=279, extent=60, fill='blue')
        self.canvas1.create_arc(200,300,text='GRÁFICO', font=('Arial','26','bold'))
        self.canvas1.pack()
        self.frame=Frame(instancia)
        self.frame.pack()
        self.label.pack()

instancia = Tk()
Kanvas(instancia)
instancia.mainloop()
