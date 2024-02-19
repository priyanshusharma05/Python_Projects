import tkinter as tk
from forex_python.converter import CurrencyRates

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        
        # Set default values
        self.amount_var.set(1.0)
        self.from_currency_var.set("USD")
        self.to_currency_var.set("EUR")
        
        # Entry widgets
        tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.amount_var).grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(root, text="From Currency:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.from_currency_var).grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(root, text="To Currency:").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.to_currency_var).grid(row=2, column=1, padx=10, pady=10)
        
        # Result label
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Convert button
        tk.Button(root, text="Convert", command=self.convert).grid(row=4, column=0, columnspan=2, pady=10)

    def convert(self):
        try:
            amount = float(self.amount_var.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            c = CurrencyRates()
            rate = c.get_rate(from_currency, to_currency)
            converted_amount = round(amount * rate, 2)

            result_text = f"{amount} {from_currency} = {converted_amount} {to_currency}"
            self.result_label.config(text=result_text)

        except Exception as e:
            self.result_label.config(text="Error: Please check your input.")


root = tk.Tk()
converter = CurrencyConverter(root)
root.geometry('500x400')
root.mainloop()
