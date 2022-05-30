a = int(input('Kérem a sorozat elő elemét:'))
d = int(input('Kérem a sorozat diferenciáját:'))

for n in range(2,10):
   an = a + (n-1)*d
   print('A(z) sorozat {0}. eleme: {1}'.format(n,an))
