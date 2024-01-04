from tkinter import *
from timee import *
from req import *

root = Tk()
root.title("Live Weather")
root.geometry("300x320")
root.resizable(0, 0)
root.config(bg="#66FFB2")

# --------------------Frame--------------------
frm1 = Frame(root, width=300, height=40, bg="#66FFB2")
frm1.pack(side=TOP)
frm2 = Frame(root, width=300, height=40, bg="#66FFB2")
frm2.pack(side=TOP)
frm3 = Frame(root, width=300, height=40, bg="#66FFB2")
frm3.pack(side=TOP)
frm4 = Frame(root, width=300, height=40, bg="#66FFB2")
frm4.pack(side=TOP)
frm5 = Frame(root, width=300, height=40, bg="#66FFB2")
frm5.pack(side=TOP)
frm6 = Frame(root, width=300, height=40, bg="#66FFB2")
frm6.pack(side=TOP)
frm7 = Frame(root, width=300, height=40, bg="#66FFB2")
frm7.pack(side=TOP)
frm8 = Frame(root, width=300, height=40, bg="#66FFB2")
frm8.pack(side=TOP)

# Label

lbl1 = Label(frm6, text="Temp Is ?? C", bg="#66FFB2")
lbl1.pack(padx=5, pady=5)

lbl2 = Label(frm5, text="For Get Temp Of Any Hour , Click On Hour Button", bg="#66FFB2")
lbl2.pack(padx=5, pady=5)

lbl3 = Label(frm7, text="Click To See Live Weather", bg="#66FFB2")
lbl3.pack(padx=5, pady=5)

# variable

temp = None

# Defination


def glw():
    temp = temps[hour]
    lbl3.config(text=f"Live Weather Of {hour} , Is {temp} C")


def h00():
    temp = temps[0]
    lbl1.config(text=f"Temp Is {temp} C")


def h01():
    temp = temps[1]
    lbl1.config(text=f"Temp Is {temp} C")


def h02():
    temp = temps[2]
    lbl1.config(text=f"Temp Is {temp} C")


def h03():
    temp = temps[3]
    lbl1.config(text=f"Temp Is {temp} C")


def h04():
    temp = temps[4]
    lbl1.config(text=f"Temp Is {temp} C")


def h05():
    temp = temps[5]
    lbl1.config(text=f"Temp Is {temp} C")


def h06():
    temp = temps[6]
    lbl1.config(text=f"Temp Is {temp} C")


def h07():
    temp = temps[7]
    lbl1.config(text=f"Temp Is {temp} C")


def h08():
    temp = temps[8]
    lbl1.config(text=f"Temp Is {temp} C")


def h09():
    temp = temps[9]
    lbl1.config(text=f"Temp Is {temp} C")


def h10():
    temp = temps[10]
    lbl1.config(text=f"Temp Is {temp} C")


def h11():
    temp = temps[11]
    lbl1.config(text=f"Temp Is {temp} C")


def h12():
    temp = temps[12]
    lbl1.config(text=f"Temp Is {temp} C")


def h13():
    temp = temps[13]
    lbl1.config(text=f"Temp Is {temp} C")


def h14():
    temp = temps[14]
    lbl1.config(text=f"Temp Is {temp} C")


def h15():
    temp = temps[15]
    lbl1.config(text=f"Temp Is {temp} C")


def h16():
    temp = temps[16]
    lbl1.config(text=f"Temp Is {temp} C")


def h17():
    temp = temps[17]
    lbl1.config(text=f"Temp Is {temp} C")


def h18():
    temp = temps[18]
    lbl1.config(text=f"Temp Is {temp} C")


def h19():
    temp = temps[19]
    lbl1.config(text=f"Temp Is {temp} C")


def h20():
    temp = temps[20]
    lbl1.config(text=f"Temp Is {temp} C")


def h21():
    temp = temps[21]
    lbl1.config(text=f"Temp Is {temp} C")


def h22():
    temp = temps[22]
    lbl1.config(text=f"Temp Is {temp} C")


def h23():
    temp = temps[23]
    lbl1.config(text=f"Temp Is {temp} C")


# Button

btn = Button(frm8, text="Live Weather", command=glw)
btn.pack(padx=10)

btn1 = Button(frm1, text="00", command=h00)
btn1.pack(padx=10, side=LEFT, pady=10)
btn2 = Button(frm1, text="01", command=h01)
btn2.pack(padx=10, side=LEFT)
btn3 = Button(frm1, text="02", command=h02)
btn3.pack(padx=10, side=LEFT)
btn4 = Button(frm1, text="03", command=h03)
btn4.pack(padx=10, side=LEFT)
btn5 = Button(frm1, text="04", command=h04)
btn5.pack(padx=10, side=LEFT)
btn6 = Button(frm1, text="05", command=h05)
btn6.pack(padx=10, side=LEFT)

# *******************************************

btn7 = Button(frm2, text="06", command=h06)
btn7.pack(padx=10, side=LEFT, pady=10)
btn8 = Button(frm2, text="07", command=h07)
btn8.pack(padx=10, side=LEFT)
btn9 = Button(frm2, text="08", command=h08)
btn9.pack(padx=10, side=LEFT)
btn10 = Button(frm2, text="09", command=h09)
btn10.pack(padx=10, side=LEFT)
btn11 = Button(frm2, text="10", command=h10)
btn11.pack(padx=10, side=LEFT)
btn12 = Button(frm2, text="11", command=h11)
btn12.pack(padx=10, side=LEFT)

# *******************************************

btn13 = Button(frm3, text="12", command=h12)
btn13.pack(padx=10, side=LEFT, pady=10)
btn14 = Button(frm3, text="13", command=h13)
btn14.pack(padx=10, side=LEFT)
btn15 = Button(frm3, text="14", command=h14)
btn15.pack(padx=10, side=LEFT)
btn16 = Button(frm3, text="15", command=h15)
btn16.pack(padx=10, side=LEFT)
btn17 = Button(frm3, text="16", command=h16)
btn17.pack(padx=10, side=LEFT)
btn18 = Button(frm3, text="17", command=h17)
btn18.pack(padx=10, side=LEFT)

# *******************************************

btn19 = Button(frm4, text="18", command=h18)
btn19.pack(padx=10, side=LEFT, pady=10)
btn20 = Button(frm4, text="19", command=h19)
btn20.pack(padx=10, side=LEFT)
btn21 = Button(frm4, text="20", command=h20)
btn21.pack(padx=10, side=LEFT)
btn22 = Button(frm4, text="21", command=h21)
btn22.pack(padx=10, side=LEFT)
btn23 = Button(frm4, text="22", command=h22)
btn23.pack(padx=10, side=LEFT)
btn24 = Button(frm4, text="23", command=h23)
btn24.pack(padx=10, side=LEFT)

root.mainloop()
