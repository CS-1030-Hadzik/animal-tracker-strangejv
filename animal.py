class Animal:
    """
    Base class representing a generic animal.
    """
    # Class-level attribute
    kingdom = "Animalia"

    # TODO create a class-level attribute that is a list of all the Animal objects
    all_animals = []

    # TODO create the initializer for Animal with name and species as attributs
    def __init__(self, name, species):
        self.name = name
        self.species = species

        Animal.all_animals.append(self)

    # TODO: Add a method to make a generic sound 
    # Call the method `speak` and make it output a specific message like 
    # "The animal makes a noise.""
    def speak(self):
        print("Then animal makes a noise")

    # TODO __str__ method for string representation
    # Example output
    # Kingdom: 'kingdom attribute', Name: 'name attribute' Species: 'species attribute' 
    def __str__(self):
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}' Species: '{self.species}'"
