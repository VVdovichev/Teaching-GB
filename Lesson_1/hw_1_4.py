n = int(input('Введите целое положительное число: '))
m = n % 10
n //= 10
while n > 0:
    if n % 10 > m:
        m = n % 10
    n //= 10
print('Наибольшая цифра в числе: ', m)