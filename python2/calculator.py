import tkinter as tk

cal = ""

def add_to_cal(symbol):
    global cal
    cal += str(symbol)
    text_res.delete(1.0, "end")
    text_res.insert(1.0, cal)

def evaluate_cal():
    global cal
    try:
        result = str(eval(cal))
        cal = result
        text_res.delete(1.0, "end")
        text_res.insert(1.0, result)
    except:
        clear_field()
        text_res.insert(1.0, "error")

def clear_field():
    global cal
    cal = ""
    text_res.delete(1.0, "end")
    text_res.insert(1.0, "error")

window = tk.Tk()
window.geometry("300x275+100+100")
window.title("Chasmiya")

text_res = tk.Text(window, height=2, width=16, font=("arial", 24, "bold"))
text_res.grid(columnspan=5)

btn_1 = tk.Button(window, text="1", command=lambda: add_to_cal(1), width=5, font=("arial", 14, "bold"))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(window, text="2", command=lambda: add_to_cal(2), width=5, font=("arial", 14, "bold"))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(window, text="3", command=lambda: add_to_cal(3), width=5, font=("arial", 14, "bold"))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(window, text="4", command=lambda: add_to_cal(4), width=5, font=("arial", 14, "bold"))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(window, text="5", command=lambda: add_to_cal(5), width=5, font=("arial", 14, "bold"))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(window, text="6", command=lambda: add_to_cal(6), width=5, font=("arial", 14, "bold"))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(window, text="7", command=lambda: add_to_cal(7), width=5, font=("arial", 14, "bold"))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(window, text="8", command=lambda: add_to_cal(8), width=5, font=("arial", 14, "bold"))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(window, text="9", command=lambda: add_to_cal(9), width=5, font=("arial", 14, "bold"))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(window, text="0", command=lambda: add_to_cal(0), width=5, font=("arial", 14, "bold"))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(window, text="+", command=lambda: add_to_cal("+"), width=5, font=("arial", 14, "bold"))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(window, text="-", command=lambda: add_to_cal("-"), width=5, font=("arial", 14, "bold"))
btn_minus.grid(row=3, column=4)

btn_multiply = tk.Button(window, text="*", command=lambda: add_to_cal("*"), width=5, font=("arial", 14, "bold"))
btn_multiply.grid(row=4, column=4)

btn_divide = tk.Button(window, text="/", command=lambda: add_to_cal("/"), width=5, font=("arial", 14, "bold"))
btn_divide.grid(row=5, column=4)

btn_equal = tk.Button(window, text="=", command=evaluate_cal, width=5, font=("arial", 14, "bold"))
btn_equal.grid(row=5, column=3)

btn_clear = tk.Button(window, text="C", command=clear_field, width=5, font=("arial", 14, "bold"))
btn_clear.grid(row=5, column=1)

window.mainloop()
