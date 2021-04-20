fruits=["apples","bananas","kiwi","mangoes"]
newfruit=[]

for x in fruits:
    if "a" in x:
        newfruit.append(x)
print(newfruit)   

newfruit=[x for x in fruits if "i" in x]
print(newfruit)