import tkinter as tk

window = tk.Tk()

button_1 = tk.Button(
        text = 'put',
        width = 25, height = 15,
        bg ='green', fg = 'red')

button_1.pack()

def hand_click_left(event):
    print('no')
    
def hand_click_right(event):
    print('yes')
    
button_1.bind('<Button-1>',
              hand_click_left)

button_1.bind('<Button-2>',
              hand_click_right)

window.mainloop()