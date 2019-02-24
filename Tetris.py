import pygame as py
import random as rn
py.init()
win = py.display.set_mode((250,500))
py.display.set_caption("Tetris")
Red=(255,0,0)
Green=(0,204,0)
Blue=(0,255,255)
Orange=(255,165,0)
Purple=(138,43,226)
DBlau=(0,0,139)
Yellow=(255,255,0)
pos1=False
Bord=[0]
for x in range(1,21):
    Bord.append(0+12*x)
    Bord.append(-1+12*x)
py.time.Clock()
run=True
Col=["0"]
Col=Col*270
Mov=["0"]
Mov=Mov*270
for x in range(0,240,12):
    Col[x]="1"
for x in range(11,251,12):
    Col[x]="1"
for x in range(240,251):
    Col[x]="1"
Image = py.image.load("tet.jpg").convert()
py.mixer.music.load("Tetris.mp3")
py.mixer.music.play(loops=-1, start=0.0)
def Draw():
    x=-25
    y=0
    win.fill((0,0,0))
    win.blit(Image, ( 0,0))
    for p in range(0,250):
        if x==275:
            y+=25
            x=-25
        if Col[p]!="0":
            if Col[p]=="1":
                farb=Red
            if Col[p]=="2":
                farb=Green
            if Col[p]=="3":
                farb=Blue
            if Col[p]=="4":
                farb=Orange
            if Col[p]=="5":
                farb=DBlau
            if Col[p]=="6":
                farb=Purple
            if Col[p]=="7":
                farb=Yellow
            py.draw.rect(win,(0,0,0),(x,y,25,25))
            py.draw.rect(win,farb,(x+1,y+1,23,23))
        x+=25
    
    py.display.update()
stop=False
pos2=0
while run:
    b=False
    if "1" not in Mov:
        line=True
        p=-1
        for x in range(0,240):
            p=p+1
            if p==11 and line==True:
                for d in range(x-12,x):
                    if d not in Bord:
                        Col[d]="0"
                for p in range (0,x):
                    if p not in Bord:
                        Mov[p]="1"
                b=True
                
                py.event.pump()
                Draw()
            elif p==12:
                p=0
                line=True
            if Col[x]=="0":
                line=False
        if b==False:
            shape=rn.randrange(1,8)
