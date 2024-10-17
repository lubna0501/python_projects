import tkinter as tk
from tkinter import messagebox
import math

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.expression = ""

        self.entry = tk.Entry(master, font=("Arial", 18), bd=5, justify="right")
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^3', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('^2', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('C', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3), ('exp', 5, 4)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(master, text=text, font=("Arial", 12), width=4, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        self.entry.focus_set()

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid expression: {e}")
        elif char == 'C':
            self.entry.delete(0, tk.END)
        elif char == 'sqrt':
            try:
                result = math.sqrt(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
        elif char == '^2':
            try:
                result = eval(self.entry.get()) ** 2
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
        elif char == '^3':
            try:
                result = eval(self.entry.get()) ** 3
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
        elif char == 'sin':
            try:
                result = math.sin(math.radians(float(self.entry.get())))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
        elif char == 'cos':
            try:
                result = math.cos(math.radians(float(self.entry.get())))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
        elif char == 'tan':
            try:
                result = math.tan(math.radians(float(self.entry.get())))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
        elif char == 'log':
            try:
                result = math.log10(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
        elif char == 'exp':
            try:
                result = math.exp(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
        else:
            self.entry.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
