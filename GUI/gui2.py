from customtkinter import *

root = CTk()

root.geometry('600x400')
root._set_appearance_mode('system')

enter = CTkEntry(root, width=300, fg_color='black', border_color='purple', border_width=4, placeholder_text='enter URL:', placeholder_text_color='purple',
                 corner_radius=20)
enter.place(x=10, y=100)


root.mainloop()