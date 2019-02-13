num1 = 2001
num2 = 1983


num = input("Please enter the year you were born ")

if int(num) >= num1:
    print ("You are a minor")
elif int(num) <= num1 and int(num) >= num2:
    print("You are a youth")
elif int(num) <= num2:
    print("You are an elder")