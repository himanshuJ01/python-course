x= lambda a:a+20
print(x(5))

def f1(n):
    return lambda a:a*n

doub =f1(2)
trip=f1(3)

print(doub(11))
print(trip(11))

#filter

def prime(x):
    for n in range(2,x):
        if x%n == 0:
            return False
    else:
        return True
filtered= filter(prime,range(10))
print("Prime number are: ", list(filtered))     


#map

def square(x):
    return x*x
numbers=[1,2,3,4,5]
listsquare = map(square,numbers)
print(list(listsquare))