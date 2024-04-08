from curses.ascii import isdigit


def isSignDigit1(input: str) -> str:

    isNumber = isdigit(input)
    if (isNumber):
        response = 'liczba'
    else:
        response = 'nie liczba'
        
    return response

def isSignDigit2(input: str) -> str:

    isNumber = isinstance(input, str)
    if (isNumber and input.isdigit()):
        response = 'liczba'
    else:
        response = 'nie liczba'
    
    return response


if __name__ == '__main__':
    
    sent = input('Podaj znak: ')
    print(f"Sposób isdigit\nPodany pierwszy znak to: {isSignDigit1(sent[0])}")
    print(f"Sposób isinstance\nPodany pierwszy znak to: {isSignDigit2(sent[0])}")
