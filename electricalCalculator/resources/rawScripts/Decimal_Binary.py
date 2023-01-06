import os


# Aquí realizamos la conversión de binario a decimal
def binary_to_decimal():
    global x
    global decimal
    try:
        number = int(input('\nPlease, enter a binary number: '))
    except:
        print('Sorry an error occurred. Try again.')
        return
    number = str(number)
    x = 1
    decimal = 0
    for cifra in number[::-1]:
        cifra = int(cifra)
        for binary in range(0, 1):
            binary_comprobator(cifra)
    print('\nThe binary number', number, 'in decimal is', decimal)


def binary_comprobator(n):
    global x
    global decimal
    if n == 1:
        decimal = decimal + x
    elif n == 0:
        decimal = decimal
    elif n != 0 or n != 1:
        print('Sorry, you must enter a number in base 2. Please try again.')
        return
    x = x * 2


# A partir de aquí realizamos la conversión de decimal a binario
def decimal_binary():
    try:
        number = int(input('\nPlease, enter a decimal number: '))
    except:
        print('Sorry an error occurred. Try again.')
        return
    number_original = number
    contador = 0
    while number > 1:
        number = number / 2
        number = int(number)
        contador = contador + 1
    return remainder(number, number_original, contador)


def remainder(n_result, n_ori, contador):
    bynary = 0
    first_number = n_ori
    for binario in range(1, contador + 1):
        binary = n_ori % 2
        bynary = str(bynary) + str(binary)
        n_ori = n_ori / 2
        n_ori = int(n_ori)
    return result(n_result, first_number, bynary)


def result(number, first_number, bynary):
    FINAL_binary = bynary + str(number)
    bynary = FINAL_binary[::-1]
    bynary = bynary[:-1]
    print('\nThe decimal number', first_number, 'in binary is', bynary)


# Definimos la estructura del programa
def start_program():
    try:
        op = int(input('Do you want decimal-binary(1) or binary-decimal(2) conversion? '))
    except:
        print('Sorry an error occurred. Try again.')
        return
    if op == 1:
        return decimal_binary()
    elif op == 2:
        return binary_to_decimal()


start_program()
