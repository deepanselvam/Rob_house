def maximumAmountRobbed(array):
    amount_1 = 0
    amount_2 = 0
    for iterator in range(len(array)):
        amount_1 += array[iterator] if iterator % 2 == 0 else 0
        amount_2 += array[iterator] if iterator % 2 != 0 else 0
    return max(amount_1, amount_2)

print(maximumAmountRobbed([2,7,9,3,1]))
