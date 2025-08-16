# Parent class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def display_info(self):
        print(f"{self.name} protects {self.city} using {self.power}.")

    def fight(self):
        print(f"{self.name} is fighting crime!")


# Child class (inherits from Superhero)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    # Overriding a method (polymorphism)
    def fight(self):
        print(f"{self.name} swoops down at {self.flight_speed} km/h to stop crime!")


# Creating objects
hero1 = Superhero("ShadowMan", "invisibility", "Gotham")
hero2 = FlyingSuperhero("SkyBlade", "laser vision", "Metropolis", 500)

# Calling methods
hero1.display_info()
hero1.fight()
hero2.display_info()
hero2.fight()


# Extended Version with Encapsulation + Polymorphism 

class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self._city = city  # encapsulation attribute

    def display_info(self):
        print(f"{self.name} protects {self._city} using {self.power}.")

    def move(self):
        print(f"{self.name} is moving to save the day!")

    def fight(self):
        print(f"{self.name} is fighting crime!")

    # Encapsulation: getter for city
    def get_city(self):
        return self._city


# Child class 1
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def move(self):  # Overridden method
        print(f"{self.name} is flying at {self.flight_speed} km/h! ✈️")


# Child class 2
class SpeedsterHero(Superhero):
    def __init__(self, name, power, city, run_speed):
        super().__init__(name, power, city)
        self.run_speed = run_speed

    def move(self):  # Overridden method
        print(f"{self.name} is running at {self.run_speed} km/h! 🏃‍♂️")


# Child class 3
class WaterHero(Superhero):
    def __init__(self, name, power, city, swim_speed):
        super().__init__(name, power, city)
        self.swim_speed = swim_speed

    def move(self):  # Overridden method
        print(f"{self.name} is swimming at {self.swim_speed} km/h 🌊")


# Creating superhero objects
hero1 = FlyingHero("SkyBlade", "Laser Vision", "Metropolis", 500)
hero2 = SpeedsterHero("FlashStrike", "Super Speed", "Central City", 300)
hero3 = WaterHero("AquaQueen", "Water Control", "Atlantis", 100)

# Storing in a list for polymorphism
heroes = [hero1, hero2, hero3]

print("\n--- Superhero Team in Action ---")
for hero in heroes:
    hero.display_info()
    hero.move()
    hero.fight()