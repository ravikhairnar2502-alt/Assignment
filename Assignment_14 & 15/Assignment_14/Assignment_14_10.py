# 10. Write a lambda function which accepts three numbers and returns largest number.

def main():
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))
    No3 = int(input("Enter Third Number : "))

    Result = lambda Value1, Value2, Value3: max(Value1, Value2, Value3)

    print(Result(No1,No2,No3))

if __name__ == "__main__":
    main()

# Output

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_14>python Assignment_14_10.py
# Enter First Number : 10
# Enter Second Number : 52
# Enter Third Number : 23
# 52