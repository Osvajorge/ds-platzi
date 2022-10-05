def isprime(number: int):
    
    if number == 0 or number == 1:
        return False
    elif number % 2 == 0:
        return False
    else: 
        return True
    
def run():
    number = input("write a number: ") #this error is intended to check run the program with this command:mypy isprime.py --check-untyped-defs
    print(isprime(number))

if __name__=='__main__':
    run()