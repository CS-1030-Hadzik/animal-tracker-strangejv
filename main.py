from animal import Animal
from dog import Dog

if __name__ == "__main__":
    # TODO: Create an instance of the Animal class
    my_animal = Animal("nobu", "canine")
        
    # TODO: Print the Animal instance
    print(my_animal)

    # TODO: Call the method to make a generic animal sound
    my_animal.speak()

    # TODO: Create an instance of the Dog class
    my_dog = Dog("Misty", "canine", "wolf")

    # TODO: Print the Dog instance
    print(my_dog)

    # TODO: Call the method to make the dog-specific sound
    my_dog.speak()

    # TODO print out all the animals
    all_animals = Animal.get_all_animals()
    for animal in all_animals:
        print(animal)
