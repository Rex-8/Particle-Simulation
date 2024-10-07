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

#starter place
x_dflt = (WW-BW)//2
y_dflt = 20

#adding a new block
def new_b(a,col):
    pygame.draw.rect(win,col, pygame.Rect(a[0],a[1], BW, BH),4)

#replacing block position
def rep_b(a):
    x,y = a
    check = ((x!=0)and(x<WW-(BW))and(y<WH-(BH)))
    if check == True:
        dd  = win.get_at((x,y+10))
        ddl = win.get_at((x-10,y+10))
        ddr = win.get_at((x+10,y+10))
        if (dd == GREY):
            new_b((x,y),GREY)
            new_b((x,y+10),SAND)
            return (x,y+10)
        elif (ddl == GREY):
            new_b((x,y),GREY)
            new_b((x-10,y+10),SAND)
            return (x-10,y+10)
        elif (ddr == GREY):
            new_b((x,y),GREY)
            new_b((x+10,y+10),SAND)
            return (x+10,y+10)
        elif (ddr == ddl == dd == SAND):
            new_b(a,SAND)
            return None
    if check == False:
        return None

#Graphics and Main
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
            if position[n] == None:
                position.remove(position[n])
            elif position[n] != None:
                position[n] = rep_b(position[n])
        except:
            pass
            
    clock.tick(80)
    pygame.display.flip()

pygame.quit()
