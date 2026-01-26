import Arithmatic

def main():
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))
    Result = 0

    Result = Arithmatic.Addition(No1,No2)
    print(f"The addition of the two numbers {No1} and {No2} is {Result}.")

    Result = Arithmatic.Subtraction(No1,No2)
    print(f"The subtraction of the two numbers {No1} and {No2} is {Result}.")

    Result = Arithmatic.Multiplication(No1,No2)
    print(f"The multiplication of the two numbers {No1} and {No2} is {Result}.")

    Result = Arithmatic.Division(No1,No2)
    print(f"The division of the two numbers {No1} and {No2} is {Result}.")    

if __name__ == "__main__":
    main()


# Output:

#C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_16,17,18,19,20 & 21\Assignment_17>python Assignment_17_1.py
'''
Enter First Number : 20
Enter Second Number : 10
The addition of the two numbers 20 and 10 is 30.
The subtraction of the two numbers 20 and 10 is 10.
The multiplication of the two numbers 20 and 10 is 200.
The division of the two numbers 20 and 10 is 2.0.
'''