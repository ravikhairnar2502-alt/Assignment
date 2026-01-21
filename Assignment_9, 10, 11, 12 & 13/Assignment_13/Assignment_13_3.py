# 3. Write a program which accepts one number and checks whether it is perfect number or not.

def main():

    No1 = int(input("Enter Number : "))
    sum = 0

    for i in range(1,No1):
        if No1 % i == 0:
            sum += i

    if sum == No1:
        print("Perfect Number")
    else:
        print("Non Perfect Number")

if __name__ == "__main__":
    main()



# Output :

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_13>python Assignment_13_3.py
# Enter Number : 6
# Perfect Number

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_13>python Assignment_13_3.py
# Enter Number : 7
# Non Perfect Number
