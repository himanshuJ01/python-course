f=open("test.txt","r")
print(f.read())
print(f.readline())
f.close()

f=open("test.txt","a") #can be use "w" to rewrite entire file
f.write("A new line now")
f.close()

f=open("test1.txt","x") # new file created

import os
if os.path.exists("test.txt"):
    os.remove("text.text")
else:
    print("File not found")    