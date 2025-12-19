import tkinter as tk
from tkinter import ttk

def tinh_toan():
    m = int(entry_m.get())
    n = int(entry_n.get())
    chon = combo.get()

    if chon == "GCD":
        a, b = m, n
        while b != 0:
            a, b = b, a % b
        kq = a
        label_kq.config(text=f"Ước số chung lớn nhất GCD({m}, {n}) = {kq}")

    elif chon == "LCM":
        a, b = m, n
        while b != 0:
            a, b = b, a % b
        gcd = a
        lcm = m * n // gcd
        label_kq.config(text=f"Bội số chung nhỏ nhất LCM({m}, {n}) = {lcm}")


window = tk.Tk()
window.title("Tính GCD và LCM")

# Nhập m
label_m = tk.Label(window, text="Nhập giá trị m:")
label_m.grid(row=0, column=0, padx=10, pady=5)
entry_m = tk.Entry(window)
entry_m.grid(row=0, column=1, padx=10, pady=5)

# Nhập n
label_n = tk.Label(window, text="Nhập giá trị n:")
label_n.grid(row=1, column=0, padx=10, pady=5)
entry_n = tk.Entry(window)
entry_n.grid(row=1, column=1, padx=10, pady=5)

# Chọn chức năng
label_chon = tk.Label(window, text="Chọn chức năng:")
label_chon.grid(row=2, column=0, padx=10, pady=5)

combo = ttk.Combobox(window, values=["GCD", "LCM"])
combo.current(0)
combo.grid(row=2, column=1, padx=10, pady=5)

# Nút tính
button = tk.Button(window, text="Tính", command=tinh_toan)
button.grid(row=3, column=1, pady=10)

# Kết quả
label_kq = tk.Label(window, text="")
label_kq.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()