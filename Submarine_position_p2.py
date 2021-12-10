

horizontial=0
depth=0
aim=0
with open('input', 'r') as f:
    list_input=f.readlines()
    clean_list= [x.strip("\n").split() for x in list_input]
    for i in clean_list:
        direction=i[0]
        number=int(i[1])
        if direction=="forward":
            horizontial=horizontial + number
            depth=(aim*number)+depth
        elif direction=="up":
            aim=aim-number
        elif direction=="down":
            aim=aim+number
    print(depth*horizontial)
   

