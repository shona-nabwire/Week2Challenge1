from datetime import datetime

def yearofbirth():
    currentyear = datetime.now().year
    
    try:
        num = int(input("Please enter the year you were born "))
        num1 = currentyear - num
        
        if num <= 0:
            raise ValueError
        elif num > currentyear:
            raise ValueError
        elif num1 < 18:
            print ("You are a minor")
        elif num1 <= 36 and num1 >= 18:
            print("You are a youth")
        elif num1 > 36:
            print("You are an elder")
    
    except ValueError:
        print("Invalid input")


yearofbirth()