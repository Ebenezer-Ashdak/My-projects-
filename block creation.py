import tkinter as tk
import random

root = tk.Tk()
root.title("Block Builder GUI")
root.geometry("400x400")

blocks = []

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

def add_block():
    x = random.randint(50, 350)
    y = random.randint(50, 350)
    block = canvas.create_rectangle(x, y, x+30, y+30, fill="blue")
    blocks.append(block)

def remove_block():
    if blocks:
        canvas.delete(blocks[-1])
        blocks.pop()

add_btn = tk.Button(root, text="Add Block", command=add_block)
add_btn.pack(side="left", padx=10, pady=10)

remove_btn = tk.Button(root, text="Remove Block", command=remove_block)
remove_btn.pack(side="right", padx=10, pady=10)

root.mainloop()