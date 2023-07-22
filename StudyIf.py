num = 15
num2 = 100
num3 = 77
str = 'tom n toms'
coffe = 'coffe'
strC = 'tom n toms'

if num < 10:
    print('true 입니다.')
elif num < 20:
    print('elif 입니다.')
else:
    print('false 입니다.')

if True:
    print('강제 실행인가')
else:
    print('너는 실행되니')
    
if 10 < num and 90 < num2:
    print('and 조건')

if num3 < 40 or 80 < num2:
    print('or 입니다.')

if str == strC:
    print('참일까')
else:
    print('거짓일까')
