def Display(Value):
    MinusV = 0
    for i in range(Value,):
        MinusV = Value - i
        print("*    "*MinusV)
        


      
def main():
    No = int(input("Enter Number :"))
    Display(No)

if __name__ == "__main__":
    main()


# Output:

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_16,17,18,19,20 & 21\Assignment_17>python Assignment_17_6.py
''' Enter Number :5
*    *    *    *    *
*    *    *    *
*    *    *
*    *
*  '''