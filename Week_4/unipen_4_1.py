def bmi(suly,magassag):
   temp = magassag / 100
   return suly / (temp*temp)


s = int(input('Kérem a súly értékét       :'))
m = int(input('Kérem a magasság értékét   :'))

index = bmi(s,m)
print('A testtömeg index:{0:.2f}'.format(index))