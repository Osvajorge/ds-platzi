def run():
    #Normal list and dicts
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"fistname": "Jorge", "lastname": "Guardado"}

    #This is a list containing dicts
    super_list = [
        {"firstname": "Jorge", "lastname": "Guardado"},
        {"firstname": "John", "lastname": "Doe"},
        {"firstname": "Juan", "lastname": "Pérez"}
    ]

    #This is a dict containing lists
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "interger_nums": [-2,-1,0,1,2],
        "floating_nums": [1.1,2.2,3.3]
    }

    #print key,values of the superdict
    for key, value in super_dict.items():
        print(key, " - ", value )
    
    #print key,values of the superlist (first loop is to access to the dict index, 
    #and second is to access to the key values of the dict: i.items() is the variable of each item inside the dict )
    for i in super_list:
        for key, value in i.items():
            print(key, ":",value,)
        #print(i["firstname"], "-", i["lastname"]) Without nesting
if __name__ == '__main__':
    run()
