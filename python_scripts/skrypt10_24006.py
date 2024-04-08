def writeAlphabet():

    alph = ''
    for i in range(97,123):
        alph += chr(i)
    
    with open(f'alfabet1-24006.txt', 'w') as file1:
        file1.write(alph)

    with open(f'alfabet2-24006.txt', 'w') as file2:
        for letter in alph:
            file2.write(letter + '\n')
    
    print('Zapisano poprawnie')

if __name__ == '__main__':

    writeAlphabet()