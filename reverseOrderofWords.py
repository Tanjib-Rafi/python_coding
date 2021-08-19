words = input("Enter the words of string:: ")

splitTheWords = words.split() #firstly spliting those words in list

NowReverseThoseWords = splitTheWords[::-1] #slicing the words in reverse order

NowJoinThoseReversedWords = ' '.join(NowReverseThoseWords) #joining those reversed words with a space between 

print("Reverse Order Of Words are :: " , NowJoinThoseReversedWords)