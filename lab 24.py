import tkinter as tk

from random import randint

window = tk.Tk()

lbl_1 = tk.Label(master=window, text ='0' )

lbl_1.pack()

button_1 = tk.Button(
        text = 'Бросить!',
        width = 15, height = 8,
        bg ='black', fg = 'red')

button_1.pack()

def hand_click(event):
    value = randint(1, 6)
    lbl_1['text'] = '{}'.format(value)
  
   
button_1.bind('<Button-1>',
              hand_click)



window.mainloop()

















