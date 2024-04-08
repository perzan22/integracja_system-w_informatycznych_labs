import utils.obliczenia as u

if __name__ == '__main__':

    x = int(input('Proszę podać liczbę na której wykonane zostaną funkcje: pierwiastek, potęga, cosinus i sinus: \n'))
    print(f'Pierwiastek z liczby {x}: {u.pierwiastek(x)}\n')
    print(f'Potęga liczby {x}: {u.potega(x)}\n')
    print(f'Cosinus z liczby {x}: {u.cosinus(x)}\n')
    print(f'Sinus z liczby {x}: {u.sinus(x)}\n')
