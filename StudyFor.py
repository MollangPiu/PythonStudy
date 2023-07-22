# list 변수 생성
list = ['apple','banana', 'cocoa', 'orange', 'dalgona', 'cleanse']
print(list)

# for문 range만으로 만들기
for index in range(6):
    print(list[index])

print('===========================')

# for문 2 (java의 foreach문)
for index in list:
    print(index)

# for문 사용(start(초기값), end(종료값), step(증감값))
# 하나만 입력할 경우, 대표적으로 end만 출력 된다.
for index in range(0, 6, 1):
    print(index)

# 10부터 6까지 1증가이다.
# 애는 false 관계이므로, 실행되더라도 바로 종료된다.
for index in range(10, 6):
    print(index)

# 감소로 -2씩 만들수도 있다.
for index in range(15, 10, -2):
    print(index)