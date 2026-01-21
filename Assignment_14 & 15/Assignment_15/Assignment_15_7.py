# 7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

def main():
    strings = ["Ravindra", "Ravi", "Vinod", "Khairnar", "RK", "RVK"]

    Result = list(filter(lambda ret: len(ret) > 5 , strings))

    print(strings)
    print(Result)

if __name__ == "__main__":
    main()

# Output

# C:\Users\EveryThink\Documents\Marvellous\Assignment\Assignment_15>python Assignment_15_7.py
# ['Ravindra', 'Ravi', 'Vinod', 'Khairnar', 'RK', 'RVK']
# ['Ravindra', 'Khairnar']