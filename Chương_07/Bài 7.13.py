import tkinter as tk
from tkinter import messagebox

def bai_1_1():
    messagebox.showinfo(
        "Lập trình hướng đối tượng",
        "Giải phương trình bậc 2"
    )

window = tk.Tk()
window.title("Hệ thống bài tập Python nâng cao")
window.geometry("400x300")

menubar = tk.Menu(window)

# Tạo menu Chương 1
chuong1 = tk.Menu(menubar, tearoff=0)
chuong1.add_command(label="1.1", command=bai_1_1)

# Các bài còn lại (demo, chưa xử lý)
for i in range(2, 10):
    chuong1.add_command(label=f"1.{i}")

menubar.add_cascade(label="Chương 1", menu=chuong1)

# Tạo các chương 2 → 7 (demo)
for m in range(2, 8):
    chuong = tk.Menu(menubar, tearoff=0)
    for n in range(1, 10):
        chuong.add_command(label=f"{m}.{n}")
    menubar.add_cascade(label=f"Chương {m}", menu=chuong)

window.config(menu=menubar)
window.mainloop()