from random import randint

from checkingInput import correct_int

# На столе лежат n монеток. Некоторые из них лежат вверх решкой(реверс),
# а некоторые – орлом(аверс). Определите минимальное число монеток, которые
# нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно перевернуть.

print("Введите количество монет: ", end='')
num_coins = correct_int()
list_coins = []
cnt_avers = 0
for i in range(num_coins):
    list_coins.append(randint(0, 1))
    if list_coins[i] == 1:
        cnt_avers += 1
print(*list_coins, f"\nЛежат орлом вверх {cnt_avers}")
cnt_revers = num_coins - cnt_avers
if cnt_avers >= cnt_revers:
    print(f"Нужно перевернуть {cnt_revers} монет(ы) орлом вверх")
else:
    print(f"Нужно перевернуть {cnt_avers} монет(ы) решкой вверх")
