from ttkbootstrap import Window, Label, Button
from datetime import datetime


root = Window()
root.title('Clock')
root.resizable(False, False)
now = str(datetime.now())
label = Label(root, text=now, font=('Times', 80))
label.pack()


def start():
    global t
    t = 0
    button.pack_forget()
    s.pack()
    while t != 1:
        label.config(text=str(datetime.now()))
        root.update()


def stop():
    global t
    t = 1
    s.pack_forget()
    button.pack()

      
button = Button(root, text='Start', command=start, width=178)
s = Button(root, text='Stop', command=stop, width=178)
button.pack()
root.mainloop()
