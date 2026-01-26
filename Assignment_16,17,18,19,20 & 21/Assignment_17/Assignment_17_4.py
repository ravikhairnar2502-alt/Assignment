def main():
    No = int(input("Enter Number :"))
    factors = []
    sum = 0

    for i in range(1,No):
        if No % i == 0:
            sum = sum + i
            factors.append(i)

    print(f"The factors of 12 are {', '.join(map(str, factors))} and their sum is {sum}.")

if __name__ == "__main__":
    main()


# Output:

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_16,17,18,19,20 & 21\Assignment_17>python Assignment_17_4.py
'''
Enter Number :12
The factors of 12 are 1, 2, 3, 4, 6 and their sum is 16.
'''