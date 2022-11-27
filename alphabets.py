import string
from random import shuffle
from random import choice

class Alphabets:
    
    def __init__(self):
        
        self.alphabet = list(fr'''{string.printable}''')

        self.__alphabet_code = []
        
        self.__key_characters = list(fr'''{string.ascii_letters}{string.digits}{string.punctuation}''')
        
        for character in self.__key_characters:
            
            self.__alphabet_code.append(ord(character))

        shuffle(self.alphabet)
        
        self.primary_key = choice(self.__alphabet_code)
        
if __name__ == '__main__':
    test = Alphabets()
    print(test.alphabet)
    print(test.primary_key)
    print(chr(test.primary_key))