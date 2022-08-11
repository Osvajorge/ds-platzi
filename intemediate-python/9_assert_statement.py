#a progam that tell you the divisors of a number
def division(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

def run ():
    num = input("write a number: ")
    assert num.isnumeric() and int(num) < 0, "Write a valid number"
    print(division(int(num)))

if __name__ == '__main__':
    run()

