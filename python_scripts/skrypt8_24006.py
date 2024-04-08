import random
import string
from typing import Counter


def generateSentence():
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(100))

def createDictionary(sent: str):
    
    dictionary = Counter(sent)
    return dict(dictionary)

def createList(sent: str):

    dictionary = Counter(sent)
    return list(dictionary)


if __name__ == '__main__':

    sent = generateSentence()
    print(f'Wygenerowany ciąg 100 randomowych znaków: {sent}\n')
    print(f'Wygenerowany słownik: {createDictionary(sent)}\n')
    print(f'Wygenerowana lista unikalnych znaków: {createList(sent)}')
