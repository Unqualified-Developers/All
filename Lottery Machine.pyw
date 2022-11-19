from random import randint
from tkinter.messagebox import showinfo, showerror, showwarning
from ttkbootstrap import Window, Toplevel, Label, Button, Entry, Radiobutton, IntVar
from webbrowser import open

# Initialize the root window.
r_win = Window()
r_win.title('Lottery Machine')
r_win.resizable(False, False)
# Main UI part 1 (The not show label and entry).
NShow = Entry(r_win)
LD = Label(text="Don't want to see:")
var = IntVar()


def not_show():
    # Click the 'Normal' radiobutton.
    LD.grid_forget()
    NShow.grid_forget()


def show():
    # Click the 'I don't want to see …' radiobutton.
    LD.grid(row=3)
    NShow.grid(row=3, column=1, padx=10, pady=5)


# Main UI Part 2 (Labels and normal entries).
Label(r_win, text='Minimum:').grid(row=0)
Label(r_win, text='Maximum:').grid(row=1)
Min = Entry(r_win)
Min.grid(row=0, column=1, padx=10, pady=5)
Max = Entry(r_win)
Max.grid(row=1, column=1, padx=10, pady=5)
Radiobutton(r_win, text='Normal.', value=0, variable=var, command=not_show).grid(row=2)
Radiobutton(r_win, text="I don't want to see …", value=1, variable=var,
            command=show).grid(row=2, column=1, padx=10, pady=5)


def generate():
    # Click the 'Generate' button.
    try:
        a = int(Min.get())
        b = int(Max.get())
        n = NShow.get()
        n_list = n.split(',')
        r = str(randint(a, b))
        variable = var.get()
        arg = 0
        if variable == 1:
            num = n_list.count(r)
            while num != 0:
                r = str(randint(a, b))
                num = n_list.count(r)
                arg = arg + 1
                if arg > 66666:
                    break
            if arg > 66666:
                showerror(title='Error', message='Something went wrong. Please try again.')
            else:
                showinfo(title='Generate', message='Number %s.' % r)
        else:
            showinfo(title='Generate', message='Number %s.' % r)
    except ValueError:
        showwarning(title='Value', message="""You are humorous, but please don't tell funny jokes here.
The value you entered is not true, it must be an integer.
Please try again!""")


def source_code():
    # Click the 'Source Code' button.
    open('https://github.com/Python-Object-Developers/All/blob/main/Lottery%20Machine.pyw')


def learn_more():
    # Click the 'Learn More' button.
    open('https://github.com/Python-Object-Developers/All/wiki/Lottery-Machine')


def end():
    global r_win, a_win
    r_win.attributes("-disabled", 0)
    a_win.destroy()


def show_about():
    # Click the 'About' button.
    global r_win, a_win
    r_win.attributes("-disabled", 1)
    a_win = Toplevel()
    a_win.title('About')
    a_win.resizable(False, False)
    Label(a_win, text='Lottery Machine 3.4', font=('Times', 13)).grid(row=0)
    Label(a_win, text='Open source, all rights reserved.').grid(row=1)
    Button(a_win, text='Source Code', command=source_code, width=30).grid(row=2)
    Button(a_win, text='Learn More', command=learn_more, width=30).grid(row=3)
    a_win.transient(r_win)
    a_win.protocol('WM_DELETE_WINDOW', end)


# Main UI Part 3 (three buttons).
Button(r_win, text='Generate', width=12, command=generate).grid(row=4)
Button(r_win, text='About', width=12, command=show_about).grid(row=4, column=1)
Button(r_win, text='Quit', width=12, command=r_win.quit).grid(row=4, column=2)
r_win.mainloop()
