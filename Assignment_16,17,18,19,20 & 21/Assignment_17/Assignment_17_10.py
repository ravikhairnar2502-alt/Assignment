def Display(Value):
    sum = 0
    for i in range(len(Value)):
        sum = sum + int(Value[i])
    
    return sum

def main():
    No = input("Enter Number :")
    Ret = Display(No)
    print(f"The sum of all the numbers {", ".join(No[:-1]) + " and " + No[-1]} is {Ret}")

if __name__ == "__main__":
    main()


# Output:

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_16,17,18,19,20 & 21\Assignment_17>python Assignment_17_10.py
'''
Enter Number :5187934
The sum of all the numbers 5, 1, 8, 7, 9, 3 and 4 is 37
'''