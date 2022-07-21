list=[10,20,30,40,50]
list1=[]
for i in range(len(list)):
    list1.insert(i,list[-1])
    
print(list)
print(list1)