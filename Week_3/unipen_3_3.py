x = int(input('Kérek egy pozitív egész számot:'))

db = 0
for i in range(2,x):
   if x % i == 0:
      db = db + 1

if db > 0:
   print('{0} nem prímszám!'.format(x))
else:
   print('{0} prímszám'.format(x))