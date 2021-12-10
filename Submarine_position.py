
final_list=[]
horizontial=0
depth=0
with open('input', 'r') as f:
    list_input=f.readlines()
    clean_list= [x.strip("\n").split() for x in list_input]
    for i in clean_list:
        direction=i[0]
        number=int(i[1])
        if direction=="forward":
            horizontial=horizontial + number
        elif direction=="up":
            depth=depth-number
        elif direction=="down":
            depth=depth+number
    print(depth*horizontial)
   

