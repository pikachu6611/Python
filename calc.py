import tkinter as tk
root = tk.Tk()


calculation = ''

def add_to_calculation(symbol):
    global calculation
    calculation = calculation + str(symbol)

    text_result.delete(0, 'end')
    text_result.insert(0, calculation)

def eval_calc():
    global calculation
    result = round(eval(calculation), 2)
    text_result.delete(0, 'end')
    text_result.insert(0, result)
    calculation = str(result)

def negate_num():
    global calculation
    result = str(int(calculation) * -1)
    text_result.delete(0, 'end')
    text_result.insert(0, result)



def clear_field():
    text_result.delete(0, 'end')
    global calculation
    calculation = ''

root.title("Calculator")
root.geometry("210x270")
#root.resizable(0, 0)
root.config(background="#F5D042")

text_result = tk.Entry(root, width=9, bg="#0A174E", fg="white", font=("verdana", 30, "bold"))
text_result.grid(row=0, column=0, columnspan=23, pady=10)

#first row buttons
btn_ac = tk.Button(root, text="AC", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1, command=clear_field)
btn_ac.grid(row=1, column=0)
btn_negate = tk.Button(root, text="+/", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                       command=negate_num)
btn_negate.grid(row=1, column=1)
btn_mod = tk.Button(root, text="%", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1)
btn_mod.grid(row=1, column=2)
btn_divide = tk.Button(root, text="/", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                       command=lambda: add_to_calculation("/"))
btn_divide.grid(row=1, column=3)


#second row buttons
btn_7 = tk.Button(root, text="7", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                  command=lambda: add_to_calculation("7"))
btn_7.grid(row=2, column=0)
btn_8 = tk.Button(root, text="8", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                  command=lambda: add_to_calculation("8"))
btn_8.grid(row=2, column=1)
btn_9 = tk.Button(root, text="9", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                  command=lambda: add_to_calculation("9"))
btn_9.grid(row=2, column=2)
btn_mul = tk.Button(root, text="*", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                    command=lambda: add_to_calculation("*"))
btn_mul.grid(row=2, column=3)

#third row buttons
btn_4 = tk.Button(root, text="4", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                  command=lambda: add_to_calculation("4"))
btn_4.grid(row=3, column=0)
btn_5 = tk.Button(root, text="5", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                  command=lambda: add_to_calculation("5"))
btn_5.grid(row=3, column=1)
btn_6 = tk.Button(root, text="6", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                  command=lambda: add_to_calculation("6"))
btn_6.grid(row=3, column=2)
btn_sub = tk.Button(root, text="-", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                    command=lambda: add_to_calculation("-"))
btn_sub.grid(row=3, column=3)

#fourth row  buttons
btn_1 = tk.Button(root, text="1", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                  command=lambda: add_to_calculation("1"))
btn_1.grid(row=4, column=0)
btn_2 = tk.Button(root, text="2", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                  command=lambda: add_to_calculation("2"))
btn_2.grid(row=4, column=1)
btn_3 = tk.Button(root, text="3", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                  command=lambda: add_to_calculation("3"))
btn_3.grid(row=4, column=2)
btn_plus = tk.Button(root, text="+", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                     command=lambda: add_to_calculation("+"))
btn_plus.grid(row=4, column=3)

#fifth row buttons
btn_0 = tk.Button(root, text="0", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                  command=lambda: add_to_calculation("0"))
btn_0.grid(row=5, column=0)
btn_dot = tk.Button(root, text=".", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                    command=lambda: add_to_calculation("."))
btn_dot.grid(row=5, column=1)
btn_equal = tk.Button(root, text="=", bg="#F5D042", fg='black', width=6, height=2,
                activeforeground="grey", activebackground="white", borderwidth=1,
                      command=eval_calc)
btn_equal.grid(row=5, column=2)


root.mainloop()