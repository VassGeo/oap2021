import numpy as np

intersection=0

with open('input', 'r') as f:
    l=f.readlines()
    clean_list=[x.strip("\n").split("->")for x in l]
    point11=[k[0].split(",") for k in clean_list]
    point22=[k[1].split(",") for k in clean_list]
    x1=[list(map(int,p1[0].split(","))) for p1 in point11]
    y1=[list(map(int,p1[1].strip(" ").split(",")))for p1 in point11]
    x2=[list(map(int,p2[0].strip(" ").split(","))) for p2 in point22]
    y2=[list(map(int,p2[1].split(","))) for p2 in point22]
    x1_x2=x1+x2
    x_max=max(x1_x2)
    y1_y2=y1+y2
    y_max=max(y1_y2)
    
    arr=np.zeros(shape=(y_max[0]+1,x_max[0]+1))
    
    for k in clean_list:
        point1=k[0].split(",")
        x1=list(map(int,point1[0].split(","))) 
        y1=list(map(int,point1[1].strip(" ").split(",")))

        point2=k[1].split(",")
        x2=list(map(int,point2[0].strip(" ").split(",")))
        y2=list(map(int,point2[1].split(",")))
        
        #x -axis(horizontal)
        
        if  y1[0]==y2[0]:
            a=min(x1[0],x2[0])
            b=max(x1[0],x2[0])
            for i in range(a,b+1):
                
                arr[y1[0]][i]+=1
                
                if arr[y1[0]][i] == 2:
                    intersection+=1

          #y-axis vertical
                    
        if x1[0]==x2[0]:
            c=min(y1[0],y2[0])
            d=max(y1[0],y2[0])
            
            for j in range(c,d+1):
                
                arr[j][x1[0]]+=1
                
                if arr[j][x1[0]]==2:
                    intersection+=1
                    
    print(intersection)
   
            
    

