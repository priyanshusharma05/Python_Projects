import tkinter as tk
# class currencyconverter:
#     def __init__(self,mainwindow):
#         self.mainwindow=mainwindow

#         tk.Label(text='Currency Converter',font=('bold',20)).grid(row=0,column=0)
        
#         self.entry=tk.Entry()
#         self.entry.grid(row=1,column=0)
        
# root=tk.Tk()
# exc=currencyconverter(root)
# root.title("Currency Converter")
# root.geometry('500x400')
# root.mainloop
from tkinter import ttk
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()

        # Entry for amount
        amount_label = tk.Label(root, text="Amount:")
        amount_label.grid(row=0, column=0, padx=10, pady=10)
        amount_entry = tk.Entry(root, textvariable=self.amount_var)
        amount_entry.grid(row=0, column=1, padx=10, pady=10)

        # Combobox for 'From' currency
        from_currency_label = tk.Label(root, text="From Currency:")
        from_currency_label.grid(row=1, column=0, padx=10, pady=10)
        from_currency_combobox = ttk.Combobox(root, textvariable=self.from_currency_var)
        from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
        from_currency_combobox['values'] = self.get_currency_list()
        from_currency_combobox.set("USD")

        # Combobox for 'To' currency
        to_currency_label = tk.Label(root, text="To Currency:")
        to_currency_label.grid(row=2, column=0, padx=10, pady=10)
        to_currency_combobox = ttk.Combobox(root, textvariable=self.to_currency_var)
        to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)
        to_currency_combobox['values'] = self.get_currency_list()
        to_currency_combobox.set("EUR")

        # Button to perform conversion
        convert_button = tk.Button(root, text="Convert", command=self.convert_currency)
        convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Label to display result
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def get_currency_list(self):
        # You can customize this list by adding more currencies as needed
        return ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "INR", "CNY"]

    def convert_currency(self):
        amount = self.amount_var.get()
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()

        if amount and from_currency and to_currency:
            try:
                api_key = "YOUR_API_KEY"  # Replace with your API key from exchangeratesapi.io
                base_url = f"https://open.er-api.com/v6/latest/{from_currency}"

                response = requests.get(base_url)
                data = response.json()

                conversion_rate = data["rates"][to_currency]
                converted_amount = amount * conversion_rate

                result_text = f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
                self.result_label.config(text=result_text)
            except Exception as e:
                self.result_label.config(text=f"Error: {str(e)}")
        else:
            self.result_label.config(text="Please enter valid values.")

if __name__ == "__main__":
    root = tk.Tk()
    converter = CurrencyConverter(root)
    root.mainloop()
