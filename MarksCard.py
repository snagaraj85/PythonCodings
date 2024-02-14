"""
Author: Nagarajan
Desc: Marks Card
Batch: 3.30 - 5.30 PM
Date: 14/02/2024
"""

M1=int(input("Enter English Marks: "))
M2=int(input("Enter Kannada Marks: "))
M3=int(input("Enter Maths Marks: "))
M4=int(input("Enter Science Marks: "))
M5=int(input("Enter Computer Marks: "))
M6=int(input("Enter Social Marks: "))

if (M1 < 0) or (M1>100) or (M2 < 0) or (M2 >100) or (M3 < 0) or (M3>100) or (M4 < 0) or (M4 >100) or (M5 < 0) or (M5>100) or (M6 < 0) or (M6 >100):
    print("Enter the Marks in between 0 and 100")
    exit()
S1=input("Enter Student Name: ")

TotalMarks=M1+M2+M3+M4+M5+M6
TotalAverage=TotalMarks/6
# print(TotalMarks)
# print(TotalAverage)
# print(type(TotalMarks))
# print(type(TotalAverage))
if TotalMarks == 600:
    print(S1," scored ",TotalMarks," with ",TotalAverage," % "," with Distinction")
elif (TotalMarks >= 500) and (TotalMarks >= 550):
    print(S1, " scored ", TotalMarks, " with ", TotalAverage, " % ", " with Distinction")
elif TotalMarks >= 423 and TotalMarks <= 549:
    print(S1, " scored ", TotalMarks, " with ", TotalAverage, " % ", " with First Class")
elif TotalMarks >= 330 and TotalMarks <= 422:
    print(S1, " scored ", TotalMarks, " with ", TotalAverage, " % ", " with Second Class")
else:
    print(S1, " scored ", TotalMarks, " with ", TotalAverage, " % ", " Failed")






