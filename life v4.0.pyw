import pygame,sys,time
from random import choice
from pygame.locals import *
pygame.init()
XX,YY=1200,650
win=pygame.display.set_mode((XX,YY),0,32)
data,w={},3
deleted=[]
f=open('save_data.txt')
generation=eval(f.readline().rstrip())#generation,number
old_lifetime=eval(f.readline().rstrip())#old_lifetime,number,second
old_cells=eval(f.readline().rstrip())#old_cells,point list
f.close()
new_cells=old_cells[:]
l3=[i*3 for i in range(-9,10)]
l3.remove(3)
l3.remove(-3)
l3.remove(0)
def terminate():
    exit()
    pygame.quit()
def one(nl,ol):
    while 1:
        p=choice(ol)
        p1=(p[0]+choice([-3,3,0]),p[1]+choice([-3,3,0]))
        if p1 not in ol:
            nl.append(p1)
            return
def two(nl,ol):
    x=1
    while x<1000:
        x+=1
        p=choice(ol)
        p1=(p[0]+choice([-3,3,0]),p[1]+choice([-3,3,0]))
        p2=(p1[0]+choice([-3,3,0]),p1[1]+choice([-3,3,0]))
        if (p1!=p2) and (p1 not in ol) and (p2 not in ol):
            nl.append(p1)
            nl.append(p2)
            return
    i=choice(q)
    i(nl,ol) 
def three(nl,ol):
    x=1
    while x<700:
        x+=1
        p=choice(ol)
        p1=(p[0]+choice(l3),p[1]+choice(l3))
        p2=(p1[0]+choice([-3,3,0]),p1[1]+choice([-3,3,0]))
        p3=(p1[0]+choice([-3,3,0]),p1[1]+choice([-3,3,0]))
        if (p1!=p2) and (p3!=p2) and (p3!=p1):
            if (p3 not in ol) and (p2 not in ol) and (p1 not in ol):
                nl.append(p1)
                nl.append(p2)
                nl.append(p3)
                return
    i=choice(q)
    i(nl,ol)
q=[one,two,three,three,three]
def add_cell(ol):
    nl=ol[:]
    for i in range(choice([1,2,1,1])):
       i=choice(q)
       i(nl,ol)
    return nl
def remove_cell(ol):
    nl=ol[:]
    p=choice(ol)
    nl.remove(p)
    return nl
def move_cell(ol):
    nl=ol[:]
    while 1:
        p=choice(ol)
        p1=(p[0]+choice([-3,3,0]),p[1]+choice([-3,3,0]))
        if p1 not in ol:
            nl.remove(p)
            nl.append(p1)
            return nl
revolution=[add_cell,add_cell,add_cell,remove_cell,move_cell]
while 1:
    generation+=1
    added=new_cells[:]
    display=dict(zip(added,[[x,y] for (x,y) in added]))
    start=time.clock()
    flip,new_changes,old_changes=0,{},{}
    catch,movedx,movedy=0,0,0
    while 1:
        flip+=1
        if flip>7:
            flip=1
            new_changes,old_changes={},{}     
        for e in pygame.event.get():
            if e.type==QUIT:
                terminate()
            if e.type==MOUSEBUTTONDOWN:
                mouseleft,mousemid,mouseright=pygame.mouse.get_pressed()
                if mouseleft:
                    catch=1
            if e.type==MOUSEBUTTONUP:
                mouseleft,mousemid,mouseright=pygame.mouse.get_pressed()                 
                if mouseleft==0:
                    catch=0    
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
                     new_changes[i]=0
                     display[i]=[i[0]+movedx,i[1]+movedy]
        tx,ty=pygame.mouse.get_rel()
        if catch:
            movedx+=tx
            movedy+=ty
            for i in display:
                display[i][0]+=tx
                display[i][1]+=ty
        l=list(display)
        for i in l:
            if (data[i]!=2 and data[i]!=3) or (i[0]>1700 or i[0]<-350 or i[1]<-400 or i[1]>1200):
                deleted.append(i)
                if data[i]==0:del data[i]
                del display[i]       
            else:
                pygame.draw.rect(win,(0,255,0),Rect(display[i],(2,2)))
        if old_changes!=new_changes:old_changes=new_changes.copy()
        else:break
        pygame.display.flip()
       
    end=time.clock()
    new_lifetime=int(end-start)
    data,deleted={},[]
    if new_lifetime>=old_lifetime:
        old_lifetime=new_lifetime
        old_cells=new_cells[:]
        f=open('save_data.txt','w')
        f.write(str(generation)+'\n')#generation,number
        f.write(str(old_lifetime)+'\n')#old_lifetime,number,second
        f.write(str(old_cells)+'\n')#old_cells,point list
        f.close()
    i=choice(revolution)
    new_cells=i(old_cells)
    

    
