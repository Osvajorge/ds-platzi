
def run ():
    n = int(input("Enter a number: "))
    if n == 1:
        print('The number is not prime',)
    if n > 1:
        for i in range( 2, n+1):
            if n%i == 0:
                print('The number is not prime')
                break
            else:
                print('The number is prime')
                break
                
   

if __name__ == '__main__':
    run()

        