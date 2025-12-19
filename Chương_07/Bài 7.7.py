import tkinter as tk

def tinh_tong():
    n = int(entry.get())
    tong = n * (n + 1) // 2
    label_kq.config(text=f"Tổng = {tong}")

window = tk.Tk()
window.title("Tính tổng 1 + 2 + ... + N")

label = tk.Label(window, text="Nhập số nguyên N:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Tính tổng", command=tinh_tong)
button.pack()

label_kq = tk.Label(window, text="Tổng = ")
label_kq.pack()

window.mainloop()