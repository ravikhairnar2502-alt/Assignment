# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

def main():
    NumList = [2, 3, 4, 5, 6, 7]

    Result = list(map(lambda Value1 : Value1 ** 2, NumList))

    print(NumList)
    print(Result)

if __name__ == "__main__":
    main()

# Output

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_15>python Assignment_15_1.py
# [2, 3, 4, 5, 6, 7]
# [4, 9, 16, 25, 36, 49]