# code of tic tac toe game
def board():
    for i in range(0,3):
        print('|', end='')
        for j in range(0,3):
            print(' ', end='')
    print('\t')
    for i in range(0,3):
        print('_', end='')
        for j in range(0,3):
            print('_', end='')
                        
            

board()
    