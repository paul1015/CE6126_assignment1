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
        self.direction = 0
        self.ld = 0
        self.rd = 0
        self.d = 0
        self.b = car_r * multiply_x
        self.x1 = zero_x + -6 * multiply_x
        self.x2 = zero_x + 6 * multiply_x
        self.x3 = zero_x + 18 * multiply_x
        self.x4 = zero_x + 30 * multiply_x
        self.y1 = zero_y + -10 * multiply_y
        self.y2 = zero_y + -22* multiply_y
        self.y3 = zero_y + -40 * multiply_y


    def create_line(self, x1, y1, x2, y2, color):
        return canvas.create_line(zero_x+x1*multiply_x, zero_y+(y1*-1)*self.multiply_y,
                           zero_x+x2*multiply_x, zero_y+(y2*-1)*self.multiply_y, fill=color, width=3)

    def create_car(self):  
        
        # center coordinates, radius

        """ x0 = self.zero_x + self.car_x * self.multiply_x - self.car_r*self.multiply_x
        y0 = self.zero_y + (self.car_y * -1 ) * self.multiply_y - self.car_r*self.multiply_y
        x1 = self.zero_x + self.car_x * self.multiply_x + self.car_r*self.multiply_x
        y1 = self.zero_y + (self.car_y * -1 ) *self.multiply_y + self.car_r*self.multiply_y """

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
        #print(' t car_ x = ', self.car_x, 'car_y = ', self.car_y, 'car_angle', self.car_angle)
        #self.car_x = self.car_x + math.cos(self.car_angle + theta) + (math.sin(theta) * math.sin(self.car_angle))
        #self.car_y = self.car_y - (math.sin(self.car_angle + theta) - (math.sin(theta)) * math.cos(self.car_angle))
        #self.car_angle = self.car_angle - math.asin(2 * math.sin(theta) / self.car_r)
        self.car_x = self.car_x + 10*(math.cos(self.car_angle) * math.cos(theta)) 
        self.car_y = self.car_y -  10*(math.sin(self.car_angle) * math.cos(theta))
        self.car_angle = self.car_angle - math.asin(2 * math.sin(theta) / self.car_r)

        #print(' t+1 car_ x = ', self.car_x, 'car_y = ', self.car_y, 'car_angle', self.car_angle)
    
        x0 = self.car_x - self.car_r*self.multiply_x
        y0 = self.car_y - self.car_r*self.multiply_y
        x1 = self.car_x + self.car_r*self.multiply_x
        y1 = self.car_y + self.car_r*self.multiply_y
        
        #draw the car
        tk.coords(car, (x0, y0, x1, y1))

        canvas.delete(self.direction)
        # direction line 
        #car_x = zero_x + car_x * multiply_x
        #car_y = zero_y + (car_y * -1 )*multiply_y
        car_x1 =  (self.car_x - self.zero_x) / self.multiply_x
        car_y1 = (self.car_y  - self.zero_y) / self.multiply_y * -1
        
        
        x2 = car_x1 + 6* math.cos(self.car_angle)
        y2 = car_y1 + 6* math.sin(self.car_angle)

        self.direction = self.create_line(car_x1, car_y1, x2, y2, "red")

        #print('car_d', self.car_x, self.x1, self.x2, self.car_y, self.y1)

        langle = self.car_angle - round(math.radians(45),2)
        rangle = self.car_angle + round(math.radians(45),2)
        #分三塊去做sensor part
        if(self.car_x >= self.x1 and self.car_x <= self.x2 and self.car_y >= self.y1):
            d1 = (self.car_y - self.y2) * (1/ math.sin(self.car_angle))
            d2 = (self.car_x - self.x1 ) * (1/ math.cos(self.car_angle))
            d3 = (self.car_x - self.x2 ) * (1/ math.cos(self.car_angle))
            if(d1 < 0 ):
                d1 = 10000
            if(d2 < 0):
                d2 = 10000
            if(d3 < 0):
                d3 = 10000
            self.d = min(d1, d2, d3) 

            ld1 = (self.car_y - self.y2) * (1/ math.sin(langle))
            ld2 = (self.car_x - self.x1 ) * (1/ math.cos(langle))
            ld3 = (self.car_x - self.x2 ) * (1/ math.cos(langle))
            if(ld1 < 0 ):
                ld1 = 10000
            if(ld2 < 0):
                ld2 = 10000
            if(ld3 < 0):
                ld3 = 10000
            self.ld = min(ld1, ld2, ld3) 

            rd1 = ((self.car_y - self.y2) * (1/ math.sin(rangle)))
            rd2 =  ((self.car_x - self.x1 ) * (1/ math.cos(rangle)))
            rd3 = ((self.car_x - self.x2 ) * (1/ math.cos(rangle)))
            rd3c = ((self.car_x - self.x2 ) * (math.tan(rangle)))
            if(rd1 < 0 ):
                rd1 = 10000
            if(rd2 < 0):
                rd2 = 10000
            if(rd3 < 0):
                rd3 = 10000
            #判斷右邊
            if(self.car_y - rd3c < self.y1 ):
                #設為最大值
                rd3 = 10000

            self.rd = min(rd1, rd2, rd3)

            #car_x = zero_x + car_x * multiply_x
            d = self.d / multiply_x
            ld = self.ld / multiply_x
            rd = self.rd / multiply_x
            print('self.d in zone 1 ', d, ld, rd )

        elif(self.car_y <= self.y1 and self.car_y >= self.y2 ):
            d1 = (self.car_y - self.y2) * (1/ math.sin(self.car_angle))
            d1c = ((self.car_y - self.y2 ) * (1/math.tan(self.car_angle)))
            d2 = (self.car_y - self.y1) * (1/ math.sin(self.car_angle))
            d3 = (self.car_x - self.x4 ) * (1/ math.cos(self.car_angle))

            d4 = ((self.car_y - self.y3 ) * (math.tan(self.car_angle)))
            d5 = (self.car_x - self.x3 ) * (1/ math.cos(self.car_angle))
            d6 = (self.car_x - self.x1 ) * (1/ math.cos(self.car_angle))
            print("y2, y1, x4, y3, x3, x1")
            
            if(d1 < 0 ):
                d1 = 10000
            if(d2 < 0):
                d2 = 10000
            if(d3 < 0):
                d3 = 10000
            if(d4 < 0):
                d4 = 10000
            if(d5 < 0):
                d5 = 10000
            if(d6 < 0):
                d6 = 10000
            print('self.x3', self.car_x + d1c , self.x3)
            #判斷左邊
            if(self.car_x + d1c >= self.x3 ):
                print("d1 ininin")
                #設為最大值
                d1 = 10000
            print('ddd', d1, d2, d3,d4, d5,d6 )

            self.d = min(d1, d2, d3, d4, d5, d6) 
            d = self.d / self.multiply_x
            
            ld1 = (self.car_y - self.y2) * (1/ math.sin(langle))
            ld1c = ((self.car_y - self.y2 ) * (math.tan(langle)))
            ld2 = (self.car_y - self.y1) * (1/ math.sin(langle))
            ld3 = (self.car_x - self.x4 ) * (1/ math.cos(langle))
            ld4 = ((self.car_y - self.y3 ) * (math.tan(langle)))
            ld5 = (self.car_x - self.x3 ) * (1/ math.cos(langle))
            ld6 = (self.car_x - self.x1 ) * (1/ math.cos(langle))
            if(ld1 < 0 ):
                ld1 = 10000
            if(ld2 < 0):
                ld2 = 10000
            if(ld3 < 0):
                ld3 = 10000
            if(ld4 < 0):
                ld4 = 10000
            if(ld5 < 0):
                ld5 = 10000
            if(ld6 < 0):
                ld6 = 10000
            #判斷左邊
            if(self.car_x + ld1c < self.x3 ):
                #設為最大值
                ld1 = 10000
            self.ld = min(ld1, ld2, ld3)

            ld = self.ld /self.multiply_x

            rd1 = (self.car_y - self.y2) * (1/ math.sin(rangle))
            rd1c = ((self.car_y - self.y2 ) * (math.tan(rangle)))
            rd2 = (self.car_y - self.y1) * (1/ math.sin(rangle))
            rd3 = (self.car_x - self.x4 ) * (1/ math.cos(rangle))
            rd4 = ((self.car_y - self.y3 ) * (math.tan(rangle)))
            rd5 = (self.car_x - self.x3 ) * (1/ math.cos(rangle))
            rd6 = (self.car_x - self.x1 ) * (1/ math.cos(rangle))
            if(rd1 < 0 ):
                rd1 = 10000
            if(rd2 < 0):
                rd2 = 10000
            if(rd3 < 0):
                rd3 = 10000
            if(rd4 < 0):
                rd4 = 10000
            if(rd5 < 0):
                ld5 = 10000
            if(rd6 < 0):
                rd6 = 10000

            if(self.car_x + rd1c < self.x3 ):
                #設為最大值
                rd1 = 10000

            self.rd = min(rd1, rd2, rd3)

            rd = self.rd /self.multiply_x
            print('self.d in zone 2', d, ld, rd)






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

    if(i > 3):
        car.create_line(x1, y1, x2, y2, "blue")

    i = i + 1

# CAR
car_obj = car.create_car()

#起跑線 0,0
car.create_line(-12, 0, 12, 0, "black")


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
