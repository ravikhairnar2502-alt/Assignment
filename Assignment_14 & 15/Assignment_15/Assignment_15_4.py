# 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.
from functools import reduce

def main():
    NumList = [1, 2, 3, 4, 5, 6, 7]

    Result = reduce(lambda a, b : a + b , NumList)

    print(NumList)
    print("Sum of list : ",Result)

if __name__ == "__main__":
    main()

# Output

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_15>python Assignment_15_4.py
# [1, 2, 3, 4, 5, 6, 7]
# Sum of list :  28