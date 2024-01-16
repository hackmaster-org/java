str = input("Enter a string: ")

if 'A' <= str <= 'Z':
    print(str,"is an uppercase letter")
elif 'a' <= str <= 'z':
    print(str,"is a lowercase letter")
elif '0' <= str <= '9':
    print(str,"is a digit")
else:
    print(str,"is a symbol")