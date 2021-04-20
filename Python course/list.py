
#Ordered, Changeable and allow duplicates

list=["car","bike",30,40,True]
for a in list:
    print(a)

print(len(list))    
print(list[2:5])
list[4]="hello"
print(list[4])

list.insert(3,"jeep")

print(list)

list.append("Oranges")

print(list)