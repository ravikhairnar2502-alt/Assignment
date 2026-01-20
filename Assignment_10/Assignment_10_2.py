# 2. Write a program which accepts one number and prints sum of first N natural numbers.

def main():

    Value1 = int(input("Enter number : "))
    Ans = 0

    for i in range(1,Value1+1):
        Ans += i
    
    print(Ans , end=" ")

    
if __name__ == "__main__":
    main()



# Output :

# C:\Users\EveryThink\Documents\Marvellous\Assignment>python Assignment_10_2.py
# Enter number : 5

# 15
