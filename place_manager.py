import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master = window, width = 150, height = 150)
frame.pack()

button_1= tk.Button(text = 'jGf',
                    height = 16,
                    width = 25,
                    bg= 'green', 
                    fg = 'black')

button_2= tk.Button(text = 'jGf',
                    width = 25,
                    height = 16,
                    bg= 'green', 
                    fg = 'black')

button_1.pack()
button_2.pack()


label_1 = tk.Label(master = frame, text = 'uuugkj', bg= 'black')
label_1.place(x=0, y=0)

label_2 = tk.Label(master = frame, text = 'uuugkj', bg ='black')
label_2.place(x=75, y=75)

window.mainloop()
