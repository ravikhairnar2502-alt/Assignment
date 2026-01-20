# 4. Write a program which accepts one number and prints that many numbers starting from 1.

def main():

    No1 = int(input("Enter number : "))
    
    for i in range(1,No1+1):
        print(i, end=' ')

if __name__ == "__main__":
    main()



# Output :

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_12>python Assignment_12_4.py
# Enter number : 5
# 1 2 3 4 5