import random
import string


def dictionaryRandom():

    _24006 = {
        '10': "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8)),
        '11': "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8)),
        '12': "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8)),
        '13': "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8)),
        '14': "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8)),
        '15': "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8)),
        '16': "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8)),
        '17': "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8)),
        '18': "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8)),
        '19': "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8)),
        '20': "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    }

    return _24006

if __name__ == '__main__':
    print(f'Program wypisuje random słownik.\nSłownik: \n{dictionaryRandom()}')