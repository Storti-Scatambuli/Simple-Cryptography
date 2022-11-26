import string

class Alphabets:
    alphabet = f'''{string.printable}'''


if __name__ == '__main__':
    test = Alphabets()
    print(test.alphabet)