class Vehicle:
    def init(self,milage,price):
        self.milage=milage
        self.price=price
class Car(Vehicle):
    def init(self, cost, warranty, seatingcapacity, fuelType, milage, price):
        super().init(milage, price)
        self.cost=cost
        self.warranty=warranty
        self.seatingcapacity=seatingcapacity
        self.fueltype=fuelType
class Bike(Vehicle):
    def init(self, ncylinders, ngears, ctype, wtype, fueltsize, milage, price):
        super().init(milage, price)
        self.ncylinders=ncylinders
        self.ngears=ngears
        self.ctype=ctype
        self.wtype=wtype
        self.fueltsize=fueltsize
class Audi(Car):
    def __init__(self, modeltype, cost, warranty, seatingcapacity, fuelType, milage, price):
        super().init(cost, warranty, seatingcapacity, fuelType, milage, price)
        self.modeltype=modeltype
        print('Modeltype =', self.modeltype, ',', 'cost =', self.cost, ',', 'warranty =', self.warranty, ',',
              'seat capactiy =', self.seatingcapacity, ',', 'fuel type =', self.fueltype, ',', 'mileage =', self.milage,
              ',', 'price=', self.price)
        return


class Ford(Car):
    def __init__(self, modeltype, cost, warranty, seatingcapacity, fuelType, milage, price):
        super().init(cost, warranty, seatingcapacity, fuelType, milage, price)
        self.modeltype=modeltype
        print('Modeltype =', self.modeltype, ',', 'cost =', self.cost, ',', 'warranty =', self.warranty, ',',
              'seat capactiy =', self.seatingcapacity, ',', 'fuel type =', self.fueltype, ',', 'mileage =', self.milage,
              ',', 'price=', self.price)
        return
class Bajaj(Bike):
    def __init__(self, maketype, ncylinders, ngears, ctype, wtype, fueltsize, milage, price):
        super().init(ncylinders, ngears, ctype, wtype, fueltsize, milage, price)
        self.maketype=maketype
        print('maketype=', self.maketype, ',', 'numberofcylinders=', self.ncylinders, ',', 'numberofgears=',
              self.ngears, 'coolingtype=', self.ctype, ',', 'wheeltype=', self.wtype, ',',
              'fueltanksize=', self.fueltsize, ',', 'mileage=', self.milage, ',', 'price=', self.price)
        return
class TVS(Bike):
    def __init__(self, maketype, ncylinders, ngears, ctype, wtype, fueltsize, milage, price):
        super().init(ncylinders, ngears, ctype, wtype, fueltsize, milage, price)
        self.maketype=maketype
        print('maketype=', self.maketype, ',', 'numberofcylinders=', self.ncylinders, ',', 'numberofgears=',
              self.ngears, 'coolingtype=', self.ctype, ',', 'wheeltype=', self.wtype, ',',
              'fueltanksize=', self.fueltsize, ',', 'mileage=', self.milage, ',', 'price=', self.price)
        return

x=Audi('Q5','100000','10','3','electric' ,'2' ,'3400')
y=Ford('sedan','10000','10','2','electric',2,'10 lakhs')
z=Bajaj('Steel','15','7','liquid','alloy','9','150','30k')
w=TVS('aluminium','10','6','liquid','alloy','10','100','10k')
