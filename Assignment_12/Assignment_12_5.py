# 4. Write a program which accepts one number and prints that many numbers starting from 1.

def main():

    No1 = int(input("Enter number : "))
    
    for i in range(No1,0,-1):
        print(i, end=' ')

if __name__ == "__main__":
    main()



# Output :

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_12>python Assignment_12_5.py
# Enter number : 5
# 5 4 3 2 1