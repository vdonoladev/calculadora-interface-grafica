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

selected_operation = IntVar()

label_3 = Label(root, text='Escolha a operação desejada').grid(row=3, column=0, 
columnspan=2)

sum_button = Radiobutton(root, text='+', variable=selected_operation, value=1)
sum_button.grid(row=4, column=0)

subtraction_button = Radiobutton(root, text='-', variable=selected_operation, value=2)
subtraction_button.grid(row=5, column=0)

multiplication_button = Radiobutton(root, text='x', variable=selected_operation, value=3)
multiplication_button.grid(row=5, column=0)

division_button = Radiobutton(root, text='/', variable=selected_operation, value=4)
division_button.grid(row=5, column=1)

root.mainloop()  # Criando um loop eterno (basicamente um "while True" por debaixo dos 
                 # panos para abrir nossa janela)
