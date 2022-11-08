Домашняя работа:
a=float(input())
b=float(input())
c=float(input())
D=b**2-4*a*c #Дискриминант
print('Дискриминант',D**0.5)
if D>0:
    print('x1=',((-b+D**0.5)/(2*a)),'x2=',((-b-D**0.5)/(2*a)))
elif D==0:
    print(-b/(2*a))
else:
    print('Нет корней')
