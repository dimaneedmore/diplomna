from tkinter import *
import random
import datetime

tk = Tk()
canvas = Canvas(tk, height=400, width=800)
tk.resizable(width=False, height=False)
canvas.pack()


def data():
    days = ["понеділок","вівторок","середа","четвер","п'ятниця","субота","неділя"]
    now = datetime.datetime.now()
    t = random.uniform(27, 30)
    h = random.uniform(50, 60)
    p = random.uniform(1049, 1050)
    time = (str(now.time()))[0:5]
    dat = now.date()
    day = days[now.weekday()]

    Label(text="temp").place(x=20, y=20)
    Label(text="%.2f" % t).place(x=50, y=20)

    Label(text="humid").place(x=620, y=20)
    Label(text="%.2f" % h).place(x=660, y=20)

    Label(text="pressure").place(x=375, y=310)
    Label(text="%.0f" % p).place(x=375, y=330)

    Label(text=time, font=20).place(x=375, y=110)
    Label(text=day).place(x=375, y=50)
    Label(text=dat).place(x=375, y=80)
    tk.after(5000, data)



def lines():
    canvas.create_line(325, 0, 325, 400)
    canvas.create_line(475, 0, 475, 400)

    canvas.create_line(325, 150, 475, 150)
    canvas.create_line(325, 300, 475, 300)


if __name__ == '__main__':
    lines()
    data()
    tk.mainloop()