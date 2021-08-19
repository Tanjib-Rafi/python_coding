Words = input("Enter the words of the string :: ")

splitWords = Words.split()

storeReverseWords = []

for word in splitWords:
    storeReverseWords.append(word[::-1])

    reverseWord = ' '.join(storeReverseWords)

print("Reversed Internal Words::" , reverseWord)

