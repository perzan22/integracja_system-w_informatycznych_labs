import math as m

#funkcja zwracajaca pierwiastki za pomocą math
def rootFinderMath():

    roots = []
    for i in range (1,257):
        root = m.sqrt(i)
        if (root % 2 == 0):
            roots.append(int(root))

    return roots

#funkcja zwracajaca pierwiastki za pomocą list comprenhension
def rootFinderLC():

    numbers = list(range(1,257))

    #uzycie list comprenhension
    roots = [int(m.sqrt(x)) for x in numbers if  m.sqrt(x) % 2 == 0]

    return roots


if __name__ == '__main__':

    print(f"Program szuka pierwiastków liczb od 1 do 256 (włącznie) podzielnych bez reszty przez 2.\nZa pomocą math: {rootFinderMath()}\nZa pomocą list comprehensions: {rootFinderLC()}")