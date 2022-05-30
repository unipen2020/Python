def szamjegyek_osszege(n):
   sum = 0
   while n > 0:
      sum = sum + n % 10
      n = n // 10
   return sum
 

n = int(input('Kérek egy egész számot:'))
print('A {0} szám számjegyeinek összege:{1}'.format(n,szamjegyek_osszege(n)))
