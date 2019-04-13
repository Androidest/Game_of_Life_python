import pygame,sys,time
from random import choice
from pygame.locals import *
pygame.init()
XX,YY=1200,650
win=pygame.display.set_mode((XX,YY),0,32)
w,w1,t,n=16,13.6,0.09,0.3
add_cell=False
def terminate():
    exit()
    pygame.quit()
while 1:
    added,escape,kill_cell=[],False,False
    data,deleted={},[]
    catch,movedx,movedy,x0,y0=0,0,0,0,0
    bc,dc=255,-1
    while 1:
        win.fill((0,0,0))
        for e in pygame.event.get():
            if e.type==QUIT:
                terminate()
            if e.type==KEYUP:
                if e.key==K_SPACE:escape=True
            if e.type==MOUSEBUTTONDOWN:
                mouseleft,mousemid,mouseright=pygame.mouse.get_pressed()
                if mouseleft:catch=True
                if mousemid:escape=True
                if mouseright:
                    x,y=pygame.mouse.get_pos()
                    x=x-((x-x0)%w)
                    y=y-((y-y0)%w)
                    if (x,y) not in added:add_cell=True
                    else:kill_cell=True
                if e.button==4 and w<30:
                    x,y=pygame.mouse.get_pos()
                    w2=w+1
                    w1=w2*0.85
                    x0,y0=(x0-x)/w*w2+x,(y0-y)/w*w2+y
                    for i in added[::]:
                        added.remove(i)
                        added.append(((i[0]-x)/w*w2+x,(i[1]-y)/w*w2+y))
                    w=w2
                if e.button==5 and w>3:
                    x,y=pygame.mouse.get_pos()
                    w2=w-1
                    w1=w2*0.85
                    x0,y0=(x0-x)/w*w2+x,(y0-y)/w*w2+y
                    for i in added[::]:                        
                        added.remove(i)
                        added.append(((i[0]-x)/w*w2+x,(i[1]-y)/w*w2+y))
                    w=w2
            if e.type==MOUSEBUTTONUP:
                mouseleft,mousemid,mouseright=pygame.mouse.get_pressed()
                if mouseright==0:
                    kill_cell=False
                    add_cell=False
                if mouseleft==0:catch=False
        dx,dy=pygame.mouse.get_rel()
        if catch:
            x0+=dx
            y0+=dy
            for i in added[::]:
                added.remove(i)
                added.append((i[0]+dx,i[1]+dy))
        if add_cell:
            x,y=pygame.mouse.get_pos()
            x=x-((x-x0)%w)
            y=y-((y-y0)%w)
            if (x,y) not in added:added.append((x,y))
        if kill_cell:
            x,y=pygame.mouse.get_pos()
            x=x-((x-x0)%w)
            y=y-((y-y0)%w)
            if (x,y) in added:added.remove((x,y))
        if escape:break
        for x,y in added:
            pygame.draw.rect(win,(0,255,0),Rect((x,y),(w1,w1)))
        if bc==225:dc=-1
        elif bc==5:dc=1
        bc+=dc
        pygame.draw.circle(win,(255,0,0),(1164,36),36)
        pygame.draw.circle(win,(0,0,0),(1164,36),28)
        pygame.draw.rect(win,(0,0,bc),Rect((1148,20),(31,31)))
        pygame.display.flip()
#---#################################################################
    escape,flip=False,0
    bc,dc=255,-1
    display=added[:]
    while 1:
        win.fill((0,0,0))
        flip+=t
        if flip>=1:
            flip=0
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
        for e in pygame.event.get():
            if e.type==KEYUP:
                if e.key==K_SPACE:escape=1
            if e.type==QUIT:
                terminate()
            if e.type==MOUSEBUTTONDOWN:
                mouseleft,mousemid,mouseright=pygame.mouse.get_pressed()
                if mousemid:escape=True
                if mouseleft:catch=1
                if e.button==4:
                    if mouseright and n<1:
                        n+=0.02
                        t=n*n
                    elif mouseright==0 and w<30:
                        x,y=pygame.mouse.get_pos()
                        w2=w+1
                        w1=w2*0.85
                        for i in added[::]:
                            added.remove(i)
                            added.append(((i[0]-x)/w*w2+x,(i[1]-y)/w*w2+y))
                        for i in deleted[::]:
                            deleted.remove(i)
                            deleted.append(((i[0]-x)/w*w2+x,(i[1]-y)/w*w2+y))
                        d=data.copy()
                        data={}
                        for i in d:
                            data[((i[0]-x)/w*w2+x,(i[1]-y)/w*w2+y)]=d[i]
                        for i in display[::]:
                            display.remove(i)
                            i=((i[0]-x)/w*w2+x,(i[1]-y)/w*w2+y)
                            display.append(i)
                        w=w2                        
                if e.button==5:
                    if mouseright and n>0:
                        n-=0.02
                        t=n*n
                    elif mouseright==0 and w>3:
                        x,y=pygame.mouse.get_pos()
                        w2=w-1
                        w1=w2*0.85
                        for i in added[::]:
                            added.remove(i)
                            added.append(((i[0]-x)/w*w2+x,(i[1]-y)/w*w2+y))
                        for i in deleted[::]:
                            deleted.remove(i)
                            deleted.append(((i[0]-x)/w*w2+x,(i[1]-y)/w*w2+y))
                        d=data.copy()
                        data={}
                        for i in d:
                            data[((i[0]-x)/w*w2+x,(i[1]-y)/w*w2+y)]=d[i]
                        for i in display[::]:
                            display.remove(i)
                            i=((i[0]-x)/w*w2+x,(i[1]-y)/w*w2+y)
                            display.append(i)
                        w=w2
            if e.type==MOUSEBUTTONUP:
                mouseleft,mousemid,mouseright=pygame.mouse.get_pressed()
                if mouseleft==0:catch=0
        dx,dy=pygame.mouse.get_rel()
        if catch:
            for i in added[::]:
                added.remove(i)
                added.append((i[0]+dx,i[1]+dy))
            for i in deleted[::]:
                deleted.remove(i)
                deleted.append((i[0]+dx,i[1]+dy))
            d=data.copy()
            data={}
            for i in d:
                data[(i[0]+dx,i[1]+dy)]=d[i]
            for i in display[::]:
                display.remove(i)
                display.append((i[0]+dx,i[1]+dy))
                pygame.draw.rect(win,(0,255,0),Rect(i,(w1,w1)))
        else:
            for i in display:pygame.draw.rect(win,(0,255,0),Rect(i,(w1,w1)))
        if escape:break
        if bc==225:dc=-5
        elif bc==5:dc=5
        bc+=dc
        pygame.draw.circle(win,(255,0,0),(1164,36),36)
        pygame.draw.circle(win,(0,0,0),(1164,36),28)
        pygame.draw.polygon(win,(0,0,bc),((1150,16),(1150,56),(1188,36)))
        pygame.display.flip()
    

    
