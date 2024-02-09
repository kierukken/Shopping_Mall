class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def newitem(self, item, quantity, cost):
        self.cart[item] = {"quantity":quantity, "cost":cost}

    def additem(self, item, quantity):
        self.cart[item]['quantity'] += quantity

    def removeitem(self, item, quantity):
        self.cart[item]['quantity'] -=  quantity
        if self.cart[item]['quantity'] <= 0:
            print("Removed all of",item,"from the shopping cart")
            self.cart.pop(item)
        else:
            print("Successfully removed",quantity,item,"from the shopping cart!")

    def printcart(self):
        print(self.cart)

    def printreciept(self):
        print("------------SHOPPING-MALL-------------\n---------------RECIEPT----------------\nItem------------Amount------------Cost")
        for x in self.cart:
            subtotal = 0
            print(x.ljust(21-len(x)), str(self.cart[x]['quantity']), str(self.cart[x]['quantity']*self.cart[x]['cost']).rjust(21-len(str(self.cart[x]['quantity']*self.cart[x]['cost']))))
            subtotal += self.cart[x]['quantity']*self.cart[x]['cost']
        print("\n\n")
        print("Subtotal:", str(subtotal).rjust(20),"\nTax:", str(subtotal*0.13).rjust(20),"\nTotal:", str(subtotal*1.13).rjust(20))
        print("--------------------------------------\n--------------------------------------")

Cart1 = ShoppingCart()
while True:
    userinput = input("\nWhat would you like to do?\n1) Buy Item(s)\n2) Remove Item(s)\n3) Print Receipt\n4) Finish Shopping\n\n")
    if userinput == "1":
        item = input("What do you want to buy? ")
        quantity = int(input("How many? "))
        if item not in Cart1.cart:
            cost = float(input("Cost per item? "))
            Cart1.newitem(item, quantity, cost)
        else:
            Cart1.additem(item, quantity)
    elif userinput == "2":
        item = input("What do you want to remove? ")
        if item not in Cart1.cart:
            print("You do not have", item)
        else:
            quantity = int(input("How many? "))
            Cart1.removeitem(item, quantity)
    elif userinput == "3":
        Cart1.printreciept()
    elif userinput == "4":
        print("Thank you for shopping at shopping mall")
        exit()
    else:
        print("Invalid please select one of the options: ")