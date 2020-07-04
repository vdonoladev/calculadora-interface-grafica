from tkinter import *  # Importando tudo da biblioteca

root = Tk()  # Criando nossa janela, uma instância de Tk()
root.title('Calculadora')  # Nomeando a janela

window_title = Label(root, text='Calculadora', font=('Helvetica',
	18)).grid(row=0, column=0, columnspan=2)  # Título para a calculadora

root.mainloop()  # Criando um loop eterno (basicamente um "while True" por debaixo dos 
                 # panos para abrir nossa janela)
