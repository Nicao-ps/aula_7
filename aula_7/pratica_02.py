def calc_all():
    x = int(input('Quantidade solicitada em unidades ofertas promocionais: '))
    y = int(input('Quantidade solicitada em unidades grandes eventos: '))
    z = float(input('Área total de cada adesivo em cm²: '))
    a = x * 2
    b = y * 3
    c = z ** 2
    print(f'Quantidade a ser ofertada para ofertas promocionais: {a} unidades')
    print(f'Quantidade a ser ofertada para grandes eventos: {b} unidades')
    print(f'Área total do adesivo: {c:.2f} cm²')


calc_all()
