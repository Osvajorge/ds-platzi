import time

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1: 
            counter += 1
            yield n2
        else: 
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux

if __name__ == '__main__':
    max = int(input('Max: '))
    fibonacci = fibo_gen()
    for element in fibonacci:
        if element > max:
            break
        print(element)
        time.sleep(.1)

