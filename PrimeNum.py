inp = int(input("Enter the number to check if it is prime: "))
pn=False
if inp == 0 or inp ==1:
    print("Invalid Digit, value should be above or equal to 2: ")
elif inp > 1:
    for i in range(2,inp):
        if (inp % i == 0):
            print(inp%i)
            pn=True
            break
    if pn:
        print(inp," is not prime number")
    else:
        print(inp," a prime number")

