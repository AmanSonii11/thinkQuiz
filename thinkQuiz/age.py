from tkinter import *
import subprocess

# running other file using run()


def life1():
    subprocess.run(["python", "tkinterforkbc.py"])
    quit()
def life2():
    subprocess.run(["python", "try.py"])
    quit()

def life3():
    subprocess.run(["python", "age3.py"])
    quit()

root = Tk()
root.geometry("1500x1500")
root.title("Home")
photo = PhotoImage(file = "thinQuiz.png")

root.iconphoto(False, photo)
root.config(bg="black")

#leftFrame=Frame(root,bg="black",padx=90)
#leftFrame.grid(row=0,column=0)

#lifelines


#logo
centerFrame=Frame(root,bg="Black")
centerFrame.grid(row=0,column=0)
a=Label(centerFrame,bg="Black",text="Select your age group",foreground="white",font=("Arial",20,"bold"),height=5,width=70)
a.grid(row=0,column=2,padx=70)

logo=PhotoImage(file="thinQuiz.png")
centerlogo=Label(centerFrame,image=logo,bg="Black",height=320)
centerlogo.grid(row=1,column=2)


#question


topFrame=Frame(root,bg="Black")
topFrame.grid(row=1,column=0,padx=70)
option1=Button(topFrame,text="General",font=('arial','16','bold'),bg="black",fg="white",bd=3,activebackground="black",command=life1)
option1.grid(row=0,column=0,padx=20)
option2=Button(topFrame,text="Below 20",font=('arial','16','bold'),bg="black",fg="white",bd=3,activebackground="black",command=life2)
option2.grid(row=0,column=1,padx=20)
option3=Button(topFrame,text="Above 20",font=('arial','16','bold'),bg="black",fg="white",bd=3,activebackground="black",command=life3)
option3.grid(row=0,column=2,padx=20)



root.mainloop()

