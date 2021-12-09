 

# Instructions https://adventofcode.com/2021/day/1


def find(depth):
        a1=0
        for index, x in enumerate (depth):
            if(index==0):
                prev_el =int(depth[index])
            else:
                if (int(prev_el)<int(depth[index])):
                
                    prev_el=int(depth[index])
                    a1+=1
                
                else:
                    prev_el=int(depth[index])
        return(a1)



    
 
