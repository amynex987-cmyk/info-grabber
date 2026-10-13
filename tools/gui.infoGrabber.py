from customtkinter import *

root = CTk()
root.geometry('600x400')
set_appearance_mode('dark')
root.title('Info Grabber GUI V0.1, Pre-Alpha')
lb = CTkLabel(root, text='Info Grabber', text_color='purple', font=('arial', 16, 'bold'))
lb.pack()

def options1(choice):
    if choice == 'light':
        set_appearance_mode('light')
    elif choice == 'dark':
        set_appearance_mode('dark')
    elif choice == 'system':
        set_appearance_mode('system')

def search(choice)
er = CTkEntry(root, width=560, height=30, corner_radius=20, border_color='purple', border_width=3, placeholder_text='Enter URL :', placeholder_text_color='purple', fg_color='black')
er.place(x=20, y=45)
op = CTkOptionMenu(root,values=['dark', 'light', 'system'], width=50, height=18, fg_color='black', text_color='purple', button_color='purple', command=(options1), corner_radius=10, dropdown_fg_color='black', dropdown_text_color='purple', dropdown_hover_color='', dropdown_font=('arial', 14, 'bold'))
op.place(x=10, y=10)






root.mainloop()