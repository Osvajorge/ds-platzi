def palindrome(word):
    try:
        if len(word) == 0:
            raise TypeError("Empy strings are not valid")
        if word.isnumeric() == True:
            raise ValueError("Numbers are not valid")
        else:
            return word == word[::-1]
    except TypeError as e:
         print(e)
    except ValueError as ve:
        print(ve)

        

def run():
    i = input("Enter a word: ")
    res = palindrome(i)
    if res == True:
        print("It's palindrome")
    if res == False:
        print("It's not palindrome")
    else:
        pass
if __name__ == '__main__':
    run()
