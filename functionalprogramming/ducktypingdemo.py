class Swift:
    def start(self):
        print("swift car start method")
    def accelerate(self):
        print("accelerate functionality in swift")
    def brk(self):
        print ("break functionality in swift")
class Innova:
    def start(self):
        print("swift car start innova")

    def accelerate(self):
        print("accelerate functionality in innova")

    def brk(self):
        print("break functionality in innova")
class Person:
    def drive(self,car):
        self.car=car
        car.start()
        car.accelerate()
        car.brk()
sw=Swift()
ino=Innova()
p=Person()
#p.drive(sw)
p.drive(ino)
