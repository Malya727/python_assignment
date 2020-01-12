# Accept the cost price and selling price of an item as a user input. Write a program to determine whether the seller has made a profit or incurred a loss. Also, determine the quantum of profit or loss. 
print("Program to Find whether a customer Encountered Proft or Loss")
cost_p = int(input("Enter Cost Price of Product :"))
selling_p = int(input("Emter Selling Price of Product :"))

result = cost_p - selling_p

if result >= 0:
    print("Seller made a Profit of " +str(result)+ " RS")
else:
    result = result * -1
    print("Seller encountered a Loss of " +str(result)+ " RS")

