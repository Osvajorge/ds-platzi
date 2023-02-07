# print numbers from 1 to 100 using a for cicle and push them into a list
print('for cicle:')
for_list = []
for i in list(range(101)):
    for_list.append(i)
print(for_list)

#print numbers from 1 to 100 using a while cicle and push them into a list
print('while cicle:')
while_list = []
i = 1
while i < 101:
    while_list.append(i)
    i += 1
print(while_list)


#print numbers from 1 to 100 without using loops
print('without loops:')
a = list(range(101))
print(a)

