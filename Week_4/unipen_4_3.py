def convert_bin(n):
   if n == 0:
      return '0'
   else:
      txt = ''
      while n > 0:
         m = n % 2
         txt = str(m) + txt
         n = n  // 2
      return txt

x = int(input('Kérek egy egész számot:'))
print(convert_bin(x))
