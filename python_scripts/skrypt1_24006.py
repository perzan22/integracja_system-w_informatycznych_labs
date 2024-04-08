from curses.ascii import isdigit

# pierwszy sposób sprawdzenia czy znak jest liczbą za pomocą isdigit
def isSignDigit1(input: str) -> str:

    isNumber = isdigit(input)
    if (isNumber):
        response = 'liczba'
    else:
        response = 'nie liczba'
        
    return response

#drugi sposób sprawdzenia czy znak jest liczbą za pomocą isinstance
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
