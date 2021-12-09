depth=[]
a1=0
with open('input', 'r') as f:
    depth=f.read().split()
    for index, x in enumerate (depth):
        if(index==0):
            prev_el =int(depth[index])
        else:
            if (int(prev_el)<int(depth[index])):
                
                prev_el=int(depth[index])
                a1+=1
                
            else:
                prev_el=int(depth[index])
                
            

print(a1)
