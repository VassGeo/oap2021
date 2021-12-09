from Measurements import find

count=0
previous_sum=0
new_list=[]
Sums_list =[]
with open('input', 'r') as f:
    l=f.read().split()
    int_list=list(map(int, l))
    new_list=int_list[0:3]
    previous_sum=sum(new_list)
    Sums_list.append(previous_sum)
    for x in int_list[3:]:
        new_list.append(x)
        current_sum=sum(new_list[-3:])
        Sums_list.append(current_sum)

print(find(Sums_list))


