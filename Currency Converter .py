import tkinter as tk
from tkinter import messagebox, ttk

# Fixed currency rates
rates = {
    "USD": 1,
    "EUR": 0.93,
    "GHS": 15.0,
    "GBP": 0.81
}

history = []

# =========================
# Conversion Function
# =========================
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_var.get()
        to_curr = to_var.get()
    except:
        messagebox.showerror("Error", "Enter valid amount.")
        return

    if from_curr not in rates or to_curr not in rates:
        messagebox.showerror("Error", "Select valid currencies.")
        return

    converted = amount / rates[from_curr] * rates[to_curr]
    result_label.config(text=f"{amount} {from_curr} = {converted:.2f} {to_curr}")

    # Save to history
    history.append((len(history)+1, amount, from_curr, to_curr, round(converted, 2)))
    update_history()

# =========================
# Update History Table
# =========================
def update_history():
    for item in tree.get_children():
        tree.delete(item)
    for record in history:
        tree.insert("", "end", values=record)

def clear_history():
    history.clear()
    update_history()
    result_label.config(text="")

# =========================
# GUI Setup
# =========================
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x500")

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

from_var = tk.StringVar()
to_var = tk.StringVar()

tk.Label(root, text="From Currency:").pack()
from_menu = tk.OptionMenu(root, from_var, *rates.keys())
from_menu.pack()

tk.Label(root, text="To Currency:").pack()
to_menu = tk.OptionMenu(root, to_var, *rates.keys())
to_menu.pack()

tk.Button(root, text="Convert", command=convert_currency).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# History Table
tk.Label(root, text="Conversion History", font=("Helvetica", 12, "bold")).pack(pady=5)
columns = ("#", "Amount", "From", "To", "Converted")
tree = ttk.Treeview(root, columns=columns, show="headings", height=8)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=90)
tree.pack(pady=10)

tk.Button(root, text="Clear History", command=clear_history).pack(pady=5)

root.mainloop()