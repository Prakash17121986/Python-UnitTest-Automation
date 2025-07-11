
# Abstraction in Python
# Hiding the implementation details from user
# Highlights
# Minutes of Meeting - Key points in meeting
# Way of information
# Internal or extra details to user
# Generalizing something 
# design level
# processing of identify the features need to show to user 
# and what features not to show to user


# Abstract class and Abstract Method
from abc import ABC, abstractmethod
from test_abstract_method import Vehicle

class Bike(Vehicle):

    def __init__(self, n, color):
        super().__init__(n)
        self.color = color

    def start(self):
        print("start with kick")

    def display(self):
        print("Hi I am calling from Bike class")

class scooty(Vehicle):

    def __init__(self, n, color):
        super().__init__(n)

    def start(self):
        print("self start")

    def display(self):
        print("Hi I am calling from Scooty class")

class Car(Vehicle):

    def __init__(self, n, gears):
        super().__init__(n)
        self.gears = 5

    def start(self):
        print("start with key")

    def display(self):
        print("Hi I am calling from Car class")




