def lache():
   for i in range(1, 34):
      for j in range(1, 50):
         k = 100 - i - j
         if i * 3 + j * 2 + k / 2 == 100:
            print("大马%d匹，中马%d匹，小马%d匹" % (i, j, k))
print(lache())
       
