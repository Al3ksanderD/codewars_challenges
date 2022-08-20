def calculate(num1, operation, num2):
    """
   calculate(2,"+", 4); //Should return 6
   calculate(6,"-", 1.5); //Should return 4.5
   calculate(-4,"*", 8); //Should return -32
   calculate(49,"/", -7); //Should return -7
   calculate(8,"m", 2); //Should return null
   calculate(4,"/",0) //should return null
   """
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/" and num2 != 0:
        return num1 / num2

print(calculate(2, "*", 3))