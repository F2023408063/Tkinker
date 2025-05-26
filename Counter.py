import tkinter as tk
root = tk.Tk()
root.title("Counter")
root.geometry("400x250")
count = 0
label = tk.Label(root, text="0", font=("Times New Roman", 30))
label.pack(pady=10)
def increase():
    global count
    count += 1
    label.config(text=str(count))
def decrease():
    global count
    count -= 1
    label.config(text=str(count))
def reset():
    global count
    count = 0
    label.config(text=str(count))
frame = tk.Frame(root)
frame.pack()
btn_increase = tk.Button(frame, text="+1", command=increase, width=8)
btn_increase.grid(row=0, column=0, padx=5, pady=5)
btn_decrease = tk.Button(frame, text="-1", command=decrease, width=8)
btn_decrease.grid(row=0, column=1, padx=5, pady=5)
btn_reset = tk.Button(frame, text="Reset", command=reset, width=18)
btn_reset.grid(row=1, column=0, columnspan=2, pady=5)
root.mainloop()