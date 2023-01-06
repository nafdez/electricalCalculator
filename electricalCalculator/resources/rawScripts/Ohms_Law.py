# Aquí ejecutamos la calculadora de ley de Ohm
def ley_ohm():
    try:
        op = int(input('Do you want to calculate the voltage(1), the resistance(2), or the current(3)?: '))
    except:
        print('Please, I haven\'t understood you')
        return ley_ohm()
    if op == 1:
        print('Your choice: Voltage\n')
        return voltage_ohm()
    elif op == 2:
        print('Your choice: Resistance\n')
        return resistance_ohm()
    elif op == 3:
        print('Your choice: Current\n')
        return current_ohm()
    else:
        print('I\'m sorry, that option isn\'t ready yet')
        return ley_ohm()

def voltage_ohm():
    R, I = float(input('What is the resistance value?:\n')), float(input('And the current value?\n'))
    V = R * I
    print('The voltage are', str(V) + 'V')
    return

def resistance_ohm():
    V, I = float(input('What is the voltage value?:\n')), float(input('And the current value?\n'))
    R = V / I
    print('The resistance are', str(R) + 'Ω')
    return

def current_ohm():
    V, R = float(input('What is the voltage value?:\n')), float(input('And the resistance value?\n'))
    I = V / R
    print('The current are', str(I) + 'A')
    return

ley_ohm()