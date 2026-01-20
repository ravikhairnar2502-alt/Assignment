def main():

    Value1 = input("Enter number : ")
    Ans = 0

    for i in range(len(Value1)):
        Ans += int(Value1[i])
    
    print(Ans , end=" ")

    
if __name__ == "__main__":
    main()



# Output :


# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_11>python Assignment_11_3.py
# Enter number : 123
# 6