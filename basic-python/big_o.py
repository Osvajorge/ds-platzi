bigo = open('bigo_notation.txt') # open file
rd = bigo.read()  # read file
words = rd.lower().split() # split file into words
count = dict() 
#check the words in the list and add how many times they appear into the dictionary
for word in words:
    count[word] = count.get(word,0) + 1

#sort the dictionary by the number of times they appear
sortedcount = sorted(count.items(), key=lambda x: x[1], reverse=True)
    

max_key = ''
max_value = 0
#notwords = ['the','o','a','of'] #list of words that are not considered to be words
max_keys = []
#find the max value in count, if there are multiple max values, add them to a list
for key, value in sortedcount:
    if value > max_value: #and key not in notwords:
        max_value = value
        max_key = key
    if value == max_value: #and key not in notwords:
        max_keys.append(key)
#print(sortedcount)
print('The total number of words is: ' +'\033[91m'+ str(len(words)) +'\033[0m')
if len(max_keys) > 1:
    print('The most common words are: ' + '\033[91m'+str(max_keys)+'\033[0m' + ', with ' + str(max_value) + ' occurrences.')
else:
    print('The most common word is: ' + '\033[91m'+max_key+'\033[0m' + ', with ' + '\033[91m'+str(max_value)+'\033[0m' + ' occurrences.')


# #print the top ten values of sortedcount, if a value is repited print all the repited values in a list
# top_ten = []
# vtoprint = []
# current = 0
# last_value = 0
# plast = 0

# for key, value in sortedcount[:10]:
#     current = value
#     top_ten.append(value)
#     if last_value == current:
#         vtoprint.append(last_value)
#         current = value
#     if plast == last_value == current:
#         vtoprint.append(last_value)
#     plast = last_value
#     last_value = current
    
    
#     print(key, value)
#     print(f' Top ten : {top_ten} Vtoprint: {vtoprint} Current:  {current} last value: {last_value} Plast: {plast}')


 
    
    

