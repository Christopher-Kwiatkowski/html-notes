class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Woof!")

    def hear(self, word):
        if self.name.lower() in word:
            self.speak()
