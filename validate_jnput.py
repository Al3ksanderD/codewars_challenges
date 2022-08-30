def validate_integer(user_input, min, max):
    if isinstance(user_input, int):
        if min < user_input < max:
            return user_input
        elif user_input < min:
            return min
        elif user_input > max:
            return max
        else:
            return None
print(validate_integer(10,0,100))

"""
Validate Integer
Implement the function validate_integer which receives 3 parameters: string user_input, integer min and integer max.

This function is used for validating, whether given user_input is an integer number within given range (min to max, both inclusive).

If given user_input is not an integer number, function should return None.

The received number must be then clamped into the min-max range. For example:

10 fits inside range (0, 100), therefore return 10
-10 is lesser than min of range (0, 100), therefore return 0
110 is greater that max of range (0, 100), therefore return 100
"""
