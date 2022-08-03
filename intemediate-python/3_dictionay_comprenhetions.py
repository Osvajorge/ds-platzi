#Using dictionary comprehentions 
def run():
    #create a dict containing the first 100 natural numbers as a keys, and the square of this numbers as a values.
    #this numbers can't be divided by 3

    # mydict = {i : i**2 for i in range (101) if i%3 != 0}

    mydict = {i: round(i**0.5,2) for i in range(1001)} #dict that contains the first 1000 natural numbers and theirs squares root
    print(mydict)
if __name__ == '__main__':
    run()
