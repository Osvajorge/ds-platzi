def ispalindrome(word: str):
    word = word.replace(" ","").lower()
    return word == word[::-1]
         

def run():
    print(ispalindrome(1000)) #this error is intended to check run the program with this command:mypy palindrome.py --check-untyped-defs

if __name__=='__main__':
    run()