a = int(input('A='))
b = int(input('B='))
c = int(input('C='))

K = a + b + c 
S = K / 2.0
temp = S*(S-a)*(S-b)*(S-c)
T = pow(temp,0.5)

print('A háromszög kerülete:{0}'.format(K))
print('A háromszög területe:{0:.2}'.format(T))



