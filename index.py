from tkinter import *

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

# Defination


# Button

btn = Button(frm8, text="Live Weather")
btn.pack(padx=10)

btn1 = Button(frm1, text="00")
btn1.pack(padx=10, side=LEFT, pady=10)
btn2 = Button(frm1, text="01")
btn2.pack(padx=10, side=LEFT)
btn3 = Button(frm1, text="02")
btn3.pack(padx=10, side=LEFT)
btn4 = Button(frm1, text="03")
btn4.pack(padx=10, side=LEFT)
btn5 = Button(frm1, text="04")
btn5.pack(padx=10, side=LEFT)
btn6 = Button(frm1, text="05")
btn6.pack(padx=10, side=LEFT)

# *******************************************

btn7 = Button(frm2, text="06")
btn7.pack(padx=10, side=LEFT, pady=10)
btn8 = Button(frm2, text="07")
btn8.pack(padx=10, side=LEFT)
btn9 = Button(frm2, text="08")
btn9.pack(padx=10, side=LEFT)
btn10 = Button(frm2, text="09")
btn10.pack(padx=10, side=LEFT)
btn11 = Button(frm2, text="10")
btn11.pack(padx=10, side=LEFT)
btn12 = Button(frm2, text="11")
btn12.pack(padx=10, side=LEFT)

# *******************************************

btn13 = Button(frm3, text="12")
btn13.pack(padx=10, side=LEFT, pady=10)
btn14 = Button(frm3, text="13")
btn14.pack(padx=10, side=LEFT)
btn15 = Button(frm3, text="14")
btn15.pack(padx=10, side=LEFT)
btn16 = Button(frm3, text="15")
btn16.pack(padx=10, side=LEFT)
btn17 = Button(frm3, text="16")
btn17.pack(padx=10, side=LEFT)
btn18 = Button(frm3, text="17")
btn18.pack(padx=10, side=LEFT)

# *******************************************

btn19 = Button(frm4, text="18")
btn19.pack(padx=10, side=LEFT, pady=10)
btn20 = Button(frm4, text="19")
btn20.pack(padx=10, side=LEFT)
btn21 = Button(frm4, text="20")
btn21.pack(padx=10, side=LEFT)
btn22 = Button(frm4, text="21")
btn22.pack(padx=10, side=LEFT)
btn23 = Button(frm4, text="22")
btn23.pack(padx=10, side=LEFT)
btn24 = Button(frm4, text="23")
btn24.pack(padx=10, side=LEFT)

root.mainloop()
