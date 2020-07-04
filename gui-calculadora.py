from tkinter import *  # Importando tudo da biblioteca

root = Tk()  # Criando nossa janela, uma instância de Tk()
root.title('Calculadora')  # Nomeando a janela

window_title = Label(root, text='Calculadora', font=('Helvetica',
	18)).grid(row=0, column=0, columnspan=2)  # Título para a calculadora

label_1 = Label(root, text='Digite um número').grid(row=1, column=0)  # Primeiro número
entry_field_1 = Entry(root, text='Número 1', width=10)
entry_field_1.grid(row=1, column=1)

label_2 = Label(root, text='Digite outro número').grid(row=2, column=0)  # Segundo número
entry_field_2 = Entry(root, text='Número 2', width=10)
entry_field_2.grid(row=2, column=1)

root.mainloop()  # Criando um loop eterno (basicamente um "while True" por debaixo dos 
                 # panos para abrir nossa janela)
