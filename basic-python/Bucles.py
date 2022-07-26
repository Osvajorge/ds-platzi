def run():
    LIMIT = 1000

    counter = 0
    pow_2 = 2**counter
    while pow_2 < LIMIT:
        print('2 elevado a {} es igual a {}'.format(counter, pow_2))
        counter += 1
        pow_2 = 2**counter

if __name__ == '__main__': 
    run()
