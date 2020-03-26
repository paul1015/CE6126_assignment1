from tkinter import *
import time

tk = Tk()  # 画布
tk.title('EIT_tank')
tk.resizable(0, 0)  # 固定窗口大小
tank = Canvas(tk, width=600, height=600, bg='ivory')
tank.pack()  # 默认布局
tank.create_oval(30, 30, 570, 570, width=1.5)  # 横轴x
tank.create_line(30, 300, 570, 300, width=1.5, fill='red', dash=6)  # 网格,虚线
tank.create_line(300, 30, 300, 570, width=1.5, fill='red', dash=6)
id_obj = tank.create_oval(130, 130, 270, 270, width=0, fill='gray')  # 物体


def move_obj(tank, idx, pos):  # 移动坐标
    if pos == 1:
        tank.coords(idx, (330, 330, 470, 470))
    elif pos == 2:
        tank.coords(idx, (330, 130, 470, 270))
    elif pos == 3:
        tank.coords(idx, (130, 130, 270, 270))
    elif pos == 4:
        tank.coords(idx, (130, 330, 270, 470))
    else:
        return 0


while 1:
    move_obj(tank, id_obj, 1)
    time.sleep(0.5)
    tk.update_idletasks()
    tk.update()

    move_obj(tank, id_obj, 2)
    time.sleep(0.5)
    tk.update_idletasks()
    tk.update()

    move_obj(tank, id_obj, 3)
    time.sleep(0.5)
    tk.update_idletasks()
    tk.update()

    move_obj(tank, id_obj, 4)
    time.sleep(0.5)
    tk.update_idletasks()
    tk.update()
