from tkinter import *


root = Tk()

# label
# myLabel1 = Label(root, text="hello world").grid(row=0, column=0)
# myLabel2 = Label(root, text="Eu sou o Gustavo").grid(row=1, column=1)
# myLabel.pack()

# grid
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)


# campo para digitar
# e = Entry(root, width=50, bg="blue", fg="white")
e = Entry(root, width=50)
e.pack()
e.insert(0, "Sem nome") # inserir uma string padrão no campo

# button
def clicar():
    # myLabelButton = Label(root, text="Foi clicado!!") # exibe o texto
    myLabelButton = Label(root, text="Olá {}!".format(e.get())) # exibe o conteudo digitado no campo 
    myLabelButton.pack()

myButton = Button(root, text="Clique", command=clicar)
# myButton = Button(root, text="Clique", command=clicar()) # executa antes do clique
myButton.pack()
# myButton.grid()

root.mainloop()
