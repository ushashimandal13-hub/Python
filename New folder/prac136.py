from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def Sound(self):
        pass
    def sleep(self):
        print("Sleeping...")
class Dog(Animal):
    def Sound(self):
        print("Bark")

class Cat(Animal):
    def Sound(self):
        print("Meow")

dog = Dog()
dog.Sound()
dog.sleep()
cat = Cat()
cat.Sound()