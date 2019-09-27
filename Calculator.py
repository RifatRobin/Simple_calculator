from tkinter import*

cal=Tk()
cal.title("Simple Calculator by robin")
# cal.geometry('250x270')

def sum():
    a=float(txtFname.get())+float(txtLname.get())
    lblfull.configure(text=a)

def sub():
    a=float(txtFname.get())-float(txtLname.get())
    lblfull.configure(text=a)

def mul():
    a=float(txtFname.get())*float(txtLname.get())
    lblfull.configure(text=a)

def div():
    a=float(txtFname.get())/float(txtLname.get())
    lblfull.configure(text=a)
def squarefornum1():
    a=float(txtFname.get())*float(txtFname.get())
    lblfull.configure(text=a)

def squarefornum2():
    a=float(txtLname.get())*float(txtLname.get())
    lblfull.configure(text=a)

lblFname=Label(cal,text="Number1: ",font=("Arial",12),width=8)#if we want to print something into the gui, we have [Label(windowname,text="which i should want to see")]
lblFname.grid(column=0,row=0, padx = 1, pady = 1)
txtFname=Entry(cal,width=15)
txtFname.grid(column=1,row=0, padx = 1, pady = 1)


lblLname=Label(cal,text="Number2:",font=("Arial",12),width=8)#if we want to print something into the gui, we have [Label(windowname,text="which i should want to see")]
lblLname.grid(column=0,row=1, padx = 1, pady = 1)
txtLname=Entry(cal,width=15)
txtLname.grid(column=1,row=1, padx = 1, pady = 1)

lblfull=Label(cal,text="",font=("Arial",14))
lblfull.grid(column=1,row=12, padx = 1, pady = 1)

btn1=Button(cal,text="+",font=("Arial",10), width=15,command=sum)
btn1.grid(column=1,row=3, padx = 1, pady = 1)

btn2=Button(cal,text="-",font=("Arial",10), width=15,command=sub)
btn2.grid(column=1,row=4, padx = 1, pady = 1)

btn3=Button(cal,text="*",font=("Arial",10), width=15,command=mul)
btn3.grid(column=1,row=5, padx = 1, pady = 1)

btn4=Button(cal,text="/",font=("Arial",10), width=15,command=div)
btn4.grid(column=1,row=6, padx = 1, pady = 1)

btn5=Button(cal,text="square of Number1",font=("Arial",10), width=15,command=squarefornum1)
btn5.grid(column=1,row=7, padx = 1, pady = 1)


btn6=Button(cal,text="square of Number2",font=("Arial",10), width=15,command=squarefornum2)
btn6.grid(column=1,row=8, padx = 1, pady = 1)

btnclose=Button(cal,text="Close",font=("Arial",10), width=8,command=cal.quit)
btnclose.grid(column=4,row=9, padx = 1, pady = 1)

cal.mainloop()
