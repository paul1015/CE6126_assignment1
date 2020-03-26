from tkinter import *
import time

def create_line(x1,y1,x2,y2,color):
    canvas.create_line(first_x+x1*multiply_x,first_y+(y1*-1)*multiply_y,first_x+x2*multiply_x,first_y+(y2*-1)*multiply_y, fill=color, width=3)

def create_circle(x, y, r, color): #center coordinates, radius
    x0 = x - r*multiply_x
    y0 = y - r*multiply_y
    x1 = x + r*multiply_x
    y1 = y + r*multiply_y
    return canvas.create_oval(x0, y0, x1, y1, fill=color)


tk = Tk()  # 画布
tk.title('Momentum')
tk.resizable(0, 0)  # 固定窗口大小
width = 1000
height = 1000
multiply_x = width/60
multiply_y = height/60
first_x = int(width/4)
first_y = int(height/1.1)
canvas = Canvas(tk, width=width, height=height, bg='ivory')
canvas.pack(fill=BOTH, expand=1)
while 1:
    canvas.pack()  # 默认布局
    ##WALL
    create_line(-6,-3,-6,22,"blue")
    create_line(-6,22,18,22,"blue")
    create_line(18,22,18,50,"blue")
    create_line(18,50,30,50,"blue")
    create_line(30,50,30,10,"blue")
    create_line(30,10,6,10,"blue")
    create_line(6,10,6,-3,"blue")
    create_line(6,-3,-6,-3,"blue")

    ##GOAL
    create_line(18,45,30,45,"red")

    ##CAR
    create_circle(first_x, first_y, 2, "red")
    create_line(-12,0,12,0,"black")
    create_line(0,0,0,4,"red")
    create_line(0,0,0,-4,"black")
    
    # height = tk.winfo_screenheight() 
    # width = tk.winfo_screenwidth() 
    tk.update()
    canvas.update()

# tank.create_oval(30, 30, 570, 570, width=1.5)  # 横轴x
# tank.create_line(30, 300, 570, 300, width=1.5, fill='red', dash=6)  # 网格,虚线
# tank.create_line(300, 30, 300, 570, width=1.5, fill='red', dash=6)
# id_obj = tank.create_oval(130, 130, 270, 270, width=0, fill='gray')  # 物体


# def move_obj(tank, idx, pos):  # 移动坐标

#     if pos == 1:
#         tank.coords(idx, (330, 330, 470, 470))
#     elif pos == 2:
#         tank.coords(idx, (330, 130, 470, 270))
#     elif pos == 3:
#         tank.coords(idx, (130, 130, 270, 270))
#     elif pos == 4:
#         tank.coords(idx, (130, 330, 270, 470))
#     else:
#         return 0


# while 1:
#     move_obj(tank, id_obj, 1)
#     time.sleep(0.5)
#     tk.update_idletasks()
#     tk.update()

#     move_obj(tank, id_obj, 2)
#     time.sleep(0.5)
#     tk.update_idletasks()
#     tk.update()

#     move_obj(tank, id_obj, 3)
#     time.sleep(0.5)
#     tk.update_idletasks()
#     tk.update()

#     move_obj(tank, id_obj, 4)
#     time.sleep(0.5)
#     tk.update_idletasks()
#     tk.update()
