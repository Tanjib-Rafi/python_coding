str = input("Enter the string:: ")

i = 0

while i < len(str):
    if i % 2 == 0 :
        print("The even index characters are: ", str[i])
    else :
        print("The odd index characters are: ", str[i])
    
    i = i+1

#using slice
print("The even index characters are :: ", str[::2])
print("The odd index characters are:: ", str[1::2])