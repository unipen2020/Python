a = int(input('A='))
b = int(input('B='))
c = int(input('C='))

D = b * b - 4 * a * c
if D > 0:
   print('Két megoldás van!')
   x_1 = (-b + pow(D,0.5)) / (2*a)
   x_2 = (-b - pow(D,0.5)) / (2*a)
   print('x1={0:.1f} x2={1:.1f}'.format(x_1,x_2))
elif D == 0:
   print('Egy megoldás van!')
   x_1 = -b / (2 * a) 
   print('x1=x2={0:.2f}'.format(x_1))
else:
   print('Nincs megoldás!')

