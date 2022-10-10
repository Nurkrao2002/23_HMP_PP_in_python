from tkinter import *
root=Tk()
p=Label(root,text="Josh Innovations")
e=Entry(root)
e.pack()
e.insert(0,"Enter your Name:")
def myclick():
    p=Label(root,text="Hello "+e.get(),fg="orange",bg="black")
    p.pack()
b=Button(root,text="Submit",command=myclick,fg="blue",bg="yellow")
b.pack()
root.mainloop()
