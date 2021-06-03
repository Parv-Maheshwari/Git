import cv2 
import numpy as np 
import math
import time
import heapq

img = cv2.imread(r"C:\Users\himad\OneDrive\NokiaXpress\Public\Pictures\Task 1 Data\Task_1_Low.png")
count_x = 0
count_y = 0
start = np.array([113,204,45])
end = np.array([60,76,231])
nav_path = np.array([0,0,0])
obs = np.array([255,255,255])

start_co = []
end_co = []

for i in img:
    for j in i:
        if np.array_equal(j,start):
            start_co.append(count_x)
            start_co.append(count_y)

        if np.array_equal(j,end):
            end_co.append(count_x)
            end_co.append(count_y)

        count_y += 1

    count_x +=1
    count_y = 0

class Node():

    def __init__(self, parent=None, position=None,f=None,g=None,h=None):
        self.parent = parent
        self.position = position
        self.f = f
        self.h = h
        self.g = g

    def __lt__(self, other):
        return self.f < other.f

node_list = []
for i in range(100):
    node_list.append([])
    for j in range(100):
        node_list[i].append(Node(parent=None,position=(i,j),f=math.inf,g=math.inf,h=math.inf))


def is_blocked(point):
    if np.array_equal(img[point],[255,255,255]):
        return True
    return False

def get_neighbors(point):
    x,y = point
    neighbors = []
    if x > 0:
        neighbors.append((x-1,y))
    if x < 99:
        neighbors.append((x+1,y))
    if y > 0: 
        neighbors.append((x,y-1))
    if y < 99:
        neighbors.append((x,y+1))   
    # if x > 0 and y > 0:
    #     neighbors.append((x-1,y-1))
    # if x < 99 and y > 0:
    #     neighbors.append((x+1,y-1))  
    # if x < 99 and y < 99:
    #     neighbors.append((x+1,y+1))
    # if x > 0 and y < 99:
    #     neighbors.append((x-1,y+1))

    points = []
    for i in neighbors:
        if not is_blocked(i):
            points.append(i)

    return points


def get_dist(point_1,point_2):
    x0,y0 = point_1
    x1,y1 = point_2

    #returning the diagonal distance
    # return max(abs(x1-x0),abs(y1-y0))

    #returning the manhattan distance 
    # return abs(x1-x0) + abs(y1-y0)

    #returning the euclidean distance
    # return math.sqrt((x1-x0)**2 + (y1-y0)**2)

    #if we just return 0 it will turn out Astar into a djikstra
    # return 0

    #returning a non admissible heurestic 
    return (x1-x0)**2 + (y1-y0)**2

    #returning an admissible heurestic 
    # return min(abs(x1-x0),abs(y1-y0))

def Astar(start,end):
    Q = []
    node_list[start[0]][start[1]].g = 0
    node_list[start[0]][start[1]].h = get_dist(start,end)
    node_list[start[0]][start[1]].f = node_list[start[0]][start[1]].h + node_list[start[0]][start[1]].g
    heapq.heappush(Q,node_list[start[0]][start[1]])

    while len(Q)>0:

        current = heapq.heappop(Q)

        if current.position == end:
            return (current,Q)
            break

        for i in get_neighbors(current.position):
            temp_g = current.g + 1
            if temp_g < node_list[i[0]][i[1]].g:
                node_list[i[0]][i[1]].g = temp_g
                node_list[i[0]][i[1]].f = node_list[i[0]][i[1]].g + get_dist(node_list[i[0]][i[1]].position , end)
                node_list[i[0]][i[1]].parent = current

                if not node_list[i[0]][i[1]] in Q:
                    img[i[0],i[1]] = [255,155,0]
                    heapq.heappush(Q,node_list[i[0]][i[1]])

def out_image():
    new_list = []
    check_list = []
    for i in img:
        for j in i:
            for k in range(10):
                new_list.append(j)
                check_list.append(j)
        for l in range(9):
            for m in check_list:
                new_list.append(m)
        check_list = []
        

    
    arr = np.array(new_list)
    arr0 = arr.reshape(1000,1000,3)

    return arr0

t1 = time.time()
path,unproccessed = Astar((start_co[0],start_co[1]),(end_co[0],end_co[1]))
t2 = time.time()
print(t2-t1)

count = 0
while path.parent is not None:
    img[path.position] = [0,0,255]
    path = path.parent
    count += 1
print(count)

for i in unproccessed:
    img[i.position] = [255,0,0]

new_img = out_image()
print(node_list[end_co[0]][end_co[1]].g)

cv2.imwrite(r"C:\Users\himad\OneDrive\NokiaXpress\Public\Pictures\Task 1 Data\Case_1_NonAdmissible_Distance_Low_Output.png", img)
cv2.imwrite(r"C:\Users\himad\OneDrive\NokiaXpress\Public\Pictures\Task 1 Data\Case_1_NonAdmissible_Distance_High_Output.png",new_img)
cv2.imshow('res2',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
            
                


