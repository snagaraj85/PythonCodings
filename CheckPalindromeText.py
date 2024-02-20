# Printing Palindromes in a list
list1=['mom','Raj','madam','Test','malayalam','palindrome','bob']
print(list1)
list2=[]
i=0
#print(temp[::-1])
print("Palindrome Strings")
#while i < len(list1):
for i in range(0,len(list1)):
    temp = list1[i]
    temp2 = temp[::-1]
    if temp == temp2:
        list2.append(temp2)
    #i=i+1
print(list2)
