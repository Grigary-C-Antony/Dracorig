import pygame
import random
size="500x500".split("x")#input("enter playground size Width x height==>")
width=int(size[0])
height=int(size[1])
pygame.init()
dis=pygame.display.set_mode((width,height))
# pygame.display.update()
pygame.display.set_caption("snake game by GCA")
gameover=False
red=(255,0,0)
white=(255,255,255)
green=(0,255,0)


x1=width/2#to get centre
y1=height/2 #to get centre

x1_changed=0
y1_changed=0
snake_speed=10#int(input("pls enter the snake speed ==>"))
 # its an equation 
foodx = round(random.randrange(0, width - 10) / 10.0) * 10.0
foody = round(random.randrange(0, width - 10) / 10.0) * 10.0

clock=pygame.time.Clock() #how many time should it go 
score=0
sl=[]
if score>10:
    snake_speed+=round(score/10)

while not gameover:
    
    colorlist=[(0,255,0),(0,255,255),(255,0,255),(255,255,0),(255,0,0),(0,0,255)]
    color=random.choice(colorlist)
    for event in pygame.event.get():
        print(event)
    if event.type==pygame.QUIT:
        gameover=True
    if event.type==pygame.KEYDOWN:#here we will define the snake coordinates
        if event.key==pygame.K_LEFT:
            x1_changed=-10
            y1_changed=0
        elif event.key==pygame.K_RIGHT:
            x1_changed=10
            y1_changed=0
        elif event.key==pygame.K_UP:
            y1_changed=-10
            x1_changed=0
        elif event.key==pygame.K_DOWN:
            y1_changed=10
            x1_changed=0
    if x1>width:
        x1=0
    if x1<0:
        x1=width
    if y1>height:
        y1=0
    if y1<0:
        y1=height
        
 
    # print(x1_changed)
    x1+=x1_changed
    y1+=y1_changed
    dis.fill((0,0,0))
    pygame.draw.rect(dis,white,[x1,y1,10,10])
    pygame.draw.rect(dis,color,[foodx,foody,10,10])
    

    sls=[]
    sls.append(x1)
    sls.append(y1)
    sl.append(sls)
    if score>=1:
        for i in sl:
            pygame.draw.rect(dis,white,[i[0],i[1],10,10])
            
    if len(sl)>score:
        del sl[0]
        

    for x in sl[:-1]:
            if x == sls:
                gameover = True


    pygame.display.update()
    
    if x1==foodx and y1==foody:
        score+=1
        print(score)
        foodx = round(random.randrange(0, width - 10) / 10.0) * 10.0
        foody = round(random.randrange(0, width - 10) / 10.0) * 10.0
        pygame.display.set_caption(f"your score==> {score} speed==>{snake_speed}")
    

 
    clock.tick(snake_speed)
pygame.quit()
quit()
