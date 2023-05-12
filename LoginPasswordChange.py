from tkinter import *
from PIL import Image ,ImageTk


root = Tk()
root.geometry("4000x3000")
root.title("Capital Reed (Pvt) Ltd")

topPanal = Label(root, bg="#33d0f6", width=4000,height=10)
topPanal.place(x=1,y=1)

logo= Image.open("C:\capital reed\logo.png")
logoimage = ImageTk.PhotoImage(logo.resize((100,100 )))
logoLable=Label(root,image=logoimage )
logoLable.place(x=1,y=1)


sidePanal = Label(root, bg="#ccccff", width=40,height=400)
sidePanal.place(x=1,y=160)
 #Frame
Frame(root,width=4000,height=2,bg="#000000").place(x=1,y=160)
Frame(root,width=2,height=2000,bg="#000000").place(x=1,y=160)
Frame(root,width=2,height=2000,bg="#000000").place(x=288,y=160)
# button
payment=Button(root,text="payment",font=("Helvetica 12 bold",15),bd=0,bg="#ccccff")
payment.place(x=60,y=170)

Expenses=Button(root,text="Expenses",font=("Helvetica 12 bold",15),bd=0,bg="#ccccff")
Expenses.place(x=60,y=200)

chequeDetail=Button(root,text="cheque Detail",font=("Helvetica 12 bold",15),bd=0,bg="#ccccff")
chequeDetail.place(x=60,y=230)

chequePrint=Button(root,text="Cheque Print",font=("Helvetica 12 bold",15),bd=0,bg="#ccccff")
chequePrint.place(x=60,y=260)
Frame(root,width=288,height=2,bg="#000000").place(x=1,y=320)

Account = Button(root, text="Account",
                    font=("Helvetica 12 bold", 15),
                    bd=0, bg="#ccccff")

Account.place(x=60, y=330)


SubRegister=Button(root,text="Sub Register",font=("Helvetica 12 bold",15),bd=0,bg="#ccccff")
SubRegister.place(x=60,y=360)

PaymentList=Button(root,text="Payment List",font=("Helvetica 12 bold",15),bd=0,bg="#ccccff")
PaymentList.place(x=60,y=390)
Frame(root,width=288,height=2,bg="#000000").place(x=1,y=5100)
Frame(root,width=288,height=2,bg="#000000").place(x=1,y=550)

Frame(root,width=288,height=2,bg="#000000").place(x=1,y=430)

CashBookReport=Button(root,text="Cash Book Report",font=("Helvetica 12 bold",15),bd=0,bg="#ccccff")
CashBookReport.place(x=60,y=440)

# Create a button of the TrailBalencewith
TrailBalence = Button(root, text="Trail Balence",
                           font=("Helvetica 12 bold", 15),
                           bd=0, bg="#ccccff")

# Place the  button of the TrailBalence at the coordinates (60, 430)
TrailBalence.place(x=60, y=470)

# Create a button of the Leger with the text " "
Leger = Button(root, text="Leger",
                           font=("Helvetica 12 bold", 15),
                           bd=0, bg="#ccccff")

# Place the  button of the leger at the coordinates (60, 430)
Leger.place(x=60, y=500)


# Create a button of the Cash count
Cashcount= Button(root, text="Cash count",
                           font=("Helvetica 12 bold", 15),
                           bd=0, bg="#ccccff")

# Place the  button of the Caash count at the coordinates (60, 430)
Cashcount.place(x=60, y=560)

Frame(root,width=288,height=2,bg="#000000").place(x=1,y=600)

# Create a button of the Daay End
DayEnd = Button(root, text="Day End",
                           font=("Helvetica 12 bold", 15),
                           bd=0, bg="#ccccff")

# Place the  button of the Day End at the coordinates (60, 430)
DayEnd.place(x=60, y=610)

# Create a button of the Stuff Attendance
StuffAttendance = Button(root, text="Stuff attendance",
                           font=("Helvetica 12 bold", 15),
                           bd=0, bg="#ccccff")

# Place the  button of the stuff Attendance at the coordinates (60, 430)
StuffAttendance.place(x=60, y=640)

# Create a button of the Salary Advances
SalaryAdvances=Button(root, text="Salary Advances",
                          font=("Helvetica 12 bold", 15),
                          bd=0, bg="#ccccff")

# Place the  button of the stuff Attendance at the coordinates (60, 430)
SalaryAdvances.place(x=60, y=670)

# Create a button of the Outside Bank Deposit
OutsideBankDeposit= Button(root, text="Outside Bank Deposit",
                          font=("Helvetica 12 bold", 15),
                          bd=0, bg="#ccccff")

# Place the  button of the stuff Attendance at the coordinates (60, 430)
OutsideBankDeposit.place(x=60, y=700)

# Create a button of the cash Drawer
CashDrawer= Button(root, text="cash Drawer",
                          font=("Helvetica 12 bold", 15),
                          bd=0, bg="#ccccff")

  # Place the  button of the cash Drawer at the coordinates (60, 430)

CashDrawer.place(x=60, y=730)
root.mainloop()