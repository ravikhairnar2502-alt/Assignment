def Display(Value):
    for j in range(1,Value+1):
        for i in range(1,Value+1):
            print(i," ",end=" ")
        print()
            
def main():
    No = int(input("Enter Number :"))
    Display(No)

if __name__ == "__main__":
    main()


# Output:

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_16,17,18,19,20 & 21\Assignment_17>python Assignment_17_7.py
''' Enter Number :5
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5 '''