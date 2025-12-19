import tkinter as tk
from PIL import Image, ImageTk

def chuyen_doi():
    nam = int(entry.get())

    con_giap = [
        "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ",
        "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"
    ]

    ten_anh = [
        r"C:\Users\Dell N5430\OneDrive\Đính kèm\PNC\18A1PNC\Chương_07\Bài 7.11\ty.jpg", 
        r"C:\Users\Dell N5430\OneDrive\Đính kèm\PNC\18A1PNC\Chương_07\Bài 7.11\suu.jpg", 
        r"C:\Users\Dell N5430\OneDrive\Đính kèm\PNC\18A1PNC\Chương_07\Bài 7.11\dan.jpg",
        r"C:\Users\Dell N5430\OneDrive\Đính kèm\PNC\18A1PNC\Chương_07\Bài 7.11\mao.jpg",
        r"C:\Users\Dell N5430\OneDrive\Đính kèm\PNC\18A1PNC\Chương_07\Bài 7.11\thin.jpg", 
        r"C:\Users\Dell N5430\OneDrive\Đính kèm\PNC\18A1PNC\Chương_07\Bài 7.11\ty2.jpg",
        r"C:\Users\Dell N5430\OneDrive\Đính kèm\PNC\18A1PNC\Chương_07\Bài 7.11\ngo.jpg", 
        r"C:\Users\Dell N5430\OneDrive\Đính kèm\PNC\18A1PNC\Chương_07\Bài 7.11\mui.jpg",
        r"C:\Users\Dell N5430\OneDrive\Đính kèm\PNC\18A1PNC\Chương_07\Bài 7.11\than.jpg",
        r"C:\Users\Dell N5430\OneDrive\Đính kèm\PNC\18A1PNC\Chương_07\Bài 7.11\dau.jpg", 
        r"C:\Users\Dell N5430\OneDrive\Đính kèm\PNC\18A1PNC\Chương_07\Bài 7.11\tuat.jpg",
        r"C:\Users\Dell N5430\OneDrive\Đính kèm\PNC\18A1PNC\Chương_07\Bài 7.11\hoi.jpg"
    ]

    index = (nam - 4) % 12
    label_kq.config(text=f"Năm âm lịch: {con_giap[index]}")

    img = Image.open(ten_anh[index])
    img = img.resize((150, 150))
    photo = ImageTk.PhotoImage(img)

    label_img.config(image=photo)
    label_img.image = photo


window = tk.Tk()
window.title("Chuyển đổi năm Dương lịch sang Âm lịch")

tk.Label(window, text="Nhập năm Dương lịch:").pack(pady=5)
entry = tk.Entry(window)
entry.pack(pady=5)

tk.Button(window, text="Chuyển đổi", command=chuyen_doi).pack(pady=5)

label_kq = tk.Label(window, text="")
label_kq.pack(pady=5)

label_img = tk.Label(window)
label_img.pack(pady=5)

window.mainloop()