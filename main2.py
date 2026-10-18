import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.geometry ("250x250")
def msg():
    messagebox.showwarning("alert","stop! viurs found")
b=tk.Button(root,text="scan for viurs",bg="blue",fg="white",command=msg)
b.pack()
root.mainloop()
