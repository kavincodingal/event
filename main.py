import tkinter as tk
root=tk.Tk()
root.title("events")
root.geometry("100x100")
def getchar(event):
    print(event.char)
root.bind("<Key>",getchar)
b=tk.Button(root,text="click me",bg="red",fg="cyan")
b.pack()
def click(event):
    print("left button is clicked")
b.bind("<Button-1>",click)

root.mainloop()