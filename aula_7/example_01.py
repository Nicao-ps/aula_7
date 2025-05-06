def greetings():
    print('Olá mundo!')


greetings()


def printline():
    print(30*"=")


printline()
print("Título com moldura")
printline()


def sum_x(x, y):
    suum = x + y
    print(int(suum))
    return suum


s = sum_x(4, 5)
print(f'O valor da variável sum é {s}')


for i in range(3):
    number1 = int(input('Informe o número 1: '))
    number2 = int(input('Informe o número 2: '))

    sum_numbers = sum(number1, number2)
    print(sum_numbers)