#            shape=5
            if shape == 1:
                if Col[5]=="0" and Col[6]=="0" and Col[7]=="0" and Col[8]=="0":
                    Col[5]="1"
                    Col[6]="1"
                    Col[7]="1"
                    Col[8]="1"
                    Mov[5]="1"
                    Mov[6]="1"
                    Mov[7]="1"
                    Mov[8]="1"
                    pos1=False
            if shape== 2:
                 if Col[5]=="0" and Col[6]=="0" and Col[18]=="0" and Col[19]=="0":
                    Col[5]="2"
                    Col[6]="2"
                    Col[18]="2"
                    Col[19]="2"
                    Mov[5]="1"
                    Mov[6]="1"
                    Mov[18]="1"
                    Mov[19]="1"
                    pos1=False
            if shape== 3:
                 if Col[5]=="0" and Col[6]=="0" and Col[18]=="0" and Col[7]=="0":
                    Col[5]="3"
                    Col[6]="3"
                    Col[18]="3"
                    Col[7]="3"
                    Mov[5]="1"
                    Mov[6]="1"
                    Mov[18]="1"
                    Mov[7]="1"
                    pos2=0
            if shape== 4:
                 if Col[5]=="0" and Col[6]=="0" and Col[7]=="0" and Col[17]=="0":
                    Col[5]="4"
                    Col[6]="4"
                    Col[7]="4"
                    Col[17]="4"
                    Mov[5]="1"
                    Mov[6]="1"
                    Mov[7]="1"
                    Mov[17]="1"
                    pos2=0
            if shape== 5:
                 if Col[5]=="0" and Col[6]=="0" and Col[7]=="0" and Col[19]=="0":
                    Col[5]="5"
                    Col[6]="5"
                    Col[7]="5"
                    Col[19]="5"
                    Mov[5]="1"
                    Mov[6]="1"
                    Mov[7]="1"
                    Mov[19]="1"
                    pos2=0
            if shape== 6:
                 if Col[17]=="0" and Col[6]=="0" and Col[18]=="0" and Col[7]=="0":
                    Col[17]="6"
                    Col[6]="6"
                    Col[18]="6"
                    Col[7]="6"
                    Mov[17]="1"
                    Mov[6]="1"
                    Mov[18]="1"
                    Mov[7]="1"
                    pos1=False
            if shape== 7:
                 if Col[6]=="0" and Col[7]=="0" and Col[18]=="0" and Col[19]=="0":
                    Col[7]="7"
                    Col[6]="7"
                    Col[18]="7"
                    Col[19]="7"
                    Mov[7]="1"
                    Mov[6]="1"
                    Mov[18]="1"
                    Mov[19]="1"
        s=False
    
   
    for event in py.event.get():
        if event.type == py.QUIT:
            run=False

    keys=py.key.get_pressed()
    if keys[py.K_LEFT] and int(py.time.get_ticks()) % 100 ==True and stop==False:
        left=True
        for x in range(0,251):
           if Mov[x]=="1" and Col[x-1]!="0" and Mov[x-1]!="1" and x not in Bord:
               left=False
        for x in range(0,251):    
            if Col[x]!="0" and Col[x-1]=="0" and Mov[x]=="1" and left==True and x not in Bord:   
                  Col[x-1]=Col[x]
                  Col[x]="0"
                  Mov[x-1]="1"
                  Mov[x]="0"
                  stop=True
        Draw()
    x=0
    if keys[py.K_RIGHT] and int(py.time.get_ticks()) % 100 ==True and stop==False:
        right=True
        for x in range(249,0,-1):
           if Mov[x]=="1" and Col[x+1]!="0" and Mov[x+1]!="1" and x not in Bord:
               right=False
        for x in range(249,0,-1):    
            if Col[x]!="0" and Col[x+1]=="0" and Mov[x]=="1" and right==True and x not in Bord:   
                  Col[x+1]=Col[x]
                  Col[x]="0"
                  Mov[x+1]="1"
                  Mov[x]="0"
                  stop=True
        Draw()
    
    if keys[py.K_UP] and int(py.time.get_ticks()) % 1000 ==True and stop==False:
