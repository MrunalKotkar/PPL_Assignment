#Inheritance is a mechanism that allows us to create a new class – known as child class –
#that is based upon an existing class – the parent class, by adding new attributes and methods
#on top of the existing class. When you do so, the child class inherits the attributes and methods of the parent class.
import math

class Shape:
    def __init__(self, filled=False):
        self.__filled = filled
    def get_filled(self):
        return self.__filled
    def set_filled(self, filled):
        self.__filled = filled

class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth
    def get_area(self):
        return self.__length * self.__breadth
    def get_perimeter(self):
        return 2 * (self.__length + self.__breadth)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius
    def get_area(self):
        return math.pi * self.__radius ** 2
    def get_perimeter(self):
        return 2 * math.pi * self.__radius


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def get_area(self):
        sp = (self.side1 + self.side2 + self.side3) / 3
        return math.sqrt(sp * (sp - self.side1) * (sp - self.side2) * (sp - self.side3))
    def get_perimeter(self):
        return (self.side1 + self.side2 + self.side3)


class Ellipse(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
    def get_area(self):
        return math.pi * self.a * self.b
    def get_perimeter(self):
       pass

class Square(Rectangle):
    def __init__(self, a):
        super().__init__()
        self.a = a
    def get_area(self):
        return self.a * self.a
    def get_perimeter(self):
        return 4 * self.a

class EquilateralTraingle(Triangle):
    def __init__(self, side):
        super().__init__()
        self.side = side
    def get_area(self):
        return (math.sqrt(3)/4)*self.side*self.side
    def get_perimeter(self):
        return 3 * self.side

class Polygon(Shape):
    def __init__(self, nsides=3, side=4):
        super().__init__()
        self.n = nsides
        self.l = side
    def get_perimeter(self, name):
        return self.n * self.l
    def get_area(self, name):
        p = self.l * self.n
        a = p / math.tan(180 / self.n)
        A = p * a
        return  A / 2



r1 = Rectangle(10.5, 2.5)
print(r1.get_area())
c1 = Circle(12)
print(c1.get_perimeter())
t1 = Triangle(5, 12, 13)
print(t1.get_area())
e1 = Ellipse(3, 4)
print(e1.get_area())


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cat(Animal):
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

class Dog(Animal):
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

class Lion(Animal):
    def info(self):
        print(f"I am a Lion. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Roar")

class Cow(Animal):
    def info(self):
        print(f"I am a cow. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Moo")

class Elephant(Animal):
    def info(self):
        print(f"I am a elephant. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Trumpets")

class Rabbit(Animal):
    def info(self):
        print(f"I am a rabbit. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Squeak")

class Goat(Animal):
    def info(self):
        print(f"I am a goat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bleat")

class Deer(Animal):
    def info(self):
        print(f"I am a deer. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bucks")

class Tiger(Animal):
    def info(self):
        print(f"I am a tiger. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Growls")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)
tiger1 = Tiger("Panthera", 6)
deer1 = Deer("Reindeer", 5)
goat1 = Goat("Billy", 7)
lion1 = Lion("Ari", 12)
cow1 = Cow("Bella", 13)
rabbit1 = Rabbit("Oreo", 5.6)
elephant1 = Elephant("Serania", 15)

cat1.make_sound()
dog1.info()
tiger1.make_sound()