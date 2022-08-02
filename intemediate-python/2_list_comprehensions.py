#push the first 100 square natual numbers into a list
def run():

    ### traditional way ###
    # sqrs = []
    # for i in range (101):
    #     if i%3 != 0:
    #         sqrs.append(i**2)
    # print(sqrs)

    #using list comprenhentions
    sqrs = [i**2 for i in range(101) if i%3 != 0]

    mylist = [i for i in range (100000) if i%4 == 0 and i%6 == 0 and i%9 == 0]

    print(mylist)
if __name__ == '__main__':
    run()

