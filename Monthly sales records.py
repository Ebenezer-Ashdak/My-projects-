import tkinter as tk
from tkinter import ttk, messagebox

# List to store all monthly sales records
records = []

# Function to add record
def add_record():
    try:
        # Get values for each crop
        maize_total = float(maize_price.get()) * float(maize_sold.get())
        beans_total = float(beans_price.get()) * float(beans_sold.get())
        rice_total = float(rice_price.get()) * float(rice_sold.get())
        total_revenue = maize_total + beans_total + rice_total

        previous = float(previous_revenue.get())
        if total_revenue > previous:
            profit = total_revenue - previous
            loss = 0
        elif total_revenue < previous:
            profit = 0
            loss = previous - total_revenue
        else:
            profit = 0
            loss = 0

        # Store record
        record = {
            "Month": month_entry.get(),
            "Maize": maize_total,
            "Beans": beans_total,
            "Rice": rice_total,
            "Revenue": total_revenue,
            "Profit": profit,
            "Loss": loss
        }
        records.append(record)
        update_table()
        clear_inputs()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# Function to update table
def update_table():
    for row in tree.get_children():
        tree.delete(row)
    for rec in records:
        # Highlight profit/loss
        if rec["Profit"] > 0:
            tree.insert("", "end", values=(rec["Month"], rec["Maize"], rec["Beans"], rec["Rice"], rec["Revenue"], rec["Profit"], rec["Loss"]), tags=("profit",))
        elif rec["Loss"] > 0:
            tree.insert("", "end", values=(rec["Month"], rec["Maize"], rec["Beans"], rec["Rice"], rec["Revenue"], rec["Profit"], rec["Loss"]), tags=("loss",))
        else:
            tree.insert("", "end", values=(rec["Month"], rec["Maize"], rec["Beans"], rec["Rice"], rec["Revenue"], rec["Profit"], rec["Loss"]))

# Function to clear input fields
def clear_inputs():
    month_entry.delete(0, tk.END)
    maize_price.delete(0, tk.END)
    maize_sold.delete(0, tk.END)
    beans_price.delete(0, tk.END)
    beans_sold.delete(0, tk.END)
    rice_price.delete(0, tk.END)
    rice_sold.delete(0, tk.END)
    previous_revenue.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Farm Management App")
root.geometry("800x600")

tk.Label(root, text="Farm Management App - Track Monthly Sales", font=("Helvetica", 16, "bold")).pack(pady=10)

# Month input
tk.Label(root, text="Month:").pack()
month_entry = tk.Entry(root)
month_entry.pack()

# Maize
tk.Label(root, text="Maize price:").pack()
maize_price = tk.Entry(root)
maize_price.pack()
tk.Label(root, text="Maize sold (bags):").pack()
maize_sold = tk.Entry(root)
maize_sold.pack()

# Beans
tk.Label(root, text="Beans price:").pack()
beans_price = tk.Entry(root)
beans_price.pack()
tk.Label(root, text="Beans sold (bags):").pack()
beans_sold = tk.Entry(root)
beans_sold.pack()

# Rice
tk.Label(root, text="Rice price:").pack()
rice_price = tk.Entry(root)
rice_price.pack()
tk.Label(root, text="Rice sold (bags):").pack()
rice_sold = tk.Entry(root)
rice_sold.pack()

# Previous month revenue
tk.Label(root, text="Previous month revenue:").pack()
previous_revenue = tk.Entry(root)
previous_revenue.pack()

# Add record button
tk.Button(root, text="Add Monthly Record", command=add_record, bg="green", fg="white").pack(pady=10)

# Table for all records
columns = ("Month", "Maize", "Beans", "Rice", "Revenue", "Profit", "Loss")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack(pady=10)

# Tags for coloring
tree.tag_configure("profit", foreground="green")
tree.tag_configure("loss", foreground="red")

root.mainloop()