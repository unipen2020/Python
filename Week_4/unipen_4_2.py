def bmi(suly,magassag):
   temp = magassag / 100
   return suly / (temp*temp)


def bmi_text(index):
   if index < 19.5:
      return 'Sovány'
   elif index > 24.5:
      return 'Kövér'
   else:
      return 'Normál'

s = int(input('Kérem a súly értékét       :'))
m = int(input('Kérem a magasság értékét   :'))

index = bmi(s,m)
print('A testtömeg index: {0:.2f}'.format(index))
print('Testalkat        : {0}'.format(bmi_text(index)))