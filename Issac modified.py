import tkinter as tk
from tkinter import messagebox
import datetime

# ======================
# SYSTEM SETTINGS
# ======================

VALID_CODE = "Issac10"
balance = 5000        # Starting balance
attempts = 0
MAX_ATTEMPTS = 3

# ======================
# FUNCTIONS
# ======================

def verify_transaction():
    global attempts

    code = code_entry.get()

    if code == VALID_CODE:
        messagebox.showinfo("Verified", "Security Check Passed ✅")
        receiver_frame.pack(pady=15)
        attempts = 0
    else:
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts

        if remaining > 0:
            messagebox.showerror("Error",
                                 f"Invalid Code! {remaining} attempts left.")
        else:
            messagebox.showerror("LOCKED",
                                 "Too many failed attempts.\nSystem Locked.")
            verify_button.config(state="disabled")


def complete_transaction():
    global balance

    try:
        amount = float(amount_entry.get())
    except:
        messagebox.showerror("Error", "Enter valid amount.")
        return

    currency = currency_entry.get()
    receiver_name = receiver_name_entry.get()

    if amount > balance:
        messagebox.showerror("Error", "Insufficient Balance!")
        return

    if not receiver_name:
        messagebox.showerror("Error", "Enter receiver name.")
        return

    balance -= amount
    balance_label.config(text=f"Balance: {balance:.2f} GHS")

    # Save transaction
    save_transaction(amount, currency, receiver_name)

    messagebox.showinfo(
        "Transaction Successful",
        f"Sent {amount} {currency} to {receiver_name}\n\nNew Balance: {balance:.2f}"
    )

    reset_fields()


def save_transaction(amount, currency, receiver):
    now = datetime.datetime.now()
    record = f"{now} | Sent {amount} {currency} to {receiver}\n"

    with open("transactions.txt", "a") as file:
        file.write(record)


def reset_fields():
    amount_entry.delete(0, tk.END)
    currency_entry.delete(0, tk.END)
    code_entry.delete(0, tk.END)
    receiver_name_entry.delete(0, tk.END)
    receiver_frame.pack_forget()


# ======================
# GUI
# ======================

root = tk.Tk()
root.title("Advanced Mobile Money")
root.geometry("400x650")
root.configure(bg="#0f172a")

title = tk.Label(root,
                 text="Mobile Money Pro",
                 font=("Arial", 18, "bold"),
                 fg="white",
                 bg="#0f172a")
title.pack(pady=15)

balance_label = tk.Label(root,
                         text=f"Balance: {balance:.2f} GHS",
                         font=("Arial", 14),
                         fg="lime",
                         bg="#0f172a")
balance_label.pack(pady=5)

# Sender Section
tk.Label(root, text="Amount:", fg="white",
         bg="#0f172a").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Currency:", fg="white",
         bg="#0f172a").pack()
currency_entry = tk.Entry(root)
currency_entry.pack()

tk.Label(root, text="Transaction Code:", fg="white",
         bg="#0f172a").pack()
code_entry = tk.Entry(root, show="*")
code_entry.pack()

verify_button = tk.Button(root,
                          text="Verify",
                          bg="green",
                          fg="white",
                          command=verify_transaction)
verify_button.pack(pady=10)

# Receiver Section
receiver_frame = tk.Frame(root, bg="#0f172a")

tk.Label(receiver_frame,
         text="Receiver Name:",
         fg="white",
         bg="#0f172a").pack()
receiver_name_entry = tk.Entry(receiver_frame)
receiver_name_entry.pack()

complete_button = tk.Button(receiver_frame,
                            text="Send Money",
                            bg="blue",
                            fg="white",
                            command=complete_transaction)
complete_button.pack(pady=10)

root.mainloop()