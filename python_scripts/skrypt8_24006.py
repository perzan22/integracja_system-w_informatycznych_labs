import random
import string
from typing import Counter


#funkcja generująca 100 znakowy ciąg randomowych znaków
def generateSentence():
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(100))

#funkcja tworząca słownik, gdzie kluczqami są występujące znaki w ciągu a wartościami są ilości powtózeń tych znaków
def createDictionary(sent: str):
    
    dictionary = Counter(sent)
    return dict(dictionary)

#funkcja tworząca listę unikaljnych znaków w ciągu
def createList(sent: str):

    dictionary = Counter(sent)
    return list(dictionary)


if __name__ == '__main__':

    sent = generateSentence()
    print(f'Wygenerowany ciąg 100 randomowych znaków: {sent}\n')
    print(f'Wygenerowany słownik: {createDictionary(sent)}\n')
    print(f'Wygenerowana lista unikalnych znaków: {createList(sent)}')
