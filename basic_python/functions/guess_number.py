import random

def run (): 
    r = random.randint(1, 100)
    n = int(input("Enter a number between 1 and 100: "))
    while n != r:
      print(r)
      if n > 100 or n < 1:
        n = int(input("Invalid number! Enter a number between 1 and 100: "))
      elif n > r:
        n = int(input("Too high! Enter a number between 1 and 100: "))
      elif n < r:
        n = int(input("Too low! Enter a number between 1 and 100: "))
      if n == r:
        print("Congrats, You win!")
        break
            
        
if __name__ == '__main__':
    run()
    
    
    
    