import others
import operators
import trig
operator = input("Enter oprator")
if operator == "cube":
    num = eval (input("Enter number"))
    x = others.cube(num)
    print(x)
elif operator == ("sin"):
    angle = eval(input("Enter angle in degrees"))
    sin_of_angle= trig.get_sine(angle)
    print(sin_of_angle)
elif operator == ("tan"):
    angle = eval(input("Enter angle in degres : "))
    print(trig.get_tan(angle))
else:
    num1 =eval(input("Enter number 1 :"))
    num2 = eval(input("Enter number 2 :"))

    if operator == "+":
        x = operators.add(num1,num2)
        print (x)
    elif operator == "-":
        x = operators.difference(num1 ,num2)
        print (x)
    elif operator == "x"or"X"or"*":
        x = operators.multiply(num1,num2)
        print(x)
    

    

# x = others.cube(3)
# y = operators.add(3,3)
# print (x)
# print(y)
# # y =    subtract(30,15)

# print (y)
