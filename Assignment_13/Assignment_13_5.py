''' 
5. Write a program which accepts marks and displays grade.
Condition Example:
≥75 Distinction
≥ 60→ First Class
≥ 50 Second Class
< 50 - Fail
'''

def main():

    No1 = int(input("Enter Radius : "))
    
    if No1 >= 75:
        print("Distinction")
    elif No1 >=60:
        print("First Class")
    elif No1 >=50:
        print("Second Class")
    elif No1 < 50:
        print("Fail")

if __name__ == "__main__":
    main()



# Output :

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_13>python Assignment_13_5.py
# Enter Radius : 85
# Distinction

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_13>python Assignment_13_5.py
# Enter Radius : 60
# First Class

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_13>python Assignment_13_5.py
# Enter Radius : 54
# Second Class

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_13>python Assignment_13_5.py
# Enter Radius : 42
# Fail