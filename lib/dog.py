#!/usr/bin/env python3

class Dog:
    def sit(self):
        print("The dog is sitting.")
    
    def bark(self):
        print("Woof!")

if __name__ == "__main__":
    my_dog = Dog()
    my_dog.sit()  # This will print: The dog is sitting.
    my_dog.bark() # This will print: Woof!
