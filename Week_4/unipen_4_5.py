def lnko(a,b):
   if a == b:
      return a
   if a > b:
      return lnko(a-b,b)
   else: 
      return lnko(b-a,a)

def lkkt(a,b):
   return (a*b) // (lnko(a,b))

a = int(input('A='))
b = int(input('B='))

print('A {0} és {1} legnagyobb közös osztója    :{2}'.format(a,b,lnko(a,b)))
print('A {0} és {1} legkisebb közös töbszöröse  :{2}'.format(a,b,lkkt(a,b)))

