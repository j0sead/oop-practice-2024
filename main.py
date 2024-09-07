#imports example robot
from example import ExampleBot

if __name__ == "__main__":

    #Testing Fred
    fred = ExampleBot('Fred')
    fred.speak()
    fred.on()
    fred.speak()
    fred.calculateSquare(4)
    fred.off()
    fred.speak()
    fred.on()
    fred.calculateSquare(3452324)


