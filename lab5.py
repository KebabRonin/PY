import math, random

# Ex1
class Shape:
    def __init__(self, x=0, y=0, rot=0):
        self.x = x
        self.y = y
        self.rot = rot

class Circle(Shape):
    def __init__(self, radius, x=0, y=0, rot=0):
        super().__init__(x, y, rot)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, width, height, x=0, y=0, rot=0):
        super().__init__(x, y, rot)
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)
    
class Triangle(Shape):
    def __init__(self, l1, l2, l3, x=0, y=0, rot=0):
        super().__init__(x, y, rot)
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def area(self):
        s = (self.l1 + self.l2 + self.l3)/2
        return math.sqrt(s * ((s - self.l1)**2) * ((s - self.l2)**2) * ((s - self.l3)**2))
    
    def perimeter(self):
        return self.l1 + self.l2 + self.l3
    


# Ex2
class Account:
    def __init__(self):
        self.money = 0
        self.loans = []
    def deposit(self, new_money):
        self.money += new_money * (1 + self.interest())
    def withdraw(self, new_money):
        self.money -= new_money
        return new_money
    def interest(self):
        return -0.002
    
class SavingsAccount(Account):
    def __init__(self):
        super().__init__()
        del self.withdraw
    def interest(self):
        return 0.01
    
class CheckingAccount(Account):
    def __init__(self):
        super().__init__()
        del self.withdraw
        del self.deposit
    def interest(self):
        return 0
    
    

# Ex3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    mileage = {('Toyota', 'X35', 2002): 60, ('Scania', 'X35', 2002): 30, ('BMW', 'X35', 2002): 235}
    tow_cap = {('Toyota', 'X35', 2002): 4000, ('Scania', 'X35', 2002): 100, ('BMW', 'X35', 2002): 600}
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.doors = 4
    def get_mileage(self):
        # return Car.mileage[(self.make, self.model, self.year)]
        return 4.3
    def get_tow_cap(self):
        # return Car.tow_cap[(self.make, self.model, self.year)]
        return 600
    
class Truck(Vehicle):
    mileage = {('Toyota', 'X35', 2002): 80, ('Scania', 'X35', 2002): 100, ('BMW', 'X35', 2002): 150}
    tow_cap = {('Toyota', 'X35', 2002): 1500, ('Scania', 'X35', 2002): 3000, ('BMW', 'X35', 2002): 5000}
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.doors = 2
    def get_mileage(self):
        # return Truck.mileage[(self.make, self.model, self.year)]
        return 5
    def get_tow_cap(self):
        # return Truck.tow_cap[(self.make, self.model, self.year)]
        return 5000
    
class Boat(Vehicle):
    mileage = {('Toyota', 'X35', 2002): 45, ('Scania', 'X35', 2002): 22, ('BMW', 'X35', 2002): 80}
    tow_cap = {('Toyota', 'X35', 2002): 15, ('Scania', 'X35', 2002): 30, ('BMW', 'X35', 2002): 50}
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.windows = 7
    def get_mileage(self):
        # return Boat.mileage[(self.make, self.model, self.year)]
        return 7.3
    def get_tow_cap(self):
        # return Boat.tow_cap[(self.make, self.model, self.year)]
        return 300


c = ('Toyota', 'X35', 2002)
print("Car_m:", Car(*c).get_mileage())
print("Car_t:", Car(*c).get_tow_cap())
print("Truck_m:", Truck(*c).get_mileage())
print("Truck_t:", Truck(*c).get_tow_cap())
print("Boat_m:", Boat(*c).get_mileage())
print("Boat_t:", Boat(*c).get_tow_cap())



# Ex4
class Employee:
    def __init__(self, salary):
        self.salary = salary
class Manager(Employee):
    def __init__(self, salary):
        super().__init__(salary)
    def manage(self, other):
        other.salary = 0
    def fire(self, other):
        del other
    def promote(self, other):
        other.salary += 1000

class Engineer(Employee):
    def __init__(self, salary, lang):
        super().__init__(salary)
        self.lang = lang
    def fix(self, *problems):
        for p in problems:
            print(f"{p}: LGTM 👍")
    def cry(self, reason= None):
        print("😭")

class Salesperson(Employee):
    def __init__(self, salary):
        super().__init__(salary)
    def make_pitch(self, product):
        print(f"{product} is a very nice product")
    def sell(self, product):
        print(f"{product}: Yours for only 19.99$")
        return 19.99


Abibas = [Salesperson(4500), Engineer(5000, 'py'), Engineer(7000, 'rust'), Engineer(0, 'haskell'), Salesperson(1500)]
m = Manager(1000000000)
for e in Abibas:
    appeals = [f for f in dir(e) if not f.startswith("__") and callable(getattr(e, f))]
    f = getattr(e, appeals[random.randrange(len(appeals))])
    f('Shoes')
    m.fire(e)



# Ex5
class Animal:
    pass

class Mammal(Animal):
    def __init__(self, speed):
        self.speed = speed
    def spawn_living_child(self):
        return Mammal(self.speed + random.random())
    
class Bird(Animal):
    def __init__(self, speed, flyspeed):
        self.speed = speed
        self.flyspeed = flyspeed
        self.state = 'grounded'
    def lay_egg(self):
        return "egg"
    def take_off(self):
        self.state = 'flying'
    def land(self):
        self.state = 'grounded'

class Fish(Animal):
    def __init__(self, swimspeed):
        self.speed = swimspeed
        self.home = (0,0)
    def make_home(self, position):
        x, y = position
        self.home = (x, y)



# Ex6
class LibraryItem:
    def __init__(self):
        self.in_library = True
    def check_out(self):
        self.in_library = False
    def ret(self):
        self.in_library = True
    def display_info(self):
        print("Unidentified object")
    
class Book(LibraryItem):
    def __init__(self):
        super().__init__()
    def display_info(self):
        print("Interesting book")
    
class DVD(LibraryItem):
    def __init__(self):
        super().__init__()
    def display_info(self):
        print("Interesting DVD")
    
class Magazine(LibraryItem):
    def __init__(self):
        super().__init__()
    def display_info(self):
        print("Interesting magazine")

catalog = [Magazine(), Book(), Book(), Book(), DVD(), DVD()]

for c in catalog:
    c.display_info()