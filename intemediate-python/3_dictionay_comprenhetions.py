#create a dict containing the first 100 natural numbers as a keys, and the square of this numbers as a values.
#this numbers can't be dividet by 3
def run():
    mydict = {i : i**2 for i in range (101) if i%3 != 0}
    print(mydict)

if __name__ == '__main__':
    run()
