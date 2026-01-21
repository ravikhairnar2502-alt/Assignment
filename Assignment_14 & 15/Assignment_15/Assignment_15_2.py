# 2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

def main():
    NumList = [1, 2, 3, 4, 5, 6, 7]

    Result = list(filter(lambda Value1 : Value1 % 2 == 0, NumList))

    print(NumList)
    print(Result)

if __name__ == "__main__":
    main()

# Output

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_15>python Assignment_15_2.py
# [1, 2, 3, 4, 5, 6, 7]
# [2, 4, 6]