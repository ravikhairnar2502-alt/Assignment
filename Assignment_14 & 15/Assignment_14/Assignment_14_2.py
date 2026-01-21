# 2. Write a lambda function which accepts one number and returns cube of that number.

def main():
    No1 = int(input("Enter Number : "))

    Result = lambda Value1 : Value1 ** 3

    print(Result(No1))

if __name__ == "__main__":
    main()

# Output

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_14>python Assignment_14_2.py
# Enter Number : 5
# 125