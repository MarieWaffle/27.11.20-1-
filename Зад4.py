n = int(input("Введите n: "))
a = int(input("Введите a: "))
if n//a:
    print('a является делителем n')
elif n//a==1:
    print('a равно n')
else:
    print('a не является делителем n')