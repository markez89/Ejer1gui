import tkinter
from tkinter import ttk

window = tkinter.Tk()

#Geometrica mediante grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

username_label = ttk.Label(window, text="Seleccione una opción:")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

def show_selected_size (event):
    print(event["value"])


def reset(event):
    r1.state(["!focus", "!selected"])
    r2.state(["!focus", "!selected"])
    r3.state(["!focus", "!selected"])
    r4.state(["!focus", "!selected"])  



r1 = ttk.Radiobutton(window, text='Option 1', value='Value 1' , command=lambda : show_selected_size(r1))
r1.grid(column=1, row=0, padx=5, pady=5)

r2 = ttk.Radiobutton(window, text='Option 2', value='Value 2', command=lambda : show_selected_size(r2))
r2.grid(column=1, row=1, padx=5, pady=5)

r3 = ttk.Radiobutton(window, text='Option 3', value='Value 3', command=lambda : show_selected_size(r3) )
r3.grid(column=1, row=2,padx=5, pady=5)

r4 = ttk.Radiobutton(window, text='Option 4', value='Value 4',command=lambda : show_selected_size(r4) )
r4.grid(column=1, row=3,padx=5, pady=5)

boton_reset = ttk.Button(window, text="Reset")
boton_reset.grid(column=0, row=1, padx=5, pady=5)
boton_reset.bind('<Button-1>', reset)


window.mainloop()