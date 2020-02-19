from tkinter import *
import random
import time;
import datetime
from ResizingCanvas import ResizingCanvas

def main():
    root = Tk()
    root.title('Sistema de vendas')
    janela = Frame(root)
    janela.pack(fill=BOTH, expand=YES)

    janela_canvas = ResizingCanvas(janela, width=1350, height=750, bg='blue', highlightthickness=0 )
    janela_canvas.pack(fill=BOTH, expand=YES)



    janela_canvas.addtag_all("all")
    root.mainloop()

if __name__ == "__main__":
    main()


# janela = Tk()
# janela.geometry("1350x750+0+0")
# janela.title("SISTEMA DE VENDAS")
# janela.configure(background='blue')


# menu_topo = Frame (janela, width=1350, height=100, bd=8, relief="raise")
# menu_topo.pack(side=TOP, expand=True)

# menu_esquerda = Frame (janela, width=900, height=650, bd=8, relief="raise")
# menu_esquerda.pack(side=LEFT, expand=YES, fill=BOTH)

# menu_direita = Frame (janela, width=440, height=650, bd=8, relief="raise")
# menu_direita.pack(side=RIGHT, expand=YES, fill=BOTH)


# # inserindo texto no label do topo
# titulo_topo = Label(menu_topo,font=('arial',50,'bold'), text="SISTEMA CAFETERIA", bd=10, width=32)
# titulo_topo.grid(row=0, column=0)


# janela.mainloop()
