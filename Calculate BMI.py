def bmi(weight, height):

    """
    Write function bmi_1 that calculates body mass index (bmi_1 = weight / height2).

    if bmi_1 <= 18.5 return "Underweight"

    if bmi_1 <= 25.0 return "Normal"

    if bmi_1 <= 30.0 return "Overweight"

    if bmi_1 > 30 return "Obese"
    """
    bmi_1 = weight / height ** 2
    if bmi_1 > 30:
        return "Obese"
    if 30.0 >= bmi_1 > 25.0:
        return "Overweight"
    if 25.0 >= bmi_1 > 18.5:
        return "Normal"
    elif bmi_1 <= 18.5:
        return "Underweight"


print(bmi(88, 1.82))