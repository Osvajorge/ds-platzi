def my_gen():
    """An example of generators"""

    print('Helo World!')
    n=0
    yield n

    print('Hello heaven')
    n=1
    yield n

    print('Hello hell!')
    n=2
    yield n

iteration = my_gen()
print(next(iteration)) # Helo World!
print(next(iteration)) # Hello heaven
print(next(iteration)) # Hello hell!
print(next(iteration)) #StopIteration
