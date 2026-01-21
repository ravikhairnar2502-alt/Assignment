# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

def main():
    No1 = int(input("Enter Number : "))

    Result = lambda Value1 : Value1%5 == 0

    print(Result(No1))

if __name__ == "__main__":
    main()

# Output

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_14>python Assignment_14_7.py
# Enter Number : 15
# True

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_14>python Assignment_14_7.py
# Enter Number : 2
# False
