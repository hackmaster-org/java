num = int(input("Enter a Number : "))

num_2 = int(input("Enter a Number : "))

num_3 = int(input("Enter a Number : "))


if(num>num_2):
    if(num>num_3):
        print(num,"is greatest among three numbers")
elif(num_2>num):
    if(num_2>num_3):
        print(num_2,"is greatest among three numbers")
else:
    print(num_3,"is greatest among three numbers")