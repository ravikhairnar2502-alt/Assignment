def main():

    Value1 = int(input("Enter number : "))

    if (Value1 % 3 == 0 and Value1 % 5 == 0):
        print(Value1,"is Divisible by 3 and 5")
    else:
        print(Value1,"is not Divisible by 3 and 5")

if __name__ == "__main__":
    main()



# Output :

# C:\Users\EveryThink\Documents\Marvellous\Assignment>python Assignment_9_5.py
# Enter number : 2
# 2 is not Divisible by 3 and 5

# C:\Users\EveryThink\Documents\Marvellous\Assignment>python Assignment_9_5.py
# Enter number : 15
# 15 is Divisible by 3 and 5


