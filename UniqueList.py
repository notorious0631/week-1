original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]


unique_list = []
for element in original_list:
    if element not in unique_list:
        unique_list.append(element)


print("Original list:", original_list)
print("Unique elements:", unique_list)
