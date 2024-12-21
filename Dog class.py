class Dog:
    species = "Canis lupus familiaris"  

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def display_details(self):
        return f"Name: {self.name}, Breed: {self.breed}, Species: {Dog.species}"


if __name__ == "__main__":
    dog1 = Dog("Labrador Retriever", "Buddy")
    dog2 = Dog("German Shepherd", "Max")

    print(dog1.display_details())
    print(dog2.display_details())