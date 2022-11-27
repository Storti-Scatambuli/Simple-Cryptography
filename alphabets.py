import string
from random import shuffle
from random import choice

class Alphabets:
    
    def __init__(self):
        
        self.alphabet = list(fr'''{string.printable}''')

        

        shuffle(self.alphabet)
        
    
    def generate_key(self):
        
        self.__alphabet_code = []
        
        self.__key_characters = list(fr'''{string.ascii_letters}{string.digits}{string.punctuation}''')
        
        for character in self.__key_characters:
            
            self.__alphabet_code.append(ord(character))
            
            return choice(self.__alphabet_code)
        
if __name__ == '__main__':
    test = Alphabets()
    print(test.alphabet)
    print(test.generate_key())