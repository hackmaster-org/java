num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter a number: "))

operator = input("Enter a operator(+, -, *, /): ")


if operator == "+":
    val = num_1 + num_2
    print(num_1,"+",num_2,"is :",val)
elif operator == "-":
    val = num_1 - num_2
    print(num_1,"-",num_2,"is :",val)
elif operator == "*":
    val = num_1 * num_2
    print(num_1,"*",num_2,"is :",val)
elif operator == "/":
    if num_2 != 0:  
        val = num_1 / num_2
        print(num_1,"/",num_2,"is :",val)
    else:
        print("Cannot divide by zero!!")
else:
    print("Invalid operator!!")



