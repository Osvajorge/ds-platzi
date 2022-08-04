# This program is created to se how the high order functions work 
from functools import reduce 

def run():
    #filter
    mylist = [1,2,3,4,5,6,7,8,9,10]
    odd = list(filter(lambda x: x%2 !=0, mylist)) #this filter function takes a lambda function of odd number that is passed through a list
    print(f"Filter function --> {odd}") 

    #map
    mylist1 = [1,2,3,4,5]
    squares = list(map(lambda x: x**2, mylist1)) #this map function takes a lambda fuction of sqr X that is passed through a list
    print(f"Map function --> {squares}")   

    #reduce
    mylist2 = [2,2,2,2,2]
    powed_list = reduce(lambda a,b: a*b, mylist2) #this reduce fucntion takes a lambda fuction that multiplies the fist variable with
                                                  # a second one, and is passed through a list
    print(f"Map function --> {powed_list}")   

if __name__ == '__main__':
    run()
