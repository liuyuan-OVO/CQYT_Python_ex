def jiechen(n):
    if n == 0:
      return 1
    else:
      return n *jiechen(n-1)
sum = 0
for i in range(1, 6):
    sum +=jiechen(i)
print(sum)   
