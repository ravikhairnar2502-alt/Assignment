# 5. Write a lambda function which accepts one number and returns True if number is even otherwise False.

def main():
    No1 = int(input("Enter Number : "))

    Result = lambda Value1 : Value1%2 != 0

    print(Result(No1))

if __name__ == "__main__":
    main()

# Output

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_14>python Assignment_14_6.py
# Enter Number : 4
# False

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_14>python Assignment_14_6.py
# Enter Number : 5
# True