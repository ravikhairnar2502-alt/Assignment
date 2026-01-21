# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

def main():
    Numbers = [i for i in range(1,5)]

    Result = reduce(lambda a,b : a * b, Numbers)

    print(Numbers)
    print(Result)

if __name__ == "__main__":
    main()

# Output

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_15>python Assignment_15_9.py
# [1, 2, 3, 4]
# 24