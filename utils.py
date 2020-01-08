import random
import string
import pyperclip


class RandomKeygen:
    size = 32
    chars = string.ascii_letters + string.digits

    def __init__(self, size=size, chars=chars):
        randkey = ''.join(random.choice(chars) for x in range(size))
        print('A random key copied on you clipboard.')
        copy_output = pyperclip.copy(randkey)
        return copy_output


if __name__ == "__main__":
    RandomKeygen()
