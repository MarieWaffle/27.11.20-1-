a = int(input())
b = a//10
c = a%10
d = b+c
if d//3:
    print('a кратно трем')
    if d//a:
        print('Сумма чисел а кратна а')
    else:
        print('Сумма чисел а не кратна а')
else:
    print('Сумма не кратна трем')
    if d//a:
        print('Сумма чисел а равна а')
    else:
        print('Сумма чисел а не кратна а')