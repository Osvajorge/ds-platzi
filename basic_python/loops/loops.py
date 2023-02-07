#This code raises the number 2 to the power of a counter. 
#The limit of the resulting number is less than one thousand. After that number, it stops raising the number. 

def run():
    LIMIT = 1000

    counter = 0
    pow_2 = 2**counter
    while pow_2 < LIMIT:
        print('2 to the {} is equal to {}'.format(counter, pow_2))
        counter += 1
        pow_2 = 2**counter

if __name__ == '__main__': 
    run()
