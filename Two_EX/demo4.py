def si():
    for i in range(1, 7):
       for j in range(i):
          print(j+1, end=" ")
       print()

def wu():
    for i in range(6, 0, -1):
       for j in range(i):
          print(j+1, end=" ")
       print()   

print(si())
print(wu())      
