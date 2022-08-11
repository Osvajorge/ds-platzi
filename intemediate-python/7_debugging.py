#This is a program that tell you the divisors of a number
def division(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

def run ():
    try:
        num = int(input("Enter a number: "))
        if str(num).isalpha() == True: #if the input is not a number
            raise ValueError
        if num < 0: #if the input is a negative number
            raise Exception
        print(division(num))
    except ValueError:
        print("Write a valid number")
    except Exception:
        print("Only positive numbers are valid")
    finally:
        print("The program ended")

if __name__ == '__main__':
    run()
