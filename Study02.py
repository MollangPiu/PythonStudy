list = [1, 2, 3, 4]
print(type(list))
print(list)
print(list[0])

#list 추가하기
list.append(5)
list.append(6)
list[0] = 10
list.insert(1, 70)
print(list)
list.remove(10) #값을 찾아서 지운다.
print(list)

listSec = ['a','b','3',"4"]
print(listSec)
listThr = [1,2,3,4]
listThr.append('insert')
print(listThr)

listWkwmd = ['a','b',[1,2,['a','b','c']]]
print(listWkwmd[2][2][2])

print('=======================')

tuple = (3, 4, 5, 6)
print(type(tuple))
print(tuple)

print('==============================')
dict = {
    'a':'apple',
    'b':'banana',
    'c':'cocoa',
    'd':'dango'
}
print(type(dict))
print(dict)
dict['d'] = 'doroma'
print(dict)
dict['ab'] = 'abb'
print(dict)
del dict['ab']
print(dict)
dict.pop('d')
print(dict)

dict2 = {'a': 'test'}
print(dict2)
dict2['1'] = 'one'
print(dict2)
dict2[1] = 'Int'
print(dict2)