def min_value(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number

list = [1,2,3,4,5,0]
print(min_value(list))