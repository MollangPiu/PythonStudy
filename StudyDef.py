def fn():
    print('fn 실행')

def fn1(str):
    print(str)

def returnTest():
    return "return"


fn()
fn1('test')
print(returnTest())

x=1
a = (lambda x,y: x + y)(x, 20)
print(a)

la = (lambda y: x + y)(50)
print(la)
print(la)


fa = (lambda: x+100)()
print(fa)


def lamBu(str):
    print(f'str: {str}')


lamBu('test1')


#람다를 먼저 선언후, 밑에 변수를 선언 할 경우
pa = (lambda: ta+100)()
print(pa)

ta = 1000