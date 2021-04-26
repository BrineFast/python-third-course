"""
после запуска программы должно появляться окно, содержащее верхнее Меню из 3-х пунктов и виджет Canvas;
1) 1-й пункт меню - Построить график. При выборе этого пункта должно выпадать меню с вариантами функций: y=sin x, y=cos x,
 y=tg x, y=ctg x, y=x2, y=x3) При выборе функции должно появляться окно для выбора диапазона значений аргумента x.
  Диапазон значений y должен определяться в программе в зависимости от диапазона x  и варианта функции.После выбора
  диапазона должен строиться график функции на виджете Canvas основного окна. Обратите внимание, что y=tg x, y=ctg -
  разрывные функции. График можно построить с помощью matplotlib . Должны быть отрисованы оси, сетка, подписи к осям и
  градуировка осей (шаг должен выбираться в зависимости от диапазона значений и с учетом того что цифры должны быть
  читаемы. У графика должна быть легенда или заголовок с названием функции.
2) 2-й пункт Справка. По нажатию на этот пункт должен открываться текстовый файл
 с описанием работы и реализации программы.
3) 3-й пункт меню Выход - закрытие окна;
при этом во всех пунктах должна присутствовать проверка на корректность данных;
при повторном выборе пункта Построить график предыдущие данные, размещенные на виджете Canvas, должны очищаться;
"""

from tkinter import *

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

root = Tk()
navigation_bar = Menu(root)
root.config(menu=navigation_bar)
root.geometry("700x700")

fig, ax = plt.subplots()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

def print_graph(x, y):
    plt.clf()
    plt.grid()
    plt.plot(x, y)
    plt.draw()

def input_validation(x_left_bound_value, x_right_bound_value):
    try:
        x_l = float(x_left_bound_value)
        x_r = float(x_right_bound_value)
        if x_l >= x_r:
            raise Exception
        return x_l, x_r
    except:
        exception.config(text='Неверный ввод')

def sin(event):
    x_left_bound_value = x_left_bound.get()
    x_right_bound_value = x_right_bound.get()

    x_l, x_r = input_validation(x_left_bound_value, x_right_bound_value)
    x = np.linspace(x_l, x_r, num=100)
    y = np.sin(x)
    input_window.destroy()
    print_graph(x, y)

def cos(event):
    x_left_bound_value = x_left_bound.get()
    x_right_bound_value = x_right_bound.get()

    x_l, x_r = input_validation(x_left_bound_value, x_right_bound_value)
    x = np.linspace(x_l, x_r, num=100)
    y = np.cos(x)
    input_window.destroy()
    print_graph(x, y)



def tg(event):
    x_left_bound_value = x_left_bound.get()
    x_right_bound_value = x_right_bound.get()

    x_l, x_r = input_validation(x_left_bound_value, x_right_bound_value)
    x = np.linspace(x_l, x_r, num=100)
    y = np.tan(x)
    y[y > 10] = np.nan
    y[y < -10] = np.nan
    input_window.destroy()
    print_graph(x, y)


def ctg(event):
    x_left_bound_value = x_left_bound.get()
    x_right_bound_value = x_right_bound.get()

    x_l, x_r = input_validation(x_left_bound_value, x_right_bound_value)
    x = np.linspace(x_l, x_r, num=100)
    y = np.cos(x) / np.sin(x)
    y[y > 10] = np.nan
    y[y < -10] = np.nan
    input_window.destroy()
    print_graph(x, y)

def x_squared(event):
    x_left_bound_value = x_left_bound.get()
    x_right_bound_value = x_right_bound.get()

    x_l, x_r = input_validation(x_left_bound_value, x_right_bound_value)
    x = np.linspace(x_l, x_r, num=100)
    y = x * x
    input_window.destroy()
    print_graph(x, y)

def x_cube(event):
    x_left_bound_value = x_left_bound.get()
    x_right_bound_value = x_right_bound.get()

    x_l, x_r = input_validation(x_left_bound_value, x_right_bound_value)
    x = np.linspace(x_l, x_r, num=100)
    y = x * x * x
    input_window.destroy()
    print_graph(x, y)

def choose_x():
    global input_window
    input_window = Toplevel(root)
    input_window.geometry("300x300")

    global x_left_bound
    x_left_bound = (Entry(input_window, width=3, bd=3))
    x_left_bound.pack()
    x_left_bound.place(x=70, y=10)

    global x_right_bound
    x_right_bound = (Entry(input_window, width=3, bd=3))
    x_right_bound.pack()
    x_right_bound.place(x=x_left_bound.winfo_width() + 105, y=10)

    label_x = Label(input_window, text="x: ", justify=LEFT)
    label_x.place(x=x_left_bound.winfo_width() + 50, y=10)
    label_left_bracket_x = Label(input_window, text="[", justify=LEFT)
    label_left_bracket_x.place(x=x_left_bound.winfo_width() + 60, y=10)
    separate_x = Label(input_window, text=";", justify=LEFT)
    separate_x.place(x=x_left_bound.winfo_width() + 95, y=10)
    label_right_bracket_x = Label(input_window, text="]", justify=LEFT)
    label_right_bracket_x.place(x=x_right_bound.winfo_width() + 130, y=10)

    global exception
    exception = Label(input_window, text="", justify=LEFT)
    exception.place(x=50, y=50)


def make_print_button(graph_type):
    drawButton = Button(input_window)  # Конструктор
    drawButton["text"] = "Построить график"  # Надпись
    drawButton.bind("<Button-1>", graph_type)  # Функция при нажатии
    input_window.bind("drawButton", graph_type)  # Окно отображения кнопки
    drawButton.pack()
    drawButton.place(x=40, y=130)  # Расположение


def sin_button():
    choose_x()
    make_print_button(sin)


def cos_button():
    choose_x()
    make_print_button(cos)


def tg_button():
    choose_x()
    make_print_button(tg)


def ctg_button():
    choose_x()
    make_print_button(ctg)


def square_button():
    choose_x()
    make_print_button(x_squared)


def cube_button():
    choose_x()
    make_print_button(x_cube)


def quit():
    root.destroy()

create_graph = Menu(navigation_bar, tearoff=0)
create_graph.add_command(label='y=sin x', command=sin_button)
create_graph.add_command(label='y=cos x', command=cos_button)
create_graph.add_command(label='y=tg x', command=tg_button)
create_graph.add_command(label='y=ctg x', command=ctg_button)
create_graph.add_command(label='y=x2', command=square_button)
create_graph.add_command(label='y=x3', command=cube_button)

navigation_bar.add_cascade(label='Построить график', menu=create_graph)
navigation_bar.add_command(label='Справка')
navigation_bar.add_command(label='Выход', command=quit)

root.mainloop()
