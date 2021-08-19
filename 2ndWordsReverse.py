str = input("Enter the words:: ")

splitWords = str.split() #spliting the words

emptyList = [] #taking an empty list for storing the words

i = 0
while i <len(splitWords):

    if i%2 == 0:
        emptyList.append(splitWords[i])
    else:
        emptyList.append(splitWords[i][::-1])  #reversing the 2nd index values 
    
    i=i+1

Output = ' '.join(emptyList)  #joining the words with an space between

print("The output is:: " ,Output)