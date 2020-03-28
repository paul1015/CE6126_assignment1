from tkinter import *
import tkinter as tkinter
import math as math
import time

#圖片的 軸是從左上角開始 x 是正 y 是負 
#theta car_angle

class car:
    #  轉換位置
    def __init__(self, zero_x, zero_y, multiply_x, multiply_y, car_x, car_y, car_angle , car_r=3, car_collar="red"):
        self.zero_x = zero_x
        self.zero_y = zero_y
        self. multiply_x = multiply_x
        self. multiply_y = multiply_y
        self.car_x = zero_x + car_x * multiply_x
        self.car_y = zero_y + (car_y * -1 )*multiply_y
        self.car_r = car_r
        self.car_collar = car_collar
        self.car_angle = round(math.radians(car_angle),2)


    def create_line(self, x1, y1, x2, y2, color):
        canvas.create_line(zero_x+x1*multiply_x, zero_y+(y1*-1)*self.multiply_y,
                           zero_x+x2*multiply_x, zero_y+(y2*-1)*self.multiply_y, fill=color, width=3)

    def create_circle(self):  
        # center coordinates, radius
        x0 = self.car_x - self.car_r*self.multiply_x
        y0 = self.car_y - self.car_r*self.multiply_y
        x1 = self.car_x + self.car_r*self.multiply_x
        y1 = self.car_y + self.car_r*self.multiply_y
        return canvas.create_oval(x0, y0, x1, y1, fill=self.car_collar)


    def car_move(self, tk, car, theta):

        #角度換算
        theta = round(math.radians(theta),2)
        # cos(a + b) = cos(a) * cos(b) - sin(a) * sin(b) 
        # sin(a + b) = sin(a) * cos(b) +   sin(b) * cos(a) 
        print(' t car_ x = ', self.car_x, 'car_y = ', self.car_y, 'car_angle', self.car_angle)
        #self.car_x = self.car_x + math.cos(self.car_angle + theta) + (math.sin(theta) * math.sin(self.car_angle))
        #self.car_y = self.car_y - (math.sin(self.car_angle + theta) - (math.sin(theta)) * math.cos(self.car_angle))
        #self.car_angle = self.car_angle - math.asin(2 * math.sin(theta) / self.car_r)
        self.car_x = self.car_x + 10*(math.cos(self.car_angle) * math.cos(theta)) 
        
        self.car_y = self.car_y -  10*(math.sin(self.car_angle) * math.cos(theta))
        self.car_angle = self.car_angle - math.asin(2 * math.sin(theta) / self.car_r)

        print(' t+1 car_ x = ', self.car_x, 'car_y = ', self.car_y, 'car_angle', self.car_angle)
    
        x0 = self.car_x - self.car_r*self.multiply_x
        y0 = self.car_y - self.car_r*self.multiply_y
        x1 = self.car_x + self.car_r*self.multiply_x
        y1 = self.car_y + self.car_r*self.multiply_y
        tk.coords(car, (x0, y0, x1, y1))



# Initial Form 
tk = Tk()
tk.title('assignment1')
tk.resizable(0, 0)


#Intial Value
width = 500
height = 500

multiply_x = width/60
multiply_y = height/60
zero_x = int(width/4)
zero_y = int(height/1.1)

#讀取檔案資料
f = open(r'case01.txt')
i = 0
for line in f:
    s = line.split(",")
    if(i == 0):
        print('line s ', s)
        car_x = int(s[0])
        car_y = int(s[1])
        car_angle = int(s[2])

    i = i + 1

        
car = car(zero_x, zero_y, multiply_x, multiply_y, car_x, car_y, car_angle)

canvas = Canvas(tk, width=width, height=height, bg='ivory')
canvas.pack(fill=BOTH, expand=1)
canvas.pack()
#我開心讀兩次檔
f = open(r'case01.txt')
i = 0
x1 = 0
y1 = 0 
x2 = 0 
y2 = 0
for line in f:
    s = line.split(",")
    if(i > 0) :
        if(i % 2 != 0):
            x1 = int(s[0])
            y1 = int(s[1])
        else :
            x2 = int(s[0])
            y2 = int(s[1])
    if(i == 2) : 
        print('goal', x1, y1, x2, y2)
        car.create_line(x1, y1, x2, y2, "red")

    if(i > 2):
        if(i != 3):
            car.create_line(x1, y1, x2, y2, "blue")

    i = i + 1
    
car.create_line(-12, 0, 12, 0, "black")

# WALL
""" car.create_line(-6, -3, -6, 22, "blue")
car.create_line(-6, 22, 18, 22, "blue")
car.create_line(18, 22, 18, 50, "blue")
car.create_line(18, 50, 30, 50, "blue")
car.create_line(30, 50, 30, 10, "blue")
car.create_line(30, 10, 6, 10, "blue")
car.create_line(6, 10, 6, -3, "blue")
car.create_line(6, -3, -6, -3, "blue") """

# GOAL Line
#car.create_line(18, 40, 30, 30, "red")


# CAR
car_obj = car.create_circle()
""" car.create_line(-12, 0, 12, 0, "black")
car.create_line(0, 0, 0, 4, "red")
car.create_line(0, 0, 0, -4, "black") """

while 1:
    """ car.car_move(canvas, car_obj)
    time.sleep(0.5) """
    theta = int(input('Input the theta between +- 40: \n'))
    if(theta == -1 ):
        break

    car.car_move(canvas, car_obj, theta)

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
