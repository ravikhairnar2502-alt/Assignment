def main():
    No = int(input("Enter Number :"))
    fact = 1

    for i in range(1,No+1):
        fact = fact * i

    print(f"The factorial of {No} is {fact}")

if __name__ == "__main__":
    main()


# Output:

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_16,17,18,19,20 & 21\Assignment_17>python Assignment_17_3.py
'''
Enter Number :5
The factorial of 5 is 120
'''