# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.

# TODO: your code here

a = int(input("Первая сторона: "))
b = int(input("Вторая сторона: "))
c = int(input("Третья сторона: "))

if a==b or a==b==c or a==c or b==c:
    print("YES")
else:
    print("NO")
