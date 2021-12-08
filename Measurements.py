

# Instructions https://adventofcode.com/2021/day/1

'''def increase_measurements():
    depth=[199,200,208,210,200,207,240,269,260,263]
    a=0
    print(len(depth))
    for x in range(len(depth)-1):
        if(depth[x+1]>depth[x]):
            a=a+1
    print(a)'''

depth=[199,200,208,210,200,207,240,269,260,263,262]
def increase_measurements():
 return sum([1 for x in range(len(depth)-1) if(depth[x+1]>depth[x])])
    
            
print(increase_measurements())
