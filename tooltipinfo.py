from tkinter import *
from tkinter.tix import *

#create  instance  for windows
root=Tk()

#set window title
root.title("Tool Tip text")

#Create instance  of Balloon
tip=Balloon(root)

#configure balloon messsage
tip.message.config(bg="black",fg="gold",font=("haveltica 15 bold"))

#create button
btn=Button(root,text="click Here",font=("arial 15 bold"))
btn.pack(padx=80,pady=80)

#bind btn with ballon instance
tip.bind_widget(btn,balloonmsg = "This is Button widget")

root.mainloop()

