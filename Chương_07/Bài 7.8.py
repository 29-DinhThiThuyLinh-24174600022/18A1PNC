import tkinter as tk

def tim_uoc():
    n = int(entry.get())
    ds_uoc = []

    for i in range(1, n + 1):
        if n % i == 0:
            ds_uoc.append(str(i))

    label_kq.config(text="Các ước của N: " + "  ".join(ds_uoc))


window = tk.Tk()
window.title("Tìm các ước của số nguyên N")

label = tk.Label(window, text="Nhập giá trị N:")
label.grid(row=0, column=0, padx=10, pady=5)

entry = tk.Entry(window)
entry.grid(row=0, column=1, padx=10, pady=5)

label_kq = tk.Label(window, text="Các ước của N:")
label_kq.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

button = tk.Button(window, text="Kiểm tra", command=tim_uoc)
button.grid(row=2, column=1, pady=10)

window.mainloop()