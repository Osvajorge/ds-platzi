def read():
    numbers = []
    with open('./files/numbers.txt', 'r', encoding="utf-8") as f:
        for line in f:  
            numbers.append(int(line))
    print(numbers)

def write():
    names = ['John', 'Bob', 'Alice', 'Mary', 'Rocío']
    with open('./files/names.txt', 'a', encoding="utf-8") as f:
        for name in names:
            f.write(name + '\n') 



def run ():
    read()
    write()

if __name__ == '__main__':
    run()
