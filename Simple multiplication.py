def simple_multiplication(number) :
    """
    This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

    """
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9


print(simple_multiplication(11))