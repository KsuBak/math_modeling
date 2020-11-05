import tkinter as tk
window = tk.Tk()


text_1 = tk.Label(text = 'hello')



label_1 = tk.Label(text = 'hkv',
                   bg = 'black',
                   fg = 'green',
                   width = 20,
                   height = 20)
label_1.pack()
text_1.pack()

window.mainloop()
