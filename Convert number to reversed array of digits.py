def digitize(n):
    """
    348597 => [7,9,5,8,4,3]
    0 => [0]
    Given a random non-negative number,
    you have to return the digits of this number within an array in reverse order.
    """
    n = str(n)
    reverse = []
    for value in n[::-1]:
        reverse.append(int(value))
    return reverse

print(digitize(12345))
