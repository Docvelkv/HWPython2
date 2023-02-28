from math import isqrt

from checkingInput import correct_int

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа
# X и Y (X, Y ≤ 1000), а Катя должна их отгадать. Для этого Петя делает
# две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

print("Введите первое число: ", end="")
num1 = correct_int()
print("Введите второе число: ", end="")
num2 = correct_int()

summa = num1 + num2
product = num1 * num2
hid_num1 = int(summa / 2 + isqrt(summa ** 2 - 4 * product) / 2)
hid_num2 = int(summa / 2 - isqrt(summa ** 2 - 4 * product) / 2)
print(f"Первое загаданное число - {hid_num1}({num1}), "
      f"второе загаданное число - {hid_num2}({num2}).")
