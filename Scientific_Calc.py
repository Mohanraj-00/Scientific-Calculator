import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("480x700")
        self.expression = ""

        self.input_text = tk.StringVar()
        self.input_frame = self.create_input_frame()
        self.create_buttons()
        self.create_menu()

    def create_input_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(side=tk.TOP)

        input_field = tk.Entry(frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=20, insertwidth=4, width=29, borderwidth=4)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)
        return frame

    def create_buttons(self):
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()

        buttons = [
            '7', '8', '9', '/', 'sin', 'asin', 'sinh', 'asinh',
            '4', '5', '6', '*', 'cos', 'acos', 'cosh', 'acosh',
            '1', '2', '3', '-', 'tan', 'atan', 'tanh', 'atanh',
            '0', '.', '=', '+', 'log', 'ln', 'sqrt', 'exp',
            'pi', 'e', 'C', '(', ')', '^', 'fact', 'deg', 'rad'
        ]

        row_val = 0
        col_val = 0

        for button in buttons:
            command = lambda x=button: self.click(x)
            tk.Button(buttons_frame, text=button, width=5, height=2, command=command).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 7:
                col_val = 0
                row_val += 1

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Guide", command=self.show_guide)

    def show_guide(self):
        guide_window = tk.Toplevel(self.root)
        guide_window.title("Calculator Guide")
        guide_text = (
            "Guide to Scientific Calculator Functions:\n\n"
            "Basic Operations:\n"
            "  - + : Addition\n"
            "  - - : Subtraction\n"
            "  - * : Multiplication\n"
            "  - / : Division\n"
            "  - = : Evaluate expression\n"
            "  - C : Clear the current expression\n"
            "\n"
            "Scientific Functions:\n"
            "  - sin, cos, tan: Trigonometric functions (input in degrees)\n"
            "  - asin, acos, atan: Inverse trigonometric functions\n"
            "  - sinh, cosh, tanh: Hyperbolic functions\n"
            "  - asinh, acosh, atanh: Inverse hyperbolic functions\n"
            "  - log: Logarithm base 10\n"
            "  - ln: Natural logarithm\n"
            "  - sqrt: Square root\n"
            "  - exp: Exponential (e^x)\n"
            "  - fact: Factorial\n"
            "\n"
            "Constants and Special Operations:\n"
            "  - pi: π (Pi)\n"
            "  - e: Euler's number\n"
            "  - ^ : Exponentiation\n"
            "  - deg: Convert radians to degrees\n"
            "  - rad: Convert degrees to radians\n"
        )
        guide_label = tk.Label(guide_window, text=guide_text, justify=tk.LEFT, padx=10, pady=10, font=('arial', 12))
        guide_label.pack()

    def click(self, button):
        if button == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = ""
                messagebox.showerror("Error", f"Invalid Expression: {str(e)}")
        elif button == "C":
            self.clear()
        elif button == "pi":
            self.expression += str(math.pi)
        elif button == "e":
            self.expression += str(math.e)
        elif button == "sqrt":
            try:
                self.expression = str(math.sqrt(float(self.expression)))
            except Exception as e:
                self.expression = ""
                messagebox.showerror("Error", f"Invalid Input for sqrt: {str(e)}")
        elif button == "exp":
            try:
                self.expression = str(math.exp(float(self.expression)))
            except Exception as e:
                self.expression = ""
                messagebox.showerror("Error", f"Invalid Input for exp: {str(e)}")
        elif button == "fact":
            try:
                self.expression = str(math.factorial(int(self.expression)))
            except Exception as e:
                self.expression = ""
                messagebox.showerror("Error", f"Invalid Input for fact: {str(e)}")
        elif button == "log":
            try:
                self.expression = str(math.log10(float(self.expression)))
            except Exception as e:
                self.expression = ""
                messagebox.showerror("Error", f"Invalid Input for log: {str(e)}")
        elif button == "ln":
            try:
                self.expression = str(math.log(float(self.expression)))
            except Exception as e:
                self.expression = ""
                messagebox.showerror("Error", f"Invalid Input for ln: {str(e)}")
        elif button == "deg":
            try:
                self.expression = str(math.degrees(float(self.expression)))
            except Exception as e:
                self.expression = ""
                messagebox.showerror("Error", f"Invalid Input for deg: {str(e)}")
        elif button == "rad":
            try:
                self.expression = str(math.radians(float(self.expression)))
            except Exception as e:
                self.expression = ""
                messagebox.showerror("Error", f"Invalid Input for rad: {str(e)}")
        elif button == "^":
            self.expression += "**"
        else:
            if button in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh', 'asinh', 'acosh', 'atanh']:
                try:
                    value = float(self.expression)
                    if button == 'sin':
                        self.expression = str(math.sin(math.radians(value)))
                    elif button == 'cos':
                        self.expression = str(math.cos(math.radians(value)))
                    elif button == 'tan':
                        self.expression = str(math.tan(math.radians(value)))
                    elif button == 'asin':
                        self.expression = str(math.degrees(math.asin(value)))
                    elif button == 'acos':
                        self.expression = str(math.degrees(math.acos(value)))
                    elif button == 'atan':
                        self.expression = str(math.degrees(math.atan(value)))
                    elif button == 'sinh':
                        self.expression = str(math.sinh(value))
                    elif button == 'cosh':
                        self.expression = str(math.cosh(value))
                    elif button == 'tanh':
                        self.expression = str(math.tanh(value))
                    elif button == 'asinh':
                        self.expression = str(math.asinh(value))
                    elif button == 'acosh':
                        self.expression = str(math.acosh(value))
                    elif button == 'atanh':
                        self.expression = str(math.atanh(value))
                except Exception as e:
                    self.expression = ""
                    messagebox.showerror("Error", f"Invalid Input for {button}: {str(e)}")
            else:
                self.expression += str(button)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
