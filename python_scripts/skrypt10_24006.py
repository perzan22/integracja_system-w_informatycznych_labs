#funkcja zapisująca alfabet do plików
def writeAlphabet():

    #pętla generuje alfabet
    alph = ''
    for i in range(97,123):
        alph += chr(i)
    
    #zapisanie alfabetu do pliku w jednej lini
    #menedżer kontekstu with zapewnia że po wykonaniu bloku kodu
    #zasób (w tym przypadku plik alfabet1-24006) zostanie zwolniony
    with open(f'alfabet1-24006.txt', 'w') as file1:
        file1.write(alph)

    #zapisanie alfabetu do pliku za pomocą pętli dzięki czemu każda litera jest pod sobą
    with open(f'alfabet2-24006.txt', 'w') as file2:
        for letter in alph:
            file2.write(letter + '\n')
    
    print('Zapisano poprawnie')

if __name__ == '__main__':

    writeAlphabet()