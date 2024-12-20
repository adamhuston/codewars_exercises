import time
import threading

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = 0
        self.boredom = 0
        self.poop = 0
        self.alive = True

    def feed(self):
        self.hunger = max(0, self.hunger - 1)
        print(f"{self.name} has been fed.")

    def play(self):
        self.boredom = max(0, self.boredom - 1)
        print(f"{self.name} has been played with.")

    def clean(self):
        self.poop = max(0, self.poop - 1)
        print(f"{self.name}'s poop has been cleaned.")

    def update(self):
        while self.alive:
            time.sleep(5)
            self.age += 1
            self.hunger += 1
            self.boredom += 1
            self.poop += 1

            if self.hunger > 5 or self.boredom > 5 or self.poop > 5:
                self.alive = False
                print(f"{self.name} has died.")
                break

            print(f"{self.name} is now {self.age} years old, hunger: {self.hunger}, boredom: {self.boredom}, poop: {self.poop}")

def main():
    name = input("Enter the name of your Tamagotchi: ")
    pet = Tamagotchi(name)

    update_thread = threading.Thread(target=pet.update)
    update_thread.start()

    while pet.alive:
        action = input("Enter an action (feed, play, clean): ").strip().lower()
        if action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "clean":
            pet.clean()
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()