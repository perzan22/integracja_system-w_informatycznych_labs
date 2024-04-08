from curses.ascii import isdigit


def isNumber(input: str) -> str:

    sent = input
    letters = []
    for letter in sent:
        letters.append(letter.isdigit())

    isNumber = all(letters)
    if(isNumber):
        return "Podany ciąg znaków jest liczbą."
    else:
        return "Podany ciąg znaków nie jest liczbą."


if __name__ == '__main__':

    sent = input("Proszę podać ciąg znaków składającty się conajmniej z dwócz znaków: ")

    while len(sent) < 2:
        print("Ciąg znaków musi mieć conajmniej 2 znaki\n")
        sent = input("Proszę podać ciąg znaków składającty się conajmniej z dwócz znaków: ")
        
    print(f"{isNumber(sent)}")
