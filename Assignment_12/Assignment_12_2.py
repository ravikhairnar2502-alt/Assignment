# 2. Write a program which accepts one number and prints its factors.

def main():

    Value1 = int(input("Enter Charachter : "))
    i = 1

    while i <= Value1:
        if Value1 % i == 0:
            print(i, end=' ')
        i += 1

if __name__ == "__main__":
    main()



# Output :

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_12>python Assignment_12_2.py
# Enter Charachter : 12
# 1 2 3 4 6 12