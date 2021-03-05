"""Liskov substitution principle"""
from .interfaces import Flyable


class Animal:
    """"""

    def eat(self):
        """"""


class Dog(Animal):
    """"""

    def eat(self):
        """"""
        return 'eat meat'


class Bird(Animal, Flyable):

    def eat(self):
        """"""
        return 'eat earthworms'

    def fly(self):
        """"""
        return 'Birds fly in different directions'


def eat(animal: Animal):
    animal.eat()


dog = Dog()
bird = Bird()

eat(dog)
eat(bird)
