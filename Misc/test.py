import turtle
from tkinter import *
from tkinter import messagebox
import random
lstNumberX = [int(x) for x in range(300, 400, 20)]
lstNumberY = [int(x) for x in range(300, 400, 10)]

def draw_heart():
    pen = turtle.Turtle()
    turtle.bgcolor("#333")
    pen.color("pink", "pink")
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-91.5, 200)
    pen.setpos(0,0)
    pen.end_fill()
    pen.home()
    pen.begin_fill()
    pen.left(40)
    pen.forward(180)
    pen.circle(91.5, 200)
    pen.setpos(0,0)
    pen.end_fill()
    draw_rose()

def draw_rose():
    # Set initial position
    turtle.penup ()
    turtle.left (90)
    turtle.fd (200)
    turtle.pendown ()
    turtle.right (90)

    # flower base
    turtle.fillcolor ("pink")
    turtle.begin_fill ()
    turtle.circle (10,180)
    turtle.circle (25,110)
    turtle.left (50)
    turtle.circle (60,45)
    turtle.circle (20,170)
    turtle.right (24)
    turtle.fd (30)
    turtle.left (10)
    turtle.circle (30,110)
    turtle.fd (20)
    turtle.left (40)
    turtle.circle (90,70)
    turtle.circle (30,150)
    turtle.right (30)
    turtle.fd (15)
    turtle.circle (80,90)
    turtle.left (15)
    turtle.fd (45)
    turtle.right (165)
    turtle.fd (20)
    turtle.left (155)
    turtle.circle (150,80)
    turtle.left (50)
    turtle.circle (150,90)
    turtle.end_fill ()

    # Petal 1
    turtle.left (150)
    turtle.circle (-90,70)
    turtle.left (20)
    turtle.circle (75,105)
    turtle.setheading (60)
    turtle.circle (80,98)
    turtle.circle (-90,40)

    # Petal 2
    turtle.left (180)
    turtle.circle (90,40)
    turtle.circle (-80,98)
    turtle.setheading (-83)

    # Leaves 1
    turtle.fd (30)
    turtle.left (90)
    turtle.fd (25)
    turtle.left (45)
    turtle.fillcolor ("green")
    turtle.begin_fill ()
    turtle.circle (-80,90)
    turtle.right (90)
    turtle.circle (-80,90)
    turtle.end_fill ()
    turtle.right (135)
    turtle.fd (60)
    turtle.left (180)
    turtle.fd (85)
    turtle.left (90)
    turtle.fd (80)

    # Leaves 2
    turtle.right (90)
    turtle.right (45)
    turtle.fillcolor ("green")
    turtle.begin_fill ()
    turtle.circle (80,90)
    turtle.left (90)
    turtle.circle (80,90)
    turtle.end_fill ()
    turtle.left (135)
    turtle.fd (60)
    turtle.left (180)
    turtle.fd (60)
    turtle.right (90)
    turtle.circle (200,60)
    messagebox.showinfo("Hadiah Buat eva", "HUHEUHEUHUEHUEHUE Coba cek email uni.evafransisca23@gmail.com\nTrus close everything dulu")
    turtle.done()
    
a = 350
b = 300
def rndm_place():
    a = random.choice(lstNumberX)
    b = random.choice(lstNumberY)
    no_Button.place(x=a, y=b)
    eInp = messagebox.askyesno("Eva Cuantek", "Yakin?")
    if eInp:
        while True:
            eInp2 = messagebox.askyesno("Eva Cuantek", "Yakin?????")
            if eInp2:
                continue
            else:
                return False
        
    else:
        messagebox.showinfo("Eehehe","ehehehhehehe :D")

master = Tk()
master.title('For Eva')
master.geometry("600x400")
Label(master, text='Will you be valentine? Ga skarang tapi tgl 18 February 2023').pack()
Button(master, text='Yes', width=20, command=draw_heart).place(x=100, y=300)
no_Button = Button(master, text='No', width=20, command=rndm_place)
no_Button.place(x=a, y=b)
master.mainloop()


