n = int(input("Enter a number: "))
factorial = 1

if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0 or n == 1:
    print(f"The factorial of {n} is 1.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}.")
33