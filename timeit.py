import os
from timeit import timeit
with open("newfile.txt", "a") as f:
    for i in range(200000000000):
        if os.path.getsize("newfile.txt")>=1024 * 1024 * 50:
            break
        f.write(str(i)+"\n")   
t= """
with open("newfile.txt") as f:
    s=0
    line=f.readlines()
    for i in line:
        if i.strip().isdigit():
            s+=int(i.strip())
"""
print(timeit(t,number=10)/10) 

t= """
with open("newfile.txt") as f:
    s=0
    for line in f:
        if line.strip().isdigit():
            s+=int(line.strip())
"""
print(timeit(t,number=10)/10) 

t="""
with open("newfile.txt") as f:
    s=sum((int(i.strip()) for i in f if i.strip().isdigit()))
"""
print(timeit(t,number=10)/10)