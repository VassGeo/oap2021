
from collections import defaultdict



coordinates=[]
intersection=0
d=defaultdict(lambda:0)

def getpoints(x):
    return [tuple([tuple([int(z) for z in y.split(',') if int(z)]) for y in x.split(' -> ')])]

    
def x_axis(x1,y1,x2):
    global intersection
    a=min(x1,x2)
    b=max(x1,x2)
        
    for key in range(a,b+1):
            
        d[(key,y1)]+=1
        if d[(key,y1)] == 2:
            intersection+=1
    return intersection
        


def y_axis(x1,y1,y2):
    global intersection
    c=min(y1,y2)
    e=max(y1,y2)
    for key in range(c,e+1):
        d[(x1,key)]+=1
        if d[(x1,key)]==2:
            intersection+=1
    return intersection
        


with open('input', 'r') as f:
    for x in f.readlines():
        if x:
            coordinates.append(getpoints(x))

for i in coordinates:
    
    point1,point2= i[0]
    
    (x1,y1)=point1
    
    (x2,y2)=point2

    if  y1==y2:
        x_axis(x1,y1,x2)
    if x1==x2:
        y_axis(x1,y1,y2)
                    
print(f"the result is {intersection}")
   
            
    

