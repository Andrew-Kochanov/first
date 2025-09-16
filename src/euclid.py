def gcd(a, b):
    x_1 = 1
    y_1 = 0
    x_2 = 0        ##коэфиценты для a и b
    y_2 = 1
    while b != 0:
        x_1, x_2 = x_2, x_1 - (a // b) * x_2
        y_1, y_2 = y_2, y_1 - (a // b) * y_2
        a, b = b, a % b

    return [a, x_1, y_1]            ##выводит список: нод, коэф а, коэф b


number_f = int(input('Введите первое число: '))
number_s = int(input('Введите второе число: '))
answer = gcd(number_f, number_s)
print(f'{number_f} * {answer[1]} + {number_s} * {answer[2]} = {answer[0]}')
