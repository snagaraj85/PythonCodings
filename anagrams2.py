
st2=['lemon','nice','dates']
st1=input("Enter the first string: ")
print(st2)
st3=[]
st4=[]
st5=[]
st6=[]
s1=st2[0]
s2=st2[1]
s3=st2[2]

for i in range(0,len(st1)):
    st6.append(st1[i])

for i in range(0,len(s1)):
    st3.append(s1[i])
    #print(st3)
for j in range(0,len(s2)):
    st4.append(s2[j])
    #print(st4)
for k in range(0,len(s3)):
    st5.append(s3[k])
    #print(st5)
st3.sort()
st4.sort()
st5.sort()

st6.sort()

if (st6 == st3) or (st6 == st4) or (st6 == st5):
    print("Entered strings were Anagrams")
else:
    print("Not Anagram Strings")



