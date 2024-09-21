from tkinter import *
import subprocess

# running other file using run()
def life1():
    subprocess.run(["python", "age.py"])
    quit()

root=Tk()
root.geometry("1500x1500")
root.title("Home")
root.config(bg="black")

centerFrame=Frame(root,bg="Black")
centerFrame.grid(row=0,column=0,padx=160)
logo=PhotoImage(file="thinQuiz.png")
centerlogo=Label(centerFrame,image=logo,bg="Black",height=500, width=1000)
centerlogo.grid()
a=Label(root,bg="Black",text="Press Start to begin the game",bd=5,foreground="white",font=("Arial",20,"bold"))
a.grid(row=1,column=0)

topFrame=Frame(root,bg="Black")
topFrame.grid(row=2,column=0,padx=160)
image50=PhotoImage(file="start.png")
life1=Button(topFrame,image=image50,bg="Black",border=0,activebackground="black",width=380,height=110,command=life1)
life1.grid(row=1,column=0)


root.mainloop()

