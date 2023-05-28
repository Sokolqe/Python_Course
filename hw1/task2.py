# Задача 2: Найдите сумму цифр трехзначного числа.
num = int(input('Введите трехзначное число: '))
result = num % 10
while num // 10 != 0:
    num //= 10
    result += num % 10    
print(f"Сумма цифр числа: {result}")