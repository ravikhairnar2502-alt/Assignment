# 5.Write a program which accepts one number and prints all odd numbers till that number.

def main():

    Value1 = int(input("Enter number : "))
    Ans = 0

    for i in range(1,Value1+1,2):
        print(i, end=' ')

    
if __name__ == "__main__":
    main()



# Output :

# C:\Users\EveryThink\Documents\Marvellous\Assignment>python Assignment_10_5.py
# Enter number : 10

# 1 3 5 7 9
