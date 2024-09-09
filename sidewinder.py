from robot import Robot
from components.speaker import Speaker



class BingerBonger(Robot):
    def _init_(self, name):
        '''Initializes robot'''
        Robot._init_(self, name)
        self.speaker = Speaker(name)

    def speak(self):
        '''speaks'''
        if self.poweredOn:
            print("i am so on right now holy gaucomole")
        else:
            print('Robot is off. Cannot speak.')



