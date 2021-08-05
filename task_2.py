numbers_list = []
result = 0
result_1 = 0
for number in range(1, 1001, 2):
    numbers_list.append(number ** 3)
for numb in numbers_list:
    numb = numb
    numb_17 = numb + 17
    sum = numb % 10
    sum_17 = numb_17 % 10
    remainder = numb // 10
    remainder_17 = numb_17 // 10
    while remainder > 0:
        sum +=remainder % 10
        remainder = remainder // 10
    if sum % 7 == 0:
        result+= numb
    while remainder_17 > 0:
        sum_17 += remainder_17 % 10
        remainder_17 = remainder_17 // 10
    if sum_17 % 7 == 0:
        result_1 += numb_17

print(numbers_list)
print(result)
print(result_1)