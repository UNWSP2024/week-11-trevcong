#AUTHOR: Trevor Conger
#DATE: 11/15/2024
#TITLE: GUI address


import tkinter as tk

def show_info():
    info_label.config(text="Name: Trevor Conger\nAddress: 15830 Van Buren St Ne, Ham Lake. Minnesota USA")

root = tk.Tk()
root.title("Personal Info")

info_label = tk.Label(root, text="")
info_label.pack(pady=20)

show_info_button = tk.Button(root, text="Show Info", command=show_info)
show_info_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)

root.mainloop()