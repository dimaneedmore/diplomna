import sys
from tkinter import *
import random
import datetime
import requests
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



t_list = []
tm_list =[]
h_list =[]

tk = Tk()
canvas = Canvas(tk, height=420, width=620)
tk.resizable(width=False, height=False)
canvas.pack()

figure_temp = Figure(figsize=(3, 2), dpi=100)
plot_canvas_t = FigureCanvasTkAgg(figure_temp, tk)
axes_t = figure_temp.add_subplot(111)
plot_canvas_t.get_tk_widget().place(x=0, y=90)


figure_humi = Figure(figsize=(3, 2), dpi=100)
plot_canvas = FigureCanvasTkAgg(figure_humi, tk)
axes_h = figure_humi.add_subplot(111)
axes_h.set_xlabel('Вологість hPa')
axes_h.set_ylabel('Час')
plot_canvas.get_tk_widget().place(x=320, y=90)


def create():
    win = Toplevel(tk)
    win.title('Telegram')
    qr = PhotoImage(file='qr_code.png')
    qr =qr.subsample(7, 8)
    lbl = Label(win)
    lbl.image = qr
    lbl['image'] = lbl.image
    lbl.place(x=20,y=20)
    c = Canvas(win, height=230, width=220)
    win.resizable(width=False, height=False)
    c.pack()
    Label(win,image=qr).place(x=20,y =10)
    Button(win, text = "Закрити вікно", command=win.destroy).place(x=70,y=190)

img = PhotoImage(file='t_icon.png')
w_icon = img.subsample(8, 8)
but = Button(tk, image=w_icon, command=create, width=50, height=50).place(x=550,y=1)


def data():
    days = ["Понеділок","Вівторок","Середа","Четвер","П'ятниця","Субота","Неділя"]
    now = datetime.datetime.now()
    t = random.uniform(27, 30)
    t_list.append(t)
    h = random.uniform(50, 60)
    h_list.append(h)
    p = random.uniform(1049, 1050)
    time = (str(now.time()))[0:5]
    tm_list.append(time)

    dat = now.date()
    day = days[now.weekday()]

    Label(text="Температура").place(x=20, y=70)
    Label(text="%.2f" % t).place(x=100, y=70)

    Label(text="Вологість").place(x=450, y=70)
    Label(text="%.2f" % h).place(x=510, y=70)

    Label(text="Атмосферний тиск").place(x=425, y=15)
    Label(text="%.0f" % p).place(x=425, y=35)

    Label(text=time, font=40).place(x=100, y=15)
    Label(text=day, font=20).place(x=15, y=10)
    Label(text=dat).place(x=15, y=35)


    s_city = "Khmelnytskyi, UA"
    city_id = 0
    appid = "e7e9533d546b6633e29b113ab7a1ee64"
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid,'lang':'ua'})
    dat = res.json()

    icon_name = dat['list'][0]['weather'][0]['icon']+".png"
    w_icon = PhotoImage(file=f'icons\{icon_name}')
    w_icon =w_icon.subsample(2, 2)
    lbl = Label(tk)
    lbl.image = w_icon
    lbl['image'] = lbl.image
    lbl.config(bg="yellow")

    Label(text="Хмельницький", font=25).place(x=205, y=5)
    lbl.place(x =365, y = 5)

    w_text = dat['list'][0]['weather'][0]['description']
    Label(text=w_text.title()).place(x=205, y=30)
    new_t_g(t_list, tm_list)
    new_h_g(h_list, tm_list)

    ostatok = 60-now.second
    tk.after(ostatok*1000, data)


def new_t_g(t_list, tm_list):
    axes_t.clear()
    axes_t.plot(tm_list, t_list, color='y')
    plot_canvas_t.draw_idle()


def new_h_g(h_list, tm_list):
    axes_h.clear()
    axes_h.plot(tm_list, h_list, color='y')
    plot_canvas.draw_idle()


def lines():
    canvas.create_line(0,60,620,60)
    canvas.create_line(200,0,200,60)
    canvas.create_line(420,0,420,60)
    canvas.create_line(310,60,310,420)


if __name__ == '__main__':
    lines()
    data()
    tk.mainloop()