from tkinter import *

root = Tk()
root.title("insterest calculator")
root.geometry("500x300")

# def
def Calciulte ():
    prin = int(principalentry.get())
    rat = int(rateentry.get())
    tin = int(timeentry.get())
    amount = (prin*rat*tin)/100
    Label(text=f"{amount}",font="arial 30 bold").place(x=200,y=220)

#text 
principal = Label(root,text="principal:",font="arial 15")
principal.place(x=50,y=20)

rate = Label(root,text="rate of interest:",font="arial 15")
rate.place(x=50,y=90)

time = Label(root,text="time:",font="arial 15")
time.place(x=50,y=160)

interest = Label(root,text="Interest:",font="arial 15")
interest.place(x=50,y=230)

#StringVar
principalvalue = StringVar()

ratevalue = StringVar()

timevalue = StringVar()

#Entry
principalentry = Entry(root,textvariable=principalvalue,font="arial 20",width=8)
principalentry.place(x=200,y=20)

rateentry = Entry(root,textvariable=ratevalue,font="arial 20",width=8)
rateentry.place(x=200,y=90)

timeentry = Entry(root,textvariable=timevalue,font="arial 20",width=8)
timeentry.place(x=200,y=160)

#Button
Button(text="Calculator",font="arial 15",command=Calciulte).place(x=350,y=20)
Button(text="Exit",command=lambda:exit(),font="arial 15",width=8).place(x=350,y=90)

root.mainloop()