str1 = input("Enter the first string:: ")
str2 = input("Enter the second string:: ")

output = ''

i,j = 0,0
while i < len(str1)  and j < len(str2):
    output  = output + str1[i] + str2[j]
    i = i + 1
    j = j + 1

print("The merge string is :: " , output)