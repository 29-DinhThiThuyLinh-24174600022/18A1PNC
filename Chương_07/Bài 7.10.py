import tkinter as tk
from tkinter import messagebox, simpledialog

window = tk.Tk()
window.withdraw()   # Ẩn cửa sổ chính

ten = simpledialog.askstring("Nhập tên", "Vui lòng nhập tên của bạn:")
tuoi = simpledialog.askinteger("Nhập tuổi", "Vui lòng nhập tuổi của bạn:")

if ten is not None and tuoi is not None:
    if tuoi >= 18:
        message = f"Xin chào {ten}!\nBạn đã trưởng thành!"
    else:
        message = f"Xin chào {ten}!\nBạn còn nhỏ tuổi!"

    messagebox.showinfo("Thông báo", message)