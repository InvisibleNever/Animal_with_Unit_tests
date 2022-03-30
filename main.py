class Animal:

    def __init__(self, type: str):
        self.type = type

    def phrase(self):
        phrase = None
        if self.type == "cat":
            phrase = "Meow"
        elif self.type == "dog":
            phrase = "Woof"
        elif self.type == "lion":
            phrase = "Roar"
        return phrase

    def paws(self):
        paws = False if self.type == "fish" else True
        return paws

    def speed(self):
        speed = 0
        if self.type == "fish":
            speed = 56
        elif self.type == "dog":
            speed = 80
        elif self.type == "cheetah":
            speed = 110
        return speed
