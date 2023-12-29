
#TASK - 3

from cProfile import label
from tkinter import *
import tkinter.messagebox


 
root = Tk() 


root.geometry('400x500') 


 
datas = [] 
  
 
def add(): 
    global datas 
    datas.append([Name.get(),Number.get(),Email.get(),address.get(1.0, "end-1c")]) 
    update_book() 
  

def show(): 
    Name.set(datas[int(select.curselection()[0])][0]) 
    Number.set(datas[int(select.curselection()[0])][1]) 
    Email.set(datas[int(select.curselection()[0])][2])
    address.delete(1.0,"end") 
    address.insert(1.0, datas[int(select.curselection()[0])][3]) 


 
def search_contact():
    shell = []
    shell.append(Name.get())
    for i in range(len(shell)):
       if shell[i] == datas[i][0]:  
            tkinter.messagebox.showinfo("Found", "Data is Found.")
    

   
def delete(): 
    del datas[int(select.curselection()[0])] 
    update_book() 
  
def Rest(): 
    Name.set('') 
    Number.set('') 
    Email.set('')
    address.delete(1.0,"end") 


def update_book(): 
    select.delete(0,END) 
    for n,p,e,a in datas: 
        shell = [n, p]
        select.insert(END,shell) 
        
  
 

Name = StringVar() 
Number = StringVar()
Email = StringVar()

frame = Frame() 
frame.pack(pady=10) 

frame1 = Frame() 
frame1.pack() 

frame2 = Frame() 
frame2.pack(pady=10) 

frame3 = Frame() 
frame3.pack(pady=10) 

Label(frame, text = 'Name :     ', font='arial 12 bold').pack(side=LEFT) 
Entry(frame, textvariable = Name,width=50).pack() 


Label(frame1, text = 'Phone No :  ', font='arial 12 bold').pack(side=LEFT) 
Entry(frame1, textvariable = Number,width=50).pack() 

Label(frame2, text = 'Email :     ', font='arial 12 bold').pack(side=LEFT) 
Entry(frame2, textvariable = Email,width=50).pack()


Label(frame3, text = 'Address :   ', font='arial 12 bold').pack(side=LEFT) 
address = Text(frame3,width=50,height=5) 
address.pack() 
 

Button(root,text="Add    ",font="arial 12 bold",command=add).place(x= 100, y=270) 
Button(root,text="Show   ",font="arial 12 bold",command=show).place(x= 100, y=310) 
Button(root,text="Search ",font="arial 12 bold",command=search_contact).place(x= 100, y=350) 
Button(root,text="Delete ",font="arial 12 bold",command=delete).place(x= 100, y=390) 
Button(root,text="Reset ",font="arial 12 bold",command=Rest).place(x= 100, y=430) 

scroll_bar = Scrollbar(root, orient=VERTICAL) 
select = Listbox(root, yscrollcommand=scroll_bar.set,width=130,height=12) 
scroll_bar.config (command=select.yview) 
scroll_bar.pack(side=RIGHT, fill=Y) 
select.place(x=200,y=260) 


root.mainloop()
