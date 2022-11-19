import tkinter
from tkinter import ttk
import py_compile
import subprocess

subprocess.run(args=['pip', 'install', 'pyinstaller'])


root = tkinter.Tk()
root.title('Compiler')
root.resizable(False, False)
ttk.Label(root, text='Select a file:').grid(row=0)
entry = ttk.Entry(root)
entry.grid(row=0, column=1)


def python_compile():
    file = entry.get()
    py_compile.compile(file)


def exe_single_n():
    file = entry.get()
    subprocess.run(args=['pyinstaller', '-F', '-w', file])


def exe_single():
    file = entry.get()
    subprocess.run(args=['pyinstaller', '-F', file])


def exe_path_n():
    file = entry.get()
    subprocess.run(args=['pyinstaller', '-D', '-w', file])


def exe_path():
    file = entry.get()
    subprocess.run(args=['pyinstaller', '-D', file])


ttk.Button(root, text='Compile', command=python_compile).grid(row=1)
ttk.Button(root, text='Generate(Single-NoCommand)', command=exe_single_n).grid(row=1, column=1)
ttk.Button(root, text='Generate(Single-Normal)', command=exe_single).grid(row=1, column=2)
ttk.Button(root, text='Quit', command=root.quit).grid(row=2)
ttk.Button(root, text='Generate(Path-NoCommand)', command=exe_path_n).grid(row=2, column=1)
ttk.Button(root, text='Generate(Path-Normal)', command=exe_path).grid(row=2, column=2)
root.mainloop()
