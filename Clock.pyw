from ttkbootstrap import Window, Label, Button
from datetime import datetime

root = Window()
root.title('Clock')
root.resizable(False, False)
now = str(datetime.now())
label = Label(root, text=now, font=('Times', 80))
label.pack()

              
def start():
    button.pack_forget()
    while True:
        time = str(datetime.now())
        label.config(text=time)
        root.update()

      
button = Button(root, text='Start', command=start, width=178)
button.pack()
root.mainloop()
