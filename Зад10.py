x =int(input('Введите х: '))
y =int(input('Введите у: '))
if x>0 and y>0:
    print('I четверть')
elif x<0 and y>0:
    print('II четверть')
elif x<0 and y<0:
    print('III четверть')
elif x>0 and y<0:
    print('IV четверть')
