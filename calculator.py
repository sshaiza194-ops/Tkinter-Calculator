from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("300x370")
def clear():
    display.delete(0, END)
def backspace():
    text=display.get() #first get the text from screen
    display.delete(0,END) #delete all
    text=text[:-1]  #delete the last character
    display.insert(END,text) #insert the updated text now

def seven():
    display.insert(END,"7")
def eight():
    display.insert(END,"8")
def nine():
    display.insert(END,"9")
def zero():
    display.insert(END,"0")
def two():
    display.insert(END,"2")
def three():
    display.insert(END,"3")
def four():
    display.insert(END,"4")
def five():
    display.insert(END,"5")
def six():
    display.insert(END,"6")
def add():
    display.insert(END,"+")
def multiply():
    display.insert(END,"*")
def divide():
    display.insert(END,"/")
def minus():
    display.insert(END,"-")
def one():
    display.insert(END,"1")
def answer():
    expression=display.get()
    result=eval(expression)
    display.delete(0,END)
    display.insert(END ,result)

root.maxsize(300,440)
root.configure(bg="grey")
#we need an entry in frame1

frame1=Frame(root,width=80,height=80,bg="white",borderwidth=5,relief=SUNKEN)
frame1.pack(padx=8,pady=8,fill=X)

display = Entry(frame1, width=15, font=("Arial", 14))
display.pack(fill=X, padx=5, pady=5)

# relief -- border styling  --  SUNKEN , RAISSED , GROOVE , RIDGE

frame2=Frame(root,borderwidth=5,relief=RIDGE,bg="lightgrey")
frame2.pack(padx=2,pady=2,fill=X)


b1=Button(frame2,fg="black",text="C",height=2,width=5,font=("arial",14),command=clear)
b1.grid(row=0,column=0,padx=3,pady=3)

b2=Button(frame2,fg="black",text="⌫",height=2,width=5,font=("arial",14),command=backspace)
b2.grid(row=0,column=1,padx=3,pady=3)

b3=Button(frame2,fg="black",text="/",height=2,width=5,font=("arial",14),command=divide)
b3.grid(row=0,column=2,padx=3,pady=3)

b4=Button(frame2,fg="black",text="*",height=2,width=5,font=("arial",14),command=multiply)
b4.grid(row=0,column=3,padx=3,pady=3)

b5=Button(frame2,fg="black",text="7",height=2,width=5,font=("arial",14),command=seven)
b5.grid(row=1,column=0,padx=3,pady=3)

b6=Button(frame2,fg="black",text="8",height=2,width=5,font=("arial",14),command=eight)
b6.grid(row=1,column=1,padx=3,pady=3)

b7=Button(frame2,fg="black",text="9",height=2,width=5,font=("arial",14),command=nine)
b7.grid(row=1,column=2,padx=3,pady=3)

b8=Button(frame2,fg="black",text="-",height=2,width=5,font=("arial",14),command=minus)
b8.grid(row=1,column=3,padx=3,pady=3)

b9=Button(frame2,fg="black",text="4",height=2,width=5,font=("arial",14),command=four)
b9.grid(row=2,column=0,padx=3,pady=3)

b10=Button(frame2,fg="black",text="5",height=2,width=5,font=("arial",14),command=five)
b10.grid(row=2,column=1,padx=3,pady=3)

b11=Button(frame2,fg="black",text="6",height=2,width=5,font=("arial",14),command=six)
b11.grid(row=2,column=2,padx=3,pady=3)

b12=Button(frame2,fg="black",text="+",height=2,width=5,font=("arial",14),command=add)
b12.grid(row=2,column=3,padx=3,pady=3)

b13=Button(frame2,fg="black",text="3",height=2,width=5,font=("arial",14),command=three)
b13.grid(row=3,column=0,padx=3,pady=3)

b14=Button(frame2,fg="black",text="2",height=2,width=5,font=("arial",14),command=two)
b14.grid(row=3,column=1,padx=3,pady=3)

b15=Button(frame2,fg="black",text="1",height=2,width=5,font=("arial",14),command=one)
b15.grid(row=3,column=2,padx=3,pady=3)

b16=Button(frame2,fg="black",text="0",height=2,width=5,font=("arial",14),command=zero)
b16.grid(row=3,column=3,padx=3,pady=3)

frame3=Frame(root,borderwidth=5,relief=RIDGE,bg="lightgrey")
frame3.pack(padx=2,pady=2,fill=X)

b=Button(frame3,text="ANSWER",font=("arial",14),borderwidth=5,relief=SUNKEN,command=answer)
b.pack(padx=6,pady=15,fill=X)

root.mainloop()