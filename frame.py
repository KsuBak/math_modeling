import tkinter as tk

window = tk.Tk()

frame_1 = tk.Frame()
frame_2 = tk.Frame()

label_1 = tk.Label(master = frame_2, text= 'jyf')
label_1.pack()

label_2 = tk.Label(master = frame_1, text= 'jyf')

label_2.pack()

frame_1.pack()
frame_2.pack()

window.mainloop()
