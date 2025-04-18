class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
    

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 3
            if self.hunger < 0:
                self.hunger = 0
            if self.happiness < 10:
                self.happiness += 1
        else:
            print(f"{self.name} is already full!")

    def sleep(self):
        if self.energy < 10:
            self.energy += 5
            if self.energy > 10:
                self.energy = 10
        else:
            print(f"{self.name} is already fully rested!")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            if self.happiness <= 8:
                self.happiness += 2
            else:
                self.happiness = 10

            if self.hunger < 10:
                self.hunger += 1
        else:
            print(f"{self.name} is too tired to play!")

    def train(self, trick):
        print(f"{self.name} is learning a new trick: {trick}")
        if trick not in self.tricks:
            self.tricks.append(trick)
            if self.happiness < 10:
                self.happiness += 1
        else:
            print(f"{self.name} already knows the trick: {trick}")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name}'s Tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
        
    def get_status(self):
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        if self.tricks:
            print(f"Tricks: {', '.join(self.tricks)}")
        else:
            print("Tricks: None")

my_pet = Pet("Navy")
my_pet.eat()         
my_pet.sleep()      
my_pet.play()
my_pet.train("roll over")
my_pet.train("sit")
my_pet.show_tricks() 
my_pet.get_status()       
          