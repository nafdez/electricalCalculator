def hexa_chooser(i):
    int_str = isinstance(i, str)
    if int_str == True:
        hexadecimal(i)
    elif int_str == False:
        hexadecimal(i)


def hexadecimal(i):
    global hexanumber
    global cifra
    i = i.upper()
    hexanumber = 0
    pesu = -1
    hexa = '0123456789'
    decimal = 'ABCDEF'
    hexadecim = '0123456789ABCDEF'
    for cifra in i[::-1]:
        pesu = pesu + 1
        pesu_elevau = pow(16, pesu)
        print(cifra + ':', pesu_elevau)
        if cifra in hexa:
            hexa_operation(cifra, pesu_elevau)
        elif cifra in decimal:
            hexadecimal_operation(cifra)
            hexa_operation(cifra, pesu_elevau)
        else:
            print('Sorry, enter an hexadecimal number please.')
            return
    print('The hexadecimal number', i, 'in decimal is', hexanumber)


def hexa_operation(i, w):
    global hexanumber
    i = int(i)
    number = i * w
    hexanumber = hexanumber + number

def hexadecimal_operation(i):
    global cifra
    if i == 'A':
        cifra = 10
    elif i == 'B':
        cifra = 11
    elif i == 'C':
        cifra = 12
    elif i == 'D':
        cifra = 13
    elif i == 'E':
        cifra = 14
    elif i == 'F':
        cifra = 15



hexadecimal(input('What\'s the hexadecimal number? '))