# [1,1,2,2,4] -> [1,2,4]

def remove_duplicates(some_list):
    #without_duplicates = []
    #for element in some_list:
    #    if element not in without_duplicates:
    #        without_duplicates.append(element)
    #return without_duplicates
    return list(set(some_list))

if __name__ == '__main__':
    l = [1,1,2,2,4]
    print(remove_duplicates(l))
