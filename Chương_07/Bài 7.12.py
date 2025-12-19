import tkinter as tk
from tkinter import messagebox

def tinh_bmi():
    try:
        can_nang = float(entry_can.get())
        chieu_cao = float(entry_cao.get())

        if can_nang <= 0 or chieu_cao <= 0:
            messagebox.showerror("Lỗi", "Cân nặng và chiều cao phải > 0")
            return

        bmi = can_nang / (chieu_cao ** 2)
        entry_bmi.delete(0, tk.END)
        entry_bmi.insert(0, f"{bmi:.2f}")

        if bmi < 18.5:
            ket_luan = "Gầy"
        elif bmi < 25:
            ket_luan = "Bình thường"
        elif bmi < 30:
            ket_luan = "Thừa cân"
        else:
            ket_luan = "Béo phì"

        label_kq.config(text="Kết luận: " + ket_luan)

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")

window = tk.Tk()
window.title("Tính chỉ số BMI")

tk.Label(window, text="Cân nặng (kg):").grid(row=0, column=0, padx=10, pady=5)
entry_can = tk.Entry(window)
entry_can.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Chiều cao (m):").grid(row=1, column=0, padx=10, pady=5)
entry_cao = tk.Entry(window)
entry_cao.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="BMI:").grid(row=2, column=0, padx=10, pady=5)
entry_bmi = tk.Entry(window)
entry_bmi.grid(row=2, column=1, padx=10, pady=5)

button = tk.Button(window, text="Tính BMI", command=tinh_bmi)
button.grid(row=3, column=1, pady=10)

label_kq = tk.Label(window, text="Kết luận:")
label_kq.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()