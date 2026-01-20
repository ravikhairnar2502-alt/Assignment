def main():

    Value1 = input("Enter number : ")

    if Value1 == Value1[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
         
if __name__ == "__main__":
    main()



# Output :


# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_11>python Assignment_11_5.py
# Enter number : 121
# Palindrome

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_11>python Assignment_11_5.py
# Enter number : 123
# Not Palindrome