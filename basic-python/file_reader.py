# This code reads the content of a file (in this case bigo_notation.txt) 
# and tells the total number of words and the most common words in it.

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



 
    
    

