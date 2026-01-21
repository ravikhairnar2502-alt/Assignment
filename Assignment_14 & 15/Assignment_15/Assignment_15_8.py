# 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

def main():
    Numbers = [i for i in range(1,16)]

    Result1 = list(filter(lambda num: num%3 == 0, Numbers))
    Result2 = list(filter(lambda num: num%5 == 0, Numbers))

    print(Numbers)
    print("Divisible by 3 :",Result1)
    print("Divisible by 5 :",Result2)

if __name__ == "__main__":
    main()

# Output

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_15>python Assignment_15_8.py
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Divisible by 3 : [3, 6, 9, 12, 15]
# Divisible by 5 : [5, 10, 15]