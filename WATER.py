import pygame

#Block Dimensions
BW = 10
BH = 10

#Window Dimensions
WW = 1000
WH = 600

#Colours
BLUE  = (0,0,128)
GREEN = (0,128,0)
RED   = (128,0,0)
BLACK = (0,0,0)
GREY  = (128,128,128)
WHITE = (255,255,255)
SAND  = (194,178,128)

pygame.init()
win = pygame.display.set_mode((WW,WH))
win.fill(GREY)

def new_b(a,col):
    pygame.draw.rect(win,col, pygame.Rect(a[0],a[1], BW, BH),4)

def rep_b(a):
    x = a[0]
    y = a[1]
    check = ((x!=0)and(x<WW)and(y<WH))
    if check == True:
        dd = win.get_at((x,y+10))
        dl = win.get_at((x-10,y+10))
        dr = win.get_at((x+10,y+10))
        ll = win.get_at((x-10,y))
        rr = win.get_at((x+10,y))

        if dd == GREY:
            new_b((x,y),GREY)
            new_b((x,y+10),BLUE)
            return (x , y+10)
        elif dl == GREY:
            new_b((x,y),GREY)
            new_b((x-10,y+10),BLUE)
            return (x-10,y+10)
        elif dr == GREY:
            new_b((x,y),GREY)
            new_b((x+10,y+10),BLUE)
            return (x+10,y+10)
        elif ll == GREY:
            new_b((x,y),GREY)
            new_b((x-10,y),BLUE)
            return (x-10,y)
        elif rr == GREY:
            new_b((x,y),GREY)
            new_b((x+10,y),BLUE)
            return (x+10,y)
    elif check == False:
        return a
        
#Graphics and Main
a = (500,20)
clock = pygame.time.Clock()
run = True
position = []
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if (pygame.mouse.get_pressed())[0] == True:
        d = pygame.mouse.get_pos()
        d1 = []
        d1.append((d[0]//10)*10)
        d1.append((d[1]//10)*10)
        position.append(d1)
            
    for n in range(len(position)):
        try:
            position[n] = rep_b(position[n])
        except:
            pass
            
    clock.tick(20)
    pygame.display.flip()
pygame.quit()
