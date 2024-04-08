from gettext import find

# funkcja zwracająca wszystkie indeksy występowania danego słowa w sentencji
def findEverySentence(sent: str, word: str):

    #podzielenie sentencji na ciągi bez szukanych słów
    splittedSent = sent.split(word)
    indexes = []
    actualIndex = 0

    #pętla sprawdza ilość znaków przed szukanym wyrazem
    #następnie ustala indeks pierwszego wyrazu
    #potem dodaje ilosc znakow w szukanym wyrazie do kolejnych znakow przed kolejnym wystąpieniem
    for words in splittedSent:
        wordLength = len(words)
        actualIndex += wordLength
        indexes.append(actualIndex)
        actualIndex += len(word)
    
    #usuwany jest z listy ostatni indeks ponieważ python uznaje koniec lini za znak
    indexes.pop()
    if len(indexes) > 0:
        return indexes
    else:
        return -1

if __name__ == '__main__':

    sent = input("Proszę podać ciąg znaków: ")
    word = input("Proszę podać szukany ciąg znaków: ")
        
    print(f"Szukany ciąg znaków znajduje się na indeksach: {findEverySentence(sent, word)}")