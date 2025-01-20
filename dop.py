import random

number_1 = random.randrange(3, 20)
number_2 = ''
result = []


def password(number_1):
    for i in range(1, number_1):
        for j in range(2, number_1):
            if i >= j:
                continue

            if number_1 % (i + j) == 0:
                result.append(i)
                result.append(j)
    return result


result = password(number_1)
print(
    f"Числа на ввод для 1-й вставки {number_1} - {number_2} \n Вид введенного числа: {number_2.join(map(str, result))}")
