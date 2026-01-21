# 9. Write a lambda function which accepts two numbers and returns multiplication.

def main():
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    Result = lambda Value1, Value2 : Value1 * Value2

    print(Result(No1,No2))

if __name__ == "__main__":
    main()

# Output

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_14>python Assignment_14_9.py
# Enter First Number : 10
# Enter Second Number : 2
# 20