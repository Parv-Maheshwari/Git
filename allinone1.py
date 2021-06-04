import cv2
import numpy as np
from queue import PriorityQueue
import math
import time

path="Task_1_Low.png"
img=cv2.imread(path)
img1=img2=img3=img4=img5=img6=img7=img8=img9=img10=img11=img12=img

cv2.namedWindow("map1",cv2.WINDOW_NORMAL)
cv2.namedWindow("map2",cv2.WINDOW_NORMAL)
cv2.namedWindow("map3",cv2.WINDOW_NORMAL)
cv2.namedWindow("map4",cv2.WINDOW_NORMAL)
cv2.namedWindow("map5",cv2.WINDOW_NORMAL)
cv2.namedWindow("map6",cv2.WINDOW_NORMAL)
cv2.namedWindow("map7",cv2.WINDOW_NORMAL)
cv2.namedWindow("map8",cv2.WINDOW_NORMAL)
cv2.namedWindow("map9",cv2.WINDOW_NORMAL)
cv2.namedWindow("map10",cv2.WINDOW_NORMAL)
cv2.namedWindow("map11",cv2.WINDOW_NORMAL)
cv2.namedWindow("map12",cv2.WINDOW_NORMAL)

obstacle_color=(255,255,255)
start_color=(45,204,113)
end_color=(231,76,60)

m,n,l=img.shape

dist1=dist2=dist3=dist4=dist5=dist6=dist7=dist8=dist9=dist10=dist11=dist12 = np.full((m, n), np.inf)
q1=q2=q3=q4=q5=q6=q7=q8=q9=q10=q11=q12 = PriorityQueue()

for x in range(m):
    for y in range(n):
        b,g,r=img[x,y]
        if b==start_color[2] and g==start_color[1] and r==start_color[0]:
            source=(x,y)
        if b==end_color[2] and g==end_color[1] and r==end_color[0]:
            end=(x,y)

class Node:
    def __init__(self,position=None, parent=None):
        self.position = position
        self.parent = parent

        self.g=0

    def __eq__(self, other):
        return self.g == other.g

    def __lt__(self, other):
        return self.g < other.g
    
    def __gt__(self, other):
        return self.g > other.g

def isValid(position):
    x,y=position
    if(x >= 0 and y >= 0 and x < img.shape[0] and y < img.shape[1] and (img[position] != obstacle_color).any()):
        return True
    return False

def distance(a,b):
    dist=math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    return dist

def getpath(current,pic):
    while current is not None:
        pic[current.position]=(112,25,25)
        current=current.parent

def dijkstra1():

    start=Node(source,None)
    start.g=0

    dest=Node(end,None)
    dest.g=0

    q1.put(start)
    dist1[start.position[0],start.position[1]]=0

    while not q1.empty():
        current=q1.get()

        img1[current.position]=(0, 140, 255)

        if current.position==dest.position:
            getpath(current,img1)
            break

        for i in range(-1,2):
            for j in range(-1,2):
                if (i!=0 and j!=0):
                    continue
                pos=(current.position[0]+i,current.position[1]+j)
                if not isValid(pos):
                    continue
                
                child=Node(pos,current)
                child.g=current.g+distance(child.position,current.position)
                
                if child.g<dist1[pos[0],pos[1]]:                    
                    img1[pos[0],pos[1]]=(255,0,0)
                    dist1[pos[0],pos[1]]=child.g
                    q1.put(child)

    return(current.g)

def dijkstra2():
    start=Node(source,None)
    start.g=0

    dest=Node(end,None)
    dest.g=0

    q2.put(start)
    dist2[start.position[0],start.position[1]]=0

    while not q2.empty():
        current=q2.get()

        img1[current.position]=(0, 140, 255)

        if current.position==dest.position:
            getpath(current,img2)
            break

        for i in range(-1,2):
            for j in range(-1,2):
                pos=(current.position[0]+i,current.position[1]+j)
                if not isValid(pos):
                    continue
                
                child=Node(pos,current)
                child.g=current.g+distance(child.position,current.position)
                
                if child.g<dist2[pos[0],pos[1]]:                    
                    img1[pos[0],pos[1]]=(255,0,0)
                    dist2[pos[0],pos[1]]=child.g
                    q2.put(child)

    return(current.g)

start_time=time.time()
print(dijkstra1())
print("time: %s seconds" % (time.time() - start_time))
cv2.imshow("map1",img1.astype(np.uint8))
cv2.waitKey(0)

start_time=time.time()
print(dijkstra2())
print("time: %s seconds" % (time.time() - start_time))
cv2.imshow("map2",img2.astype(np.uint8))
cv2.waitKey(0)