class Engine:
    def start(self):
        print("Engine Started")
class car:
    def __init__(self):
        self.engine= Engine()
    def drive(self):
        self.engine .start()
        print("Car is moving")

c = car()
c.drive()