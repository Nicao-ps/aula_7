WEIGHT_LIMIT = 100.0
TICKET = 4.0


def printline():
    print(89*'*')


def check_weight():
    print('')
    printline()
    weight = float(input('\nInforme o peso da carga: '))
    if weight > 0.0:
        if weight > WEIGHT_LIMIT:
            overweight = weight - WEIGHT_LIMIT
            ticket_value = overweight * TICKET
            print(f'\nPeso da carga: {weight:.2f} kg.')
            print(f'\nCapacidade máxima excedida em {overweight:.2f} kg.')
            print(f'\nValor esperado da multa: R$ {ticket_value:.2f}')
            return check_weight()
        else:
            print(f'\nPeso da carga: {weight:.2f} kg.')
            print('\nCapacidade máxima não excedida.')
            print('\nNão é esperado multa.')
            return check_weight()
    else:
        print('\nErro! O peso da carga não pode apresentar valor negativo!')
        return check_weight()


check_weight()
