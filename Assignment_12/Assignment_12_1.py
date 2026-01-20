# 1. Write a program which accepts one character and checks whether it is vowel or consonant.

def main():

    Vowels = ('A','a','E','e','I','i','O','o','U','u')
    Value1 = input("Enter Charachter : ")

    if Value1 in Vowels:
        print('Vowel')
    else:
        print('Consonant')

if __name__ == "__main__":
    main()



# Output :

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_12>python Assignment_12_1.py
# Enter Charachter : a
# Vowel

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_12>python Assignment_12_1.py
# Enter Charachter : x
# Consonant