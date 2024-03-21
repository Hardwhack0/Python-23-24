class Dog:
    def __init__(self, name):
        self.name = name
        print(f"Vytvářím objekt psa s jménem {self.name}.")

    def bark(self):
        print(self.name + " štěká!")