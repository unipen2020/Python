x = int(input('Kérek egy egész számot:'))

db = 0
for i in range(1,x):
   if x % i == 0:
      db = db + i

if db == x:
   print('{0} egy tökélets szám!'.format(x))
else:
   print('{0} nem tökéletes szám!'.format(x))