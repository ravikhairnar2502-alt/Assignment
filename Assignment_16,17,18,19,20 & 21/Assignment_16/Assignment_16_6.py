def Display(Value):
    if Value < 0:
        print("Negative")
    elif Value > 0:
        print("Positive")
    else:
        print("Zero")
        
def main():
    No = int(input("Enter Number :"))
    Display(No)

if __name__ == "__main__":
    main()


# Output:

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_16,17,18,19,20 & 21\Assignment_16>python Assignment_16_6.py
# Enter Number :5
# Positive

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_16,17,18,19,20 & 21\Assignment_16>python Assignment_16_6.py
# Enter Number :-1
# Negative

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_16,17,18,19,20 & 21\Assignment_16>python Assignment_16_6.py
# Enter Number :0
# Zero