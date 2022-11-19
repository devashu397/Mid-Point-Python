first_xcord = int(input("Enter the first X-coordinate: "))
second_xcord = int(input("Enter the second X-coordinate: "))
first_ycord = int(input("Enter the first Y-coordinate: "))
second_ycord = int(input("Enter the second Y-ccordinate: "))

x = (first_xcord + second_xcord) / 2
y = (first_ycord + second_ycord) / 2
cord = (x, y)

print(f"\nMid Point of these coordinates is: {cord}")