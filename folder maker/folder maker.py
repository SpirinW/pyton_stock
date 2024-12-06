from os import *
print('1) n папок\n2)[a:b]')
print('Введите вариант')
step = int(input())
if step == 1:
    n=int(input('Сколько папок создать? '))
    a=int(input('С какого номера начать? '))
    for i in range(n+1):
        try:
            mkdir(str(a+i))
        except:
            print(f'Folder {a+i} already exists')
elif step == 2:
    for i in range(int(input('a: ')), int(input('b: '))+1):
        try:
            mkdir(str(i))
        except:
            print(f'Folder {i} already exists')
print('Done')
a=input()
