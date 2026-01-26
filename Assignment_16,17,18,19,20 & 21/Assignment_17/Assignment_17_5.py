def main():

    Value1 = int(input("Enter number : "))

    for i in range(2,Value1):
        if Value1 % i == 0:
            print("Not Prime Number")
            break
    else:
        print("It is Prime Number")
    
if __name__ == "__main__":
    main()


# Output:

#C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_16,17,18,19,20 & 21\Assignment_17>python Assignment_17_5.py
'''
Enter number : 5
It is Prime Number
'''