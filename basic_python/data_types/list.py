counts = dict()
names = ['A','B','C','D','D','E','E','E',]
for name in names:
	if name not in counts:	
		counts[name] = 1
	else: 
		counts[name] +=1
print(counts)


print('--------------------------------------------------------------------------------------------------------------------')
counts = dict()
names = ['A','B','C','D','D','E','E','E',]
for name in names:
	counts[name] = counts.get(name,0) + 1
print(counts)

print('--------------------------------------------------------------------------------------------------------------------')
print(counts.get('H',0), counts.get('H',1))
