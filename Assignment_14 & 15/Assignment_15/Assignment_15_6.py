# 6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce

def main():
    NumList = [1, 2, 3, 4, 5, 6, 7]

    Result = reduce(lambda a, b: min(a,b), NumList)

    print(NumList)
    print(Result)

if __name__ == "__main__":
    main()

# Output

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_15>python Assignment_15_6.py
# [1, 2, 3, 4, 5, 6, 7]
# 1