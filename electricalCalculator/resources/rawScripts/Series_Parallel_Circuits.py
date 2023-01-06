# Aquí determinaremos las funciones para la asociación de circuitos, primero las resistencias, después la intensidad, y
# por último la tensión
def resistance_p_s():
    try:
        p_s = int(input('Do you want calculate the resistance in series(1) or in parallel?(2): '))
    except:
        print('Sorry, can you repeat again please?')
        return resistance_p_s()
    if p_s == 1:
        return series_r()
    elif p_s == 2:
        return parallel_r()
    else:
        print('I\'m sorry, that option isn\'t ready yet')
        return resistance_p_s()

def series_r():
    n_r = int(input('How many resistors do you want to calculate?: '))
    RT = float(input('What\'s the value of the first resistance?:\n'))
    print('Okey, let\'s continue with the rest of the resistors\n')
    for RChoosen in range(1, n_r):
        Rx = float(input('Value of the next resistance:\n'))
        RT = RT + Rx
    print('La resistencia total es de:', str(RT) + 'Ω')
    return

def parallel_r():
    RT = 0
    n_r = int(input('How many resistors do you want to calculate? '))
    Rx = float(input('What\'s the value of the first resistance?:\n'))
    RT = RT + (1 / Rx)
    print('Okey, let\'s continue with the rest of the resistors\n')
    for RChoosen in range(1, n_r):
        Rx = float(input('Value of the next resistance:\n'))
        RT = RT + (1/Rx)
        Req = 1/RT
    Req = Req
    print('The equivalent resistance is', str(Req) + 'Ω')
    return

# La intensidad
def current_p():
    n_c = int(input('How many currents you need to calculate? '))
    I = float(input('What\'s the first current?\n'))
    print('Okey, let\'s continue with the rest of the currents\n')
    for CChoseen in range(1, n_c):
        Ix = float(input('Value of the next current?:\n'))
        I = I + Ix
    print('The total current is:', str(I) + 'A')
    return

# La tensión
def voltage_s():
    n_c = int(input('How many sources of tension do you have? '))
    V = float(input('What\'s the voltage of the first power source?\n'))
    print('Okay, let\' continue with the rest of the voltages values\n')
    for CChoseen in range(1, n_c):
        Vx = float(input('Value of the next voltage:\n'))
        V = V + Vx
    print('The total voltage is', str(V) + 'V')
    return
# Pero primero, hagamos escoger al ususario qué quiere hacer
def c_r_or_v():
    try:
        choice = int(input('Do you want to use the resistance(1), current(2) or voltage(3) calculator?\n'))
    except:
        print('Hmmm... Can you repeat please?')
        return c_r_or_v()
    if choice == 1:
        return resistance_p_s()
    elif choice == 2:
        return current_p()
    elif choice == 3:
        return voltage_s()
    else:
        print('I\'m sorry, that option isn\'t ready yet')
        return c_r_or_v()

c_r_or_v()