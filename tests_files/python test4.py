from customtkinter import *#


root = CTk()
root.geometry('600x400')


btn = CTkButton(root, text='black', text_color='purple', fg_color='black', width=100, height=35, border_color='purple', border_width=4, corner_radius=200)
btn.place(x=100, y=100)

root.mainloop()