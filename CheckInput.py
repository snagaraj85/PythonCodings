"""
Author: Nagarajan
Desc: Number to Words
Batch: 3.30 - 5.30 PM
Date: 14/02/2024
"""


inp = input("enter a input value: ")
if inp.isdigit():
    print("input is integer value")
elif '-' in inp:
    print("input is negative")
elif '.' in inp:
    print("input is float value")
else:
    print("input is a string")
