mainlist = [[1, 2, 3], [3, 5, 6], [1, 2, 2]]
highest_total = float('-inf')
lowest_total = float('inf')
highest_output = []
lowest_output = []

for sublist in mainlist:
    total = sum(sublist)

    if total > highest_total:
        highest_total = total
        highest_output = sublist

    if total < lowest_total:
        lowest_total = total
        lowest_output = sublist

print(f'List with the highest total value in the nested list is {highest_output}')
print(f'List with the lowest total value in the nested list is {lowest_output}')
