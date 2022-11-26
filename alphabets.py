import string
from random import shuffle

class Alphabets:
    
    alphabet = list(fr'''{string.printable}''')
    
    def __init__(self):
        shuffle(self.alphabet)
    

if __name__ == '__main__':
    test = Alphabets()
    print(test.alphabet)