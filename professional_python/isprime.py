def isprime(number: int):
    
    if number == 0 or number == 1:
        return False
    elif number % 2 == 0:
        return False
    else: 
        return True
    
def run():
    number = input("write a number: ")
    print(isprime(number))

if __name__=='__main__':
    run()