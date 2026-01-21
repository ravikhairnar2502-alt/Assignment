# 2. Write a program which accepts radius of circle and prints area of circle.

import math

def main():

    Radius = float(input("Enter Radius : "))
    Area = math.pi * (Radius ** 2)
    print("Area of Rectangle :", round(Area,2))

if __name__ == "__main__":
    main()



# Output :

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_13>python Assignment_13_2.py
# Enter Radius : 20
# Area of Rectangle : 1256.64