class Bike:
    def __init__(self):
       self.name="dicover"
       self.price=2379
       self.colour="blue"
    def accelerate(self):
       print("accelerating")
       print(self.colour)
    def breaksystem(self):
       print("bike is stopping")
    def start(self):
       print("bike is starting")
b1=Bike()
b1.start()
b1.accelerate()
b1.breaksystem()
