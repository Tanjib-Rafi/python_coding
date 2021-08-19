str = input("Enter Your String:: ")

#1st way
reverseOutput = str[::-1]  #slicing string from right to left 

#2nd way
reversedString = reversed(str)  #reverse string using reverse method
reverseUsingReversed = ''.join(reversedString) #joining char with empty string

#3rd way
reverseWithWhile = ''  #an empty variable for storing the char

i = len(str) - 1 #starting loop from right to left
while(i >= 0 ):
    reverseWithWhile = reverseWithWhile + str[i]
    i = i-1


print("Reverse String is:: " , reverseOutput) #printing 1st way 
print("Reverse String is:: " , reverseUsingReversed) #printing 2nd way
print("Reverse String is:: ", reverseWithWhile) #printing 3rd way