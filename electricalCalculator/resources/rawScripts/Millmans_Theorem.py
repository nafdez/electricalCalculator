def millman():
    try:
        n_c = int(input('How many generators do you have? '))
        if n_c <= 1:
            print('Sorry, Millman\'s Theorem is only for parallel generators.')
            return
    except:
        print('Please, can you enter an integer number?')
        return millman()
    try:
        Ei = float(input('What\'s the first voltage?\n'))
        ri = float(input('And what\'s the resistance?\n'))
        Ei_ri = Ei/ri
        one_ri = 1/ri
        Mill = Ei_ri/one_ri
        for Millman in range(1, n_c):
            Ei2 = float(input('What\'s the next voltage?\n'))
            ri2 = float(input('And what\'s the resistance?\n'))
            Ei_ri2 = Ei2 / ri2
            one_ri2 = 1 / ri2
            Ei_ri = Ei_ri + Ei_ri2
            one_ri = one_ri + one_ri2
        Mill = Ei_ri / one_ri
    except:
        print('Sorry, I only accept numeric characters')
        return millman()
    print(Mill)
    return

millman()