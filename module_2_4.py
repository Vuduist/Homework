# Список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Пустые списки для простых и не простых чисел
primes = []
not_primes = []

# Перебор чисел в списке numbers
for number in numbers:
    if number < 2:  # Числа меньше 2 не являются простыми
        continue

    is_prime = True  # Флаг для проверки на простоту
    for divisor in range(2, int(number ** 0.5) + 1):  # Проверяем делители до корня числа
        if number % divisor == 0:
            is_prime = False
            break

    # Распределение числа по спискам
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# Вывод результатов
print("Primes:", primes)
print("Not Primes:", not_primes)
