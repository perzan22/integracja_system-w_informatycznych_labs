from gettext import find


def findEverySentence(sent: str, word: str):

    splittedSent = sent.split(word)
    indexes = []
    actualIndex = 0
    for words in splittedSent:
        wordLength = len(words)
        actualIndex += wordLength
        indexes.append(actualIndex)
        actualIndex += len(word)
    
    
    indexes.pop()
    if len(indexes) > 0:
        return indexes
    else:
        return -1

if __name__ == '__main__':

    sent = input("Proszę podać ciąg znaków: ")
    word = input("Proszę podać szukany ciąg znaków: ")
        
    print(f"Szukany ciąg znaków znajduje się na indeksach: {findEverySentence(sent, word)}")