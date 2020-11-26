#1
def pattern(totalrows):

    for i in range(1, totalrows + 1):

        for k in range(1, i):
            print(" ", end="")

        for j in range(i, totalrows + 1):
            print(j, end=" ")

        print()

        for i in range(totalrows - 1, 0, -1):


         for k in range(1, i):
            print(" ", end="")


        for j in range(i, totalrows + 1):
            print(j, end=" ")

        print()

totalrows = 5

pattern(totalrows)



#2
class Vehicle:
    def __init__(self, milage, price):
        self.milage=milage
        self.price=price
        return
class car(Vehicle):
    ownershipcost=int(input("enter owner ship cost"))
    warrenty=int(input("entr the warrenty details"))
    seatingcapacity=int(input("enter seating capacity"))
    fuel=int(input("enter fuel type diesel/petrol"))
