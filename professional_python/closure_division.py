def make_division_of(n):
    def division(x):
        return x / n
    return division

def run():
    division3 = make_division_of(3)
    print(division3(10))


if __name__ == '__main__':
    run()