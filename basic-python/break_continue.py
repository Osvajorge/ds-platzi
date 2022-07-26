def run():
    #Use break to exit a for loop
    print('break in for loop:')
    text = input('write a text: ').lower()
    for character in text:
        if character == 'o':
            break
        print(character)

    #Use continue to skip a certain iteration in a for loop
    print('continue in for loop:')
    text2 = input('write a text: ').lower()
    for character in text:
        if character == 'o':
            continue
        print(character)


    #Use break to exit a while loop
    print('break in while loop:')
    text3 = input('write a text: ').lower()
    i = 0
    while i < len(text3):
        if text3[i] == 'o':
            break
        print(text3[i])
        i += 1

    # Use continue to skip a certain iteration in a while loop
    print('continue in while loop:')
    text4 = input('write a text: ').lower()
    i = 0
    a = 1
    while i < len(text4):
        if text4[i] == 'o':
            i += 1
            continue
        print('Letter' + str(a) + ': ', text4[i])
        i += 1
        a += 1

    print('end of program')


if __name__ == '__main__':
    run()
