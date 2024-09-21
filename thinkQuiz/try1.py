from tkinter import *  #imported tkintermodule #gui module 


root=Tk()# created a main application window
root.title("Reviews project properly")#give title to appliaction
root.geometry("500x300")#provide sizing to our window

icons= PhotoImage(file="thinquiz.png")#loads an image file
root.iconphoto(True,icons)#set image as an icon to our window

# Tkinter widget
l=Label(text="A")
l.place(x=2,y=7)
a=Button(root,text="Submit",command=quit)
a.place(x=19,y=7)# geomertic measure used to organize widgets:pack(block), place(as user define),grid(for grid)


root.mainloop()