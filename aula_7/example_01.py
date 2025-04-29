def greetings():
    print('Olá mundo!')


greetings()


def printline():
    print(30*"=")


printline()
print("Título com moldura")
printline()


def sum(x, y):
    s = x + y
    return s

    print(s)


s = sum(4, 5)
print(f'O valor da variável sum é {s}')


for i in range(3):
    number_1 = int(input('Informe o número 1: '))
    number_2 = int(input('Informe o número 2: '))

    sum_numbers = sum(number_1, number_2)
    print(sum_numbers)
