st1=input("Enter the first string: ")
st2=input("Enter the second string: ")
st3=[]
st4=[]

for i in range(0,len(st1)):
    st3.append(st1[i])
for j in range(0,len(st2)):
    st4.append(st2[j])

st3.sort()
st4.sort()
if st3 == st4:
    print("Entered strings were Anagrams")
else:
    print("Not Anagram Strings")