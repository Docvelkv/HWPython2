import checkingInput

# Требуется вывести все целые степени двойки (т.е. числа вида 2**k),
# не превосходящие числа N.

print("Введите число: ", end="")
num = checkingInput.correct_int()
num_degree = 0
while 2 ** num_degree <= num:
    print(2 ** num_degree, end=" ")
    num_degree += 1
