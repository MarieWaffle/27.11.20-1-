a = int(input("Введите радиус круга: "))
b = int(input("Введите сторону квадрата: "))
c = 3.14*a**2
d = b*b
if c > d:
    print("Площадь круга больше")
else:
    print("Площать квадрата больше")