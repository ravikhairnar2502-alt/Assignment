# 1. Write a program which accepts one number and checks whether it is prime or not.

def main():

    Value1 = int(input("Enter number : "))

    for i in range(2,Value1):
        if Value1 % i == 0:
            print("Not Prime Number")
            break
    else:
        print("Prime Number")

if __name__ == "__main__":
    main()



# Output :

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_11>python Assignment_11_1.py
# Enter number : 11
# Prime Number

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_11>python Assignment_11_1.py
# Enter number : 6

# Not Prime Number
