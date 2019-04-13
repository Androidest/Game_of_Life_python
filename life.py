import pygame,sys,time
from pygame.locals import *
pygame.init()
XX,YY=1366,768
win=pygame.display.set_mode((XX,YY),0,32)
l,data,w=[],{},3
added,deleted=[(621,288),(594,291),(597,291),(615,291),(618,291),\
               (591,294),(603,294),(615,294),(618,294),(588,297),\
               (606,297),(615,297),(618,297),(588,300),(600,300),\
               (606,300),(609,300),(621,300),(588,303),(606,303),\
               (591,306),(603,306),(594,309),(597,309),(558,297),\
               (561,297),(558,300),(561,300),(627,285),(627,288),\
               (627,300),(627,303),(657,291),(660,291),(657,294),\
               (660,294)],[]
for (x,y) in added:l.append((x+90,y+120))
for (x,y) in added:l.append((x-60,y+78))
for (x,y) in added:l.append((x+81,y-150))
for (x,y) in added:l.append((x-99,y-60))
added=added+l
display=added[:]
win.fill((0,0,0))
for i in display:pygame.draw.rect(win,(0,255,0),Rect(i,(2,2)))
pygame.display.flip()
def terminate():
    exit()
    pygame.quit()
while 1:
    for e in pygame.event.get():
             if e.type==QUIT:
                 terminate()
    win.fill((0,0,0))
    for (x,y) in added:
        x0,x1=x-w,x+w
        y0,y1=y-w,y+w
        if (x,y) not in data:data[(x,y)]=0
        l=[(x0,y0),(x,y0),(x1,y0),(x0,y),(x1,y),(x0,y1),(x,y1),(x1,y1)]
        for i in l:
            try:data[i]+=1
            except:data[i]=1
    for (x,y) in deleted:
        x0,x1=x-w,x+w
        y0,y1=y-w,y+w
        l=[(x0,y0),(x,y0),(x1,y0),(x0,y),(x1,y),(x0,y1),(x,y1),(x1,y1)]
        for i in l:
            data[i]-=1
    added,deleted=[],[]
    l=list(data)
    for i in l:
        if data[i]==3:
            if i not in display:
                 added.append(i)
                 display.append(i)
    for i in display[::]:
        if data[i]!=2 and data[i]!=3:
            deleted.append(i)
            if data[i]==0:del data[i]
            display.remove(i)       
        else:
            pygame.draw.rect(win,(0,255,0),Rect(i,(2,2)))
    
    pygame.display.flip()
    
