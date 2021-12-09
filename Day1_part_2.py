import itertools

j=3
i=0
count=0
resevered_list=[]
with open('input', 'r') as f:
    f_list=f.read().split()
    generated_list = list(map(int, f_list))
    for x in generated_list:
        
        if (i==0):
            resevered_list=list(itertools.islice(generated_list,i,j,1))
            previous_sum=sum(resevered_list)
            i=i+1
            j=j+1
        
        else:
            resevered_list=list(itertools.islice(generated_list,i,j,1))
            if(len(resevered_list)==3):    
                current_sum=sum((list(itertools.islice(generated_list,i,j,1))))
                if previous_sum<current_sum:
                    count=count+1
                previous_sum=current_sum
                i=i+1
                j=j+1
print(f"The result is: {count}")
