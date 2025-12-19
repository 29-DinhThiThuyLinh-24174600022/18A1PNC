import tkinter as tk
from tkinter import ttk, messagebox

def tinh_tien():
    try:
        km = float(entry_km.get())
        phut_cho = int(entry_cho.get())
        loai_xe = combo_xe.get()

        if km <= 0 or phut_cho < 0:
            messagebox.showerror("Lỗi", "Dữ liệu không hợp lệ")
            return

        # Giá mở cửa
        tong = 12000
        km_con_lai = km - 0.8

        if km_con_lai > 0:
            if loai_xe == "Xe 4 chỗ":
                gia_30 = 15300
                gia_sau_30 = 12100
            else:
                gia_30 = 16100
                gia_sau_30 = 13800

            if km_con_lai <= 30:
                tong += km_con_lai * gia_30
            else:
                tong += 30 * gia_30
                tong += (km_con_lai - 30) * gia_sau_30

        # Tiền chờ
        if phut_cho > 5:
            tong += (phut_cho - 5) * 750

        label_kq.config(text=f"Tổng tiền: {int(tong):,} đồng")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng số")

window = tk.Tk()
window.title("Tính cước taxi")

tk.Label(window, text="Chọn loại xe:").grid(row=0, column=0, padx=10, pady=5)
combo_xe = ttk.Combobox(window, values=["Xe 4 chỗ", "Xe 7 chỗ"])
combo_xe.current(0)
combo_xe.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Quãng đường (km):").grid(row=1, column=0, padx=10, pady=5)
entry_km = tk.Entry(window)
entry_km.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Thời gian chờ (phút):").grid(row=2, column=0, padx=10, pady=5)
entry_cho = tk.Entry(window)
entry_cho.grid(row=2, column=1, padx=10, pady=5)

button = tk.Button(window, text="Tính tiền", command=tinh_tien)
button.grid(row=3, column=1, pady=10)

label_kq = tk.Label(window, text="Tổng tiền:")
label_kq.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()