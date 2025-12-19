import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Chương trình xem ảnh")

image = Image.open(r"C:\Users\Dell N5430\OneDrive\Đính kèm\PNC\18A1PNC\Chương_07\Bài 7.5\oto.png")
new_size = (400, 400)
image = image.resize(new_size, Image.Resampling.LANCZOS)

img = ImageTk.PhotoImage(image)

label = tk.Label(window, image=img)
label.image = img
label.pack()

window.mainloop()