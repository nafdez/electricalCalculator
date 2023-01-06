def parallel_series():
    option = int(input('Do you wanna calculate a series(1) or a parallel(2) circuit?'))
    if option == 1:
        print('Your choice is:', 'series')
        return ch_v_c_series()
    elif option == 2:
        print('Your choice is:', 'parallel')
        return ch_v_c_parallel()

def ch_v_c_series():
    option = int(input('Okay, and do you want to calculate total voltage(1) or the capacitance(2)?'))
    if option == 1:
        print('Your choice is:', 'total voltage')
        return volt
    elif option == 2:
        print('Your choice is:', 'capacitance')
        return capacit





def ch_v_c_parallel():
    option = int(input('Okay, and do you want to calculate total charge(1) or the capacitance(2)?'))
    return


def capacitance_series():
    n_c = int(input('How many capacitors do you have? '))
    C1 = float(input('What\'s the capacitance of the first capacitor?\n'))
    C1x = 1 / C1
    for capacitor in range(1, n_c):
        Cx = float(input('And what\'s the capacitance of the next capacitor?\n'))
        C1x = C1x + (1 / Cx)
    Ct = 1 / C1x
    print('The total capacitance is', str(Ct))

capacitance_series()