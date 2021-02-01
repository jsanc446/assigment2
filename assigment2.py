import socket

class Assignment2:


    def __init__(self, age=int):
        self.age = age

    def sayWelcome(self, name=str):

        print("Welcome to the assignment, " + name + "!  Haven't seen you for "
              + str(self.age) + " years!") 
