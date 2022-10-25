#closure functions
def make_multiplier(x): #we define a function

    def multiplier(n): # And inside we have a nested funct
        return x * n
    return multiplier # inside of the fisrt fucntion we return the second funct

times10 = make_multiplier(10) #Define the values of x
times4 = make_multiplier(4)

print(times10(3)) #define the vaules of n
print(times4(5))
print(times10(times4(2))) 

