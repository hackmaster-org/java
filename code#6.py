cost = float(input("Enter a cost price of an item : "))

gst = (18/100)*cost

print("\nGst on the item is :",gst,"/-")

sell_price = cost + gst

print("Total amount with gst is",sell_price)