class Pet:
    def __init__(self):
      self.name = ""
      self.type = ""
      self.age = 0

  # Setters
    def setName(self, name):
        self.name = name

    def setType(self, pet_type):
        self.type = pet_type

    def setAge(self, age):
        self.age = age     

  # Accessors    
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age


# Main Program
def main():
  # Create a Pet object
  pet = Pet() 

  # Ask user for pet details
  pet_name = input("Enter the name of your pet:")
  pet_type = input("Enter the type of animal:")
  pet_age = input("Enter your pet's age:")

  # Store data in the Pet object
  pet.setName(pet_name)
  pet.setType(pet_type)
  pet.setAge(pet_age) 

  # Display the pet's information using accessor methods
  print("\nPet Information:")              
  print(f"Name:{pet.getName()}")
  print(f"Type:{pet.getType()}")
  print(f"Age:{pet.getAge()}")

# Call the main function
if __name__ == "__main__":
  main() 