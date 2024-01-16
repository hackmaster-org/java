print("\nWelcome to Bill Generator!!\n")

cost = int(input("Enter cost of a item : "))
discount = int(input("Enter discount (%) on the item : "))

sale_price = cost - (discount/100)*cost 

print("Sale price of the item : ",sale_price,"/-")