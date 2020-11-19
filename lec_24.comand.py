import tkinter as tk

window = tk.Tk()



button_1.pack()

def hand_click_1():
    print('no')
    
def hand_click_2():
    print('yes')

button_1 = tk.Button(
        text = 'put',
        width = 25, height = 15,
        bg ='green', fg = 'red',
        comand=hand_click_1) 

 pack  

window.mainloop()