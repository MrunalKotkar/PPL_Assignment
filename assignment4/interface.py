from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass

class Child(Father):
    def disp1(self):
        print("Child Class")
        print("disp1 abstract Method")

class Grandchildren(Child):
    def disp2(self):
        print("Grandchildrn Class")
        print("disp2 abstract Method")



g = Grandchildren()
g.disp1()
g.disp2()