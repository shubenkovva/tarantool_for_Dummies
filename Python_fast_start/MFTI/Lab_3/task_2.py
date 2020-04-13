from graph import *
import math
import numpy as np

#!!! Рисуем сетку 50x50 !!!#
penSize(0.5)
penColor(0, 0, 0)
for i in range(0, 1000, 50):
    lineTo(i, 1000)
    moveTo(i + 50, 0)
moveTo(0, 0)
for i in range(0, 1000, 50):
    lineTo(1000, i)
    moveTo(0, i + 50)
moveTo(0, 0)
#!!! Рисуем сетку 50x50 !!!#

def main():
    f_cat(200, 200, 100, 50, 'right', (153, 77, 2))
    f_cat(200, 400, 50, 25, 'left', (153, 77, 2))

def f_get_coord_elipce(x, y, a, b):
    '''
    :param x: координата расположения центра кота
    :param y: координата расположения центра кота
    :param a: длинна половины кота
    :param b: толщина половины кота
    :return: координаты элипса
    '''
    x_y_coord_d = list()
    x_y_coord_u = list()
    x_array = np.arange(-1000, 1000, 0.5)

    for i in x_array:
        par = (1 - ((i - x)**2)/a**2) * b**2
        if par >= 0:
            x_y_coord_d.append([i, math.sqrt(par) + y])
            x_y_coord_u.append([i, -math.sqrt(par) + y])

    return x_y_coord_d, x_y_coord_u

def f_paint_elipce(down, up, color):
    penColor(0, 0, 0)
    penSize(1)
    brushColor(color[0], color[1], color[2])
    polygon(down + up[::-1] + down[:1])

def f_paint_elipce(down, up, color):
    penColor(0, 0, 0)
    penSize(1)
    brushColor(color[0], color[1], color[2])
    polygon(down + up[::-1] + down[:1])

def f_paint_hvost(down, up, color, direction, x, y, angel):
    x_y_coord_d_hvost_new = list()
    x_y_coord_u_hvost_new = list()

    x_y_coord_d_new_angel = list()
    x_y_coord_u_new_angel = list()
    #Получаем координаты хвоста в новой системы координат
    for i in down:
        x_y_coord_d_hvost_new.append([i[0] - x, i[1] - y])
    for i in up:
        x_y_coord_u_hvost_new.append([i[0] - x, i[1] - y])

    #вычисляем координаты в старом базисе, с учетом наклона нового базиса
    for i in x_y_coord_d_hvost_new:
        x_y_coord_d_new_angel.append([i[0] * angel[0] - i[1] * angel[1] + x,
                                      i[0] * angel[1] + i[1] * angel[0] + y])
    for i in x_y_coord_u_hvost_new:
        x_y_coord_u_new_angel.append([i[0] * angel[0] - i[1] * angel[1] + x,
                                      i[0] * angel[1] + i[1] * angel[0] + y])


    penColor(0, 0, 0)
    penSize(1)
    brushColor(153, 77, 2)
    polygon(x_y_coord_d_new_angel + x_y_coord_u_new_angel[::-1] + x_y_coord_d_new_angel[:1])

def f_cat(x, y, a, b, direction, color):
    '''
    :param x: координата расположения центра кота
    :param y: координата расположения центра кота
    :param a: длинна половины кота
    :param b: толщина половины кота
    :param direction: направление кота
    :return:
    '''
    x_y_coord_d_body, x_y_coord_u_body = f_get_coord_elipce(x, y, a, b) # Получаем координаты нижней и верхней части тела кота
   #Получаем координаты хвоста, Рисуем хвост
    if direction == 'left':
        #Координаты системы координат хвоста
        x_system_koord_hvost = x_y_coord_d_body[-2:][0][0] + a/5
        y_system_koord_hvost = x_y_coord_d_body[-2:][0][1]
#        angel = [math.cos(math.sqrt(3)/2), math.sin(1/2)]
        angel = [math.cos(math.pi/6), math.sin(math.pi/6)]
        #Координаты системы координат хвоста
        x_y_coord_d_hvost, x_y_coord_u_hvost = f_get_coord_elipce(x_system_koord_hvost, y_system_koord_hvost, a/2, b/4)
        f_paint_hvost(x_y_coord_d_hvost, x_y_coord_u_hvost, color, direction, x_system_koord_hvost, y_system_koord_hvost, angel) #Рисуем хвост справа
    elif direction == 'right':
        #Координаты системы координат хвоста
        x_system_koord_hvost = x_y_coord_d_body[2:][0][0] - a/5
        y_system_koord_hvost = x_y_coord_d_body[2:][0][1]
        angel = [math.cos(5 * math.pi/6), math.sin(5 * math.pi/6)]
        #Координаты системы координат хвоста
        x_y_coord_d_hvost, x_y_coord_u_hvost = f_get_coord_elipce(x_system_koord_hvost, y_system_koord_hvost, a/2, b/4)
        f_paint_hvost(x_y_coord_d_hvost, x_y_coord_u_hvost, color, direction, x_system_koord_hvost, y_system_koord_hvost, angel) #Рисуем хвост слева
    #Получаем координаты хвоста, Рисуем хвост

    f_paint_elipce(x_y_coord_d_body, x_y_coord_u_body, color)

    #Рисуем голову кота
    if direction == 'left':
        circle(x_y_coord_d_body[1:][0][0], x_y_coord_u_body[1:][0][1], b)
    elif direction == 'right':
        circle(x_y_coord_d_body[-1:][0][0], x_y_coord_u_body[-1:][0][1], b)
    #Рисуем голову кота

main()
run()