class Speaker:
    '''Represents a speaker which can print to the terminal'''
    def __init__(self, name):
        '''Initializes speaker with the robot name'''
        self.name = name
    
    def speak(self, message):
        '''Prints out a message with the speaker'''
        print(f'<{self.name}>: {message}')
