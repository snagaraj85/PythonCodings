f = open("PythonImage.png", "rb")
data = f.read()
print(type(data))
print(data)
f.close()

f1=open("PythonImg.txt","wb")
data2=f1.write(data)
f1.close()