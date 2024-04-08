from gettext import find

#funkcja sprawdza pierwsze wystąpienie danego ciągu w sentencji
def findSentence(sent: str, word: str) -> int:

    index = sent.find(word)
    return index

if __name__ == '__main__':

    sent = input("Proszę podać ciąg znaków: ")
    word = input("Proszę podać szukany ciąg znaków: ")
        
    print(f"Szukany ciąg znaków znajduje się na indeksie: {findSentence(sent, word)}")