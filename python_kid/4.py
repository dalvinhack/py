x=int(input('Скорость лодки:'))
y=int(input('На сколько процентов катер движется быстрее лодки:'))
z=int(input('Время:'))
print('Скорость катера = ', int(y*x/100+x))
print('Катер пройдет за',z,('часа(ов) на'),int((y*x/100+x)*z-x*z),('км больше лодки'))
