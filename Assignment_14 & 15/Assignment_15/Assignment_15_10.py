# 10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

def main():
    NumList = [1, 2, 3, 4, 5, 6, 7]

    Result = list(filter(lambda Value1 : Value1 % 2 == 0, NumList))

    print(NumList)
    print(Result)
    print(len(Result))

if __name__ == "__main__":
    main()

# Output

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_15>python Assignment_15_10.py
# [1, 2, 3, 4, 5, 6, 7]
# [2, 4, 6]
# 3