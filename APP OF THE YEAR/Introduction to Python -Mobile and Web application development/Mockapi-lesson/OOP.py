class Cat:
    # TODO 1: add an extra parameter to the constructor to define the colour
    # of the cat and store it for use
    def __init__(self, name, color="black"):
        self.name = name
        self.color = color

    def meow(self):
        print(f"Meow  my name is {self.name}")

    # TODO 2: Define a method called Jump that takes in a value and prints
    # "The {color} cat jumps x meters high"
    def Jump(self, height):
        print(f"The {self.color} cat jumps {height} meters high")


def demo():
    cat1 = Cat("sussie")

    cat2 = Cat("Bob")

    # TODO 3: Create a new cat object with name JOHN and colour purple
    cat3 = Cat("JOHN", "purple")

    cat1.meow()
    cat2.meow()
    cat3.meow()

    cat1.name = "Tiffany"

    # TODO 4: Change the colour of cat 2 to be white and observe the change
    cat2.color = "white"

    cat1.meow()
    cat2.meow()
    cat3.meow()

    # TODO 5: Call the newly defined Jump method on each cat here
    # and observe what it prints
    cat1.Jump(2)
    cat2.Jump(1.5)
    cat3.Jump(3)


demo()