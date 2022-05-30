def fibonacci(n):
   if n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      return fibonacci(n-1)+fibonacci(n-2)


n = int(input('Kérek egy egész számot:'))
print('A fibonacci sorozat {0}. tagja:{1}'.format(n,fibonacci(n)))

for i in range(0,11):
   print('A fibonacci sorozat {0}. tagja:{1}'.format(i,fibonacci(i)))