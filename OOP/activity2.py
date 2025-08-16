class Animal:
  def move(self):
    print("The animal moves in some way.")
    
class Dog(Animal):
  def move(self):
    print("The dog runs!")
    
class Bird(Animal):
  def move(self):
    print("The bird flies!")
    
class Fish(Animal):
  def move(self):
    print("The fish swims!")
    
# List of different animals
animals = [Dog(), Bird(), Fish()]

# Demonstrating polymorphism
for animal in animals:
  animal.move()
  
