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
        self.car_orangle = car_angle
        self.car_angle = round(math.radians(car_angle),2)
        self.direction = 0
        self.ldirection = 0
        self.rdirection = 0
        self.ld = 0
        self.rd = 0
        self.d = 0
        self.b = car_r * multiply_x
        # x , y 左至右 上至下
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

        """ self.car_x = zero_x + car_x * multiply_x
        self.car_y = zero_y + (car_y * -1 )*multiply_y """
        print('car Posintion ', (self.car_x - zero_x) /self.multiply_x , -1 * (self.car_y - zero_y) / self.multiply_y)
        
        """ self.car_angle = round(math.radians(car_angle),2) """
        print('car angle', self.car_angle)

        #print(' t+1 car_ x = ', self.car_x, 'car_y = ', self.car_y, 'car_angle', self.car_angle)
    
        x0 = self.car_x - self.car_r*self.multiply_x
        y0 = self.car_y - self.car_r*self.multiply_y
        x1 = self.car_x + self.car_r*self.multiply_x
        y1 = self.car_y + self.car_r*self.multiply_y

       
        
        #draw the car
        tk.coords(car, (x0, y0, x1, y1))

        canvas.delete(self.direction)
        canvas.delete(self.ldirection)
        canvas.delete(self.rdirection)
        # direction line 
        #car_x = zero_x + car_x * multiply_x
        #car_y = zero_y + (car_y * -1 )*multiply_y
        car_x1 =  (self.car_x - self.zero_x) / self.multiply_x
        car_y1 = (self.car_y  - self.zero_y) / self.multiply_y * -1
        
        
        x2 = car_x1 + 6* math.cos(self.car_angle)
        y2 = car_y1 + 6* math.sin(self.car_angle)

        self.direction = self.create_line(car_x1, car_y1, x2, y2, "red")

        #print('car_d', self.car_x, self.x1, self.x2, self.car_y, self.y1)
        round(math.radians(car_angle),2)
        langle =   self.car_angle + round(math.radians(45),2)
        rangle = self.car_angle - round(math.radians(45),2)

        x2 = car_x1 + 6* math.cos(langle )
        y2 = car_y1 + 6* math.sin(langle ) 
        self.ldirection = self.create_line(car_x1, car_y1, x2, y2, "black")

        x2 = car_x1 + 6* math.cos(rangle )
        y2 = car_y1 + 6* math.sin(rangle ) 
        self.rdirection = self.create_line(car_x1, car_y1, x2, y2, "black")
        
        #sensor part
        #往回開就是腦袋開抽
        #boundary base
        
        #forward
        #x1 boudanry
        x1d = (abs(self.car_x - self.x1 ) * -1 * (1/ math.cos(self.car_angle)))
        x1dc = abs((self.car_x - self.x1 ) * (math.tan(self.car_angle)))
        

        #x1 boundary judge
        if(self.car_y - x1dc <= self.y2 or x1d < 0):
            #設為最大值
            x1d = 10000
            
        else :
            x1d = x1d / self.multiply_x

        #print('x1d', x1d)
        
        #x2 boundary
        x2d = (abs(self.car_x - self.x2 ) * (1/ math.cos(self.car_angle)))
        x2dc = (abs(self.car_x - self.x2 ) * (math.tan(self.car_angle)))
        
        #x2 boundary judge
        if(self.car_y - x2dc <= self.y1 or x2d < 0):
            #設為最大值
            x2d = 10000
            
        else :
            
            x2d = x2d / self.multiply_x
        
        #print('x2d', x2d)

        #x3 boundary
        x3d = (abs(self.car_x - self.x3 ) * -1 *(1/ math.cos(self.car_angle)))
        x3dc = (abs(self.car_x - self.x3 ) * (math.tan(self.car_angle)))
        
        #x3 boundary judge
        if(self.car_y - x3dc <= self.y1 or x3d < 0):
            #設為最大值
            x3d = 10000
            
        else :
            
            x3d = x3d / self.multiply_x
        
        #print('x3d', x3d)

        #x4 boundary
        x4d = (abs(self.car_x - self.x4 )  * (1/ math.cos(self.car_angle)))
        x4dc = abs((self.car_x - self.x4 ) * (math.tan(self.car_angle)))
        
        #x4 boundary judge
        if(self.car_y - x4dc <= self.y3 or x4d < 0):
            #設為最大值
            x4d = 10000
            
        else :
           
            x4d = x4d / self.multiply_x
        
        #print('x4d', x4d)
        
        # y2 boundary
        y2d = (abs(self.car_y - self.y2) * (1/ math.sin(self.car_angle)))
        y2dc = abs((self.car_y - self.y2 ) * abs(1/math.tan(self.car_angle)))

        # y2 boundary judge
        if(self.car_x + y2dc >= self.x3 or y2d < 0 ):
            y2d = 10000
        else :
            y2d = y2d / self.multiply_y
        
        #print('y2d', y2d)

        # y1 boundary 
        y1d = (abs(self.car_y - self.y1) * -1 * (1/ math.sin(self.car_angle)))
        y1dc = abs((self.car_y - self.y1 ) * (1/math.tan(self.car_angle)))

       #y1 boundary judge
        if(self.car_x + y1dc <= self.x2 or y1d < 0):
            y1d = 10000
        else :
            y1d = y1d / self.multiply_y
        
        #print('y1d', y1d)

        #y3 boundary 
        y3d = (abs(self.car_y - self.y3) * (1/ math.sin(self.car_angle)))
        y3dc = abs((self.car_y - self.y3 ) * abs(1/math.tan(self.car_angle)))

        #y3 boundary judge
        if(self.car_x + y3dc >= self.x4 or y3d < 0 ):
            y3d = 10000
        else :
            y3d = y3d / self.multiply_y
        
        #print('y3d', y3d)

        print('d ', min(x1d, x2d, x3d, x4d, y1d, y2d, y3d))
        d = min(x1d, x2d, x3d, x4d, y1d, y2d, y3d)
        if(d <= 3) :
            print('bang!')

        #left sensor
        x1ld = (abs(self.car_x - self.x1 ) * -1 * (1/ math.cos(langle)))
        x1ldc = abs((self.car_x - self.x1 ) * (math.tan(langle)))
        
        if(self.car_y - x1ldc <= self.y2 or x1ld < 0):
            #設為最大值
            x1ld = 10000
            
        else :

            x1ld = x1ld / self.multiply_x
        
        print('x1ld', x1ld)
        
        x2ld = (abs(self.car_x - self.x2 ) * (1/ math.cos(langle)))
        x2ldc = (abs(self.car_x - self.x2 ) * (math.tan(langle)))
        
        
        if(self.car_y - x2ldc <= self.y1 or x2ld < 0):
            #設為最大值
            x2ld = 10000
            
        else :
            x2ld = x2ld / self.multiply_x
        
        print('x2ld', x2ld)

        x3ld = (abs(self.car_x - self.x3 ) * -1 *(1/ math.cos(langle)))
        x3ldc = abs((self.car_x - self.x3 ) * (math.tan(langle)))
        
        print('???? ', x3ld, x3ldc, self.car_y, self.y1)
        if(self.car_y - x3ldc <= self.y3 or x3ld < 0):
            #設為最大值
            x3ld = 10000
            
        else :
            
            x3ld = x3ld / self.multiply_x
        
        print('x3ld', x3ld)

        x4ld = (abs(self.car_x - self.x4 )  * (1/ math.cos(langle)))
        x4ldc = abs((self.car_x - self.x4 ) * (math.tan(langle)))
        
        if(self.car_y - x4ldc <= self.y3 or x4ld < 0):
            #設為最大值
            x4ld = 10000
            
        else :
           
            x4ld = x4ld / self.multiply_x
        
        print('x4ld', x4ld)

        y2ld = (abs(self.car_y - self.y2) * (1/ math.sin(langle)))
        y2ldc = abs((self.car_y - self.y2 ) * abs(1/math.tan(langle)))

        if(self.car_x + y2ldc >= self.x3 or y2ld < 0 ):
            y2ld = 10000
        else :
            y2ld = y2ld / self.multiply_y
        
        print('y2ld', y2ld)

        y1ld = (abs(self.car_y - self.y1) * -1 * (1/ math.sin(langle)))
        y1ldc = abs((self.car_y - self.y1 ) * (1/math.tan(langle)))

        
        if(self.car_x + y1ldc <= self.x2 or y1ld < 0):
            y1ld = 10000
        else :
            y1ld = y1ld / self.multiply_y
        
        print('y1ld', y1ld)

        
        y3ld = (abs(self.car_y - self.y3) * (1/ math.sin(langle)))
        y3ldc = abs((self.car_y - self.y3 ) * abs(1/math.tan(langle)))

        if(self.car_x + y3ldc >= self.x4 or y3ld < 0 ):
            y3ld = 10000
        else :
            y3ld = y3ld / self.multiply_y
        
        print('y3ld', y3ld)

        print('ld ', min(x1ld, x2ld, x3ld, x4ld, y1ld, y2ld, y3ld))
        ld = min(x1ld, x2ld, x3ld, x4ld, y1ld, y2ld, y3ld)
        if(ld <= 3):
            print('bang!')

        #right sensor
        x1rd = (abs(self.car_x - self.x1 ) * -1 * (1/ math.cos(rangle)))
        x1rdc = abs((self.car_x - self.x1 ) * (math.tan(rangle)))
        
        if(self.car_y - x1rdc <= self.y2 or x1rd < 0):
            #設為最大值
            x1rd = 10000
            
        else :
            x1rd = x1rd / self.multiply_x
        
        #print('x1rd', x1rd)
        
        x2rd = (abs(self.car_x - self.x2 ) * (1/ math.cos(rangle)))
        x2rdc = (abs(self.car_x - self.x2 ) * (math.tan(rangle)))
        
        
        if(self.car_y - x2rdc <= self.y1 or x2rd < 0):
            #設為最大值
            x2rd = 10000
            
        else :
            
            x2rd = x2rd / self.multiply_x
        
        #print('x2rd', x2rd)

        x3rd = (abs(self.car_x - self.x3 ) * -1 *(1/ math.cos(rangle)))
        x3rdc = (abs(self.car_x - self.x3 ) * (math.tan(rangle)))
        
        if(self.car_y - x3rdc <= self.y1 or x3rd < 0):
            #設為最大值
            x3rd = 10000
            
        else :
            x3rd = x3rd / self.multiply_x
        
        #print('x3rd', x3rd)

        x4rd = (abs(self.car_x - self.x4 )  * (1/ math.cos(rangle)))
        x4rdc = abs((self.car_x - self.x4 ) * (math.tan(rangle)))
        
        if(self.car_y - x4rdc <= self.y3 or x4rd < 0):
            #設為最大值
            x4rd = 10000
            
        else :
            x4rd = x4rd / self.multiply_x
        
        #print('x4rd', x4rd)

        y2rd = (abs(self.car_y - self.y2) * (1/ math.sin(rangle)))
        y2rdc = abs((self.car_y - self.y2 ) * abs(1/math.tan(rangle)))

        if(self.car_x + y2rdc >= self.x3 or y2rd < 0 ):
            y2rd = 10000
        else :
            y2rd = y2rd / self.multiply_y
        
        #print('y2rd', y2rd)

        y1ld = (abs(self.car_y - self.y1) * -1 * (1/ math.sin(rangle)))
        y1ldc = abs((self.car_y - self.y1 ) * (1/math.tan(rangle)))

        if(self.car_x + y1ldc <= self.x2 or y1ld < 0):
            y1ld = 10000
        else :
            y1ld = y1ld / self.multiply_y
        

        
        y3rd = (abs(self.car_y - self.y3) * (1/ math.sin(rangle)))
        y3rdc = abs((self.car_y - self.y3 ) * abs(1/math.tan(rangle)))

        if(self.car_x + y3rdc >= self.x4 or y3rd < 0 ):
            y3rd = 10000
        else :
            y3rd = y3rd / self.multiply_y
        
        #print('y3rd', y3rd)

        print('rd ', min(x1rd, x2rd, x3rd, x4rd, y1ld, y2rd, y3rd))
        rd = min(x1rd, x2rd, x3rd, x4rd, y1ld, y2rd, y3rd)
        if(rd <= 3) :
            print('bang')
        
        dw = Label(canvas, text = 'd : ' + str(d), fg='white', bg='black')
        dw.pack()
        canvas.create_window(100, 100, window=dw)
        
        ldw = Label(canvas, text = 'ld : ' + str(ld), fg='white', bg='black')
        ldw.pack()
        canvas.create_window(100, 75, window=ldw)
        
        rdw = Label(canvas, text = 'rd : ' + str(rd), fg='white', bg='black')
        rdw.pack()
        canvas.create_window(100, 125, window=rdw)
       


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
