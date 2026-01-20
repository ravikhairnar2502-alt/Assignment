def main():

    Value1 = int(input("Enter number : "))
    Ans = 0

    for i in range(1,11):
        Ans = Value1 * i
        print(Ans , end=" ")

    
if __name__ == "__main__":
    main()



# Output :

# C:\Users\EveryThink\Documents\Marvellous\Assignment>python Assignment_10_1.py
# Enter number : 4
# 4 8 12 16 20 24 28 32 36 40