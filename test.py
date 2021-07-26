
import pygame
import numpy as np
from numba import jit , cuda
from random import seed
from random import randint
from timeit import default_timer as timer
# To run on CPU

height = 480
width = 720
speed = 10
cycle = 10
HERTZ = 120
def InRange(x,y,xFood,yFood,IaRange) :
    yRange = y - yFood
    xRange = x - xFood
    InRange = False
    if yRange > -IaRange and yRange < IaRange and xRange > -IaRange and xRange < IaRange :
        InRange = True
    return(InRange)
def IaMov(x,y,x_change,y_change):
          global cycle
          global height
          global width
          global HERTZ
          speed  = randint(1,10)
          speed = speed * (HERTZ/500)
          Rng = randint(0,4)    
          if cycle % 10 == 0:     
           if Rng > 0  and Rng <= 1 :
             x_change += -speed
             y_change += 0
           elif Rng > 1 and Rng <= 2 :
             x_change += speed
             y_change += 0
           elif Rng > 2 and Rng <= 3 :
            y_change += -speed
            x_change += 0
           elif Rng > 3 and Rng <= 4 :
             y_change += speed
             x_change += 0
          x += x_change
          y += y_change
          if y > height :
             y -= height
          if y < 0 :
             y += height
          if x > width :
             x -= width
          if x < 0 :
               x += width 
          pos = [x,y,x_change,y_change]
          return(pos)
def cmd (stop) :
    global cycle
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_DELETE :
                    stop = True 
    Commands = [stop]
    return(Commands)

def func(stop):
    pygame.init()
    global cycle
    global HERTZ
    IaRange = 5
    IaNum = 10
    x = []
    y = []
    IaType = []
    x_change = []      
    y_change = []
    xFood = []
    yFood = []
    FoodQuant = 10
    Bv = 300
    for i in range(IaNum) :
       x.append(Bv)
       y.append(Bv)
       x_change.append(0)
       y_change.append(0)
       IaType.append(randint(0,1))
    for i in range(FoodQuant) :
       xFood.append(randint(0,width))
       yFood.append(randint(0,height))
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0,255,0)
    blue = (0,0,255)
    dis = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    while not stop : 
        Commands = cmd(stop)
        stop = Commands[0]
        init = 0
        iFood = 0
        for i in range(FoodQuant) :
             pygame.draw.circle(dis, blue, [xFood[iFood], yFood[iFood]],10 )
             iFood += 1
             
        for i in range(IaNum) :
            Ia =  IaMov(x[init],y[init],x_change[init],y_change[init])
            x[init] = Ia[0]
            y[init] = Ia[1]
            x_change[init] = Ia[2]
            y_change[init] = Ia[3]
            if IaType[init] == 0 :
               pygame.draw.rect(dis, red, [x[init], y[init], 10, 10])
            elif IaType[init] == 1 :
                pygame.draw.rect(dis, green, [x[init], y[init], 10, 10])
            i = 0        
            for i in range(FoodQuant) :
               CaptDis = InRange(x[init],y[init],xFood[i],yFood[i],IaRange)
               if  CaptDis == True :
                    x.append(x[init])
                    y.append(y[init])
                    x_change.append(0)
                    y_change.append(0)
                    IaType.append(IaType[init])
                    IaNum += 1
                    xFood[i] = width + 10
                    yFood[i] = height + 10

            init += 1
        pygame.display.update()       
        title = str(IaNum)
        pygame.display.set_caption(title)
        dis.fill(white)
        cycle += 1
        clock.tick(HERTZ)
        

    pygame.quit()
    quit()
if __name__=="__main__":
    stop = False
    func(stop)
 
