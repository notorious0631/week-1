number = int(input("Enter the number: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
if start <= number <= end:
    print(f"{number} is in the range [{start}, {end}].")
else:
    print(f"{number} is not in the range [{start}, {end}].")
