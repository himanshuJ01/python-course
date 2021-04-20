# ordered, unchanable and allow duplicates
tuples = ("car","bike" , 30 , 40, True)

print(len(tuples))

y=list(tuples)
y[2]="Hello"
x=tuple(y)

print(x)