#    if True:
        for x in range(240,0,-1):
            if Col[x]!="0" and Mov[x]=="1" and x not in Bord:
                piece=Col[x]
                
                break
        if piece =="1":
            
            if pos1 == False:
                      if Mov[x]=="1" and x not in Bord and x>12:
                          if Col[x+11]=="0" and Col[x+23]=="0" and Col[x+35]=="0":
                              Col[x-3]="0"
                              Col[x-2]="0"
                              Col[x]="0"
                              Mov[x-3]="0"
                              Mov[x-2]="0"
                              Mov[x]="0"
                              Col[x+11]="1"
                              Col[x+23]="1"
                              Col[x+35]="1"
                              Mov[x+11]="1"
                              Mov[x+23]="1"
                              Mov[x+35]="1"
                              Draw()                            
            if pos1 ==True:
               
                      if Mov[x]=="1" and x not in Bord and x>12:
                          if Col[x-23]=="0" and Col[x-25]=="0" and Col[x-26]=="0" :
                              Col[x-36]="0"
                              Col[x-12]="0"
                              Col[x]="0"
                              Mov[x-36]="0"
                              Mov[x-12]="0"
                              Mov[x]="0"
                              Col[x-23]="1"
                              Col[x-25]="1"
                              Col[x-26]="1"
                              Mov[x-25]="1"
                              Mov[x-23]="1"
                              Mov[x-26]="1"
                              Draw()
            pos1=not pos1
            Draw()
        if piece =="2":
            if pos1 == False:
                      if Mov[x]=="1" and x not in Bord and x>25:
                          if Col[x-25]=="0" and Col[x-2]=="0":
                              Col[x-1]="0"
                              Col[x]="0"
                              Mov[x-1]="0"
                              Mov[x]="0"
                              Col[x-2]="2"
                              Col[x-25]="2"
                              Mov[x-2]="1"
                              Mov[x-25]="1"
                              Draw()
                            
            if pos1 ==True:
               
                      if Mov[x]=="1" and x not in Bord and x>23:
                          if Col[x+1]=="0" and Col[x+2]=="0":
                              Col[x-23]="0"
                              Col[x]="0"
                              Mov[x-23]="0"
                              Mov[x]="0"
                              Col[x+1]="2"
                              Col[x+2]="2"
                              Mov[x+1]="1"
                              Mov[x+2]="1"
                              Draw()
            pos1=not pos1
            Draw()
        if piece =="3":
            if pos2 == 0:
                      if Mov[x]=="1" and x not in Bord and x>24:
                          if Col[x-24]=="0":
                              Col[x-11]="0"
                              Mov[x-11]="0"
                              Col[x-24]="3"
                              Mov[x-24]="1"
                              pos2=1
                              Draw()
                              
            elif pos2 ==1:
               
                      if Mov[x]=="1" and x not in Bord and x>12:
                          if Col[x-11]=="0":
                              Col[x]="0"
                              Mov[x]="0"
                              Col[x-11]="3"
                              Mov[x-11]="1"
                              pos2=2
                              Draw()
            elif pos2 ==2:
               
                      if Mov[x]=="1" and x not in Bord and x>12:
                          if Col[x+11]=="0":
                              Col[x-2]="0"
                              Mov[x-2]="0"
                              Col[x+11]="3"
                              Mov[x+11]="1"
                              pos2=3
                              Draw()
            elif pos2 ==3:
               
                      if Mov[x]=="1" and x not in Bord and x>24:
                          if Col[x-13]=="0":
                              Col[x-24]="0"
                              Mov[x-24]="0"
                              Col[x-13]="3"
                              Mov[x-13]="1"
                              pos2=0
                              Draw()
            Draw()
        if piece =="4":
            if pos2 == 0:
                      if Mov[x]=="1" and x not in Bord and x>10:
                          if Col[x+2]=="0" and Col[x+14]=="0":
                              Col[x]="0"
                              Col[x-12]="0"
                              Mov[x-12]="0"
                              Mov[x]="0"
                              Col[x+2]="4"
                              Col[x+14]="4"
                              Mov[x+14]="1"
                              Mov[x+2]="1"
                              pos2=1
                              Draw()
                              
            elif pos2 ==1:
               
                      if Mov[x]=="1" and x not in Bord and x>25:
                          if Col[x-1]=="0" and Col[x-2]=="0":
                              Col[x-24]="0"
                              Mov[x-24]="0"
                              Col[x-25]="0"
                              Mov[x-25]="0"
                              Col[x-1]="4"
                              Mov[x-1]="1"
                              Col[x-2]="4"
                              Mov[x-2]="1"                       
                              pos2=2
                              Draw()
            elif pos2 ==2:
               
                      if Mov[x]=="1" and x not in Bord and x>25:
                          if Col[x-14]=="0" and Col [x-26]=="0":
                              Col[x]="0"
                              Mov[x]="0"
                              Col[x-12]="0"
                              Mov[x-12]="0"
                              Col[x-14]="4"
                              Mov[x-14]="1"
                              Col[x-26]="4"
                              Mov[x-26]="1"
                              pos2=3
                              Draw()
            elif pos2 ==3:
               
                      if Mov[x]=="1" and x not in Bord and x>25:
                          if Col[x-24]=="0" and Col[x-23]=="0":
                              Col[x]="0"
                              Mov[x]="0"
                              Col[x-1]="0"
                              Mov[x-1]="0"
                              Col[x-24]="4"
                              Mov[x-24]="1"
                              Col[x-23]="4"
                              Mov[x-23]="1"
                              pos2=0
                              Draw()
            Draw()
        if piece =="5":
            if pos2 == 0:
                      if Mov[x]=="1" and x not in Bord and x>10:
                          if Col[x+12]=="0" and Col[x+11]=="0":
                              Col[x-13]="0"
                              Col[x-14]="0"
                              Mov[x-14]="0"
                              Mov[x-13]="0"
                              Col[x+12]="5"
                              Col[x+11]="5"
                              Mov[x+11]="1"
                              Mov[x+12]="1"
                              pos2=1
                              Draw()
                              
            elif pos2 ==1:
               
                      if Mov[x]=="1" and x not in Bord and x>25:
                          if Col[x-2]=="0" and Col[x-14]=="0":
                              Col[x-12]="0"
                              Mov[x-12]="0"
                              Col[x-24]="0"
                              Mov[x-24]="0"
                              Col[x-2]="5"
                              Mov[x-2]="1"
                              Col[x-14]="5"
                              Mov[x-14]="1"                       
                              pos2=2
                              Draw()
            elif pos2 ==2:
               
                      if Mov[x]=="1" and x not in Bord and x>25:
                          if Col[x-26]=="0" and Col [x-25]=="0":
                              Col[x]="0"
                              Mov[x]="0"
                              Col[x-1]="0"
                              Mov[x-1]="0"
                              Col[x-26]="5"
                              Mov[x-26]="1"
                              Col[x-25]="5"
                              Mov[x-25]="1"
                              pos2=3
                              Draw()
            elif pos2 ==3:
               
                      if Mov[x]=="1" and x not in Bord and x>25:
                          if Col[x-22]=="0" and Col[x-10]=="0":
                              Col[x]="0"
                              Mov[x]="0"
                              Col[x-12]="0"
                              Mov[x-12]="0"
                              Col[x-22]="5"
                              Mov[x-22]="1"
                              Col[x-10]="5"
                              Mov[x-10]="1"
                              pos2=0
                              Draw()
        if piece =="6":
            if pos1 == False:
                  if Mov[x]=="1" and x not in Bord and x>25:
                      if Col[x-25]=="0" and Col[x-13]=="0":
                          Col[x-1]="0"
                          Col[x-11]="0"
                          Mov[x-1]="0"
                          Mov[x-11]="0"
                          Col[x-13]="6"
                          Col[x-25]="6"
                          Mov[x-13]="1"
                          Mov[x-25]="1"
                          Draw()
                        
            if pos1 ==True:
           
                  if Mov[x]=="1" and x not in Bord and x>23:
                      if Col[x-1]=="0" and Col[x-11]=="0":
                          Col[x-25]="0"
                          Col[x-13]="0"
                          Mov[x-25]="0"
                          Mov[x-13]="0"
                          Col[x-1]="6"
                          Col[x-11]="6"
                          Mov[x-1]="1"
                          Mov[x-11]="1"
                          Draw()
            pos1=not pos1
        Draw()
        py.time.delay(100)   
    if keys[py.K_DOWN] and int(py.time.get_ticks()) % 60 ==True and stop==False:
        down=True
        for x in range(249,0,-1):
           if Mov[x]=="1" and Col[x+12]!="0" and Mov[x+12]!="1" and x not in Bord:
               down=False
        for x in range(228,0,-1):    
            if Col[x]!="0" and Col[x+12]=="0" and Mov[x]=="1" and down==True and x not in Bord:   
                  Col[x+12]=Col[x]
                  Col[x]="0"
                  Mov[x+12]="1"
                  Mov[x]="0"
        Draw()
    py.event.pump()
    if (py.time.get_ticks()) % 101 ==True:
        stop=False
    x=250
    b=True
#    if True:
    if int(py.time.get_ticks()) % 1000 ==True:         
        for x in range(250,0,-1):
            if x % 50 ==True:
                Draw()
            if Col[x]!="0" and Mov[x]=="1" and x not in Bord and x<245 and b==True:
                            s=True
                            if Col[x+12]=="0":
                                Col[x+12]=Col[x]
                                Mov[x+12]="1"
                                Col[x]="0"
                                Mov[x]="0"
                            else:
                                b=False                          
                                last=x
                                break
        if b==False:
            for x in range (last,240,+1):
                  if x<239:
                    if Mov[x+12]!="0":
                        Col[x]=Col[x+12]
                        Col[x+12]="0"
            Mov=["0"]
            Mov=Mov*251
         
        if s==False:
            break
    Draw()
    py.event.pump()
py.quit()            