#L04 - steganography (Pyloop)

# W plikach *.bmp zaszyte zostały wiadomości tekstowe (w każdym pliku inna).
# Uzupełnij funkcję `extract_message` tak, aby przujmując nazwę pliku zwracała
# wiadomość w nim zakodowaną.

# Przydatne linki:
# https://en.wikipedia.org/wiki/Steganography
# https://en.wikipedia.org/wiki/BMP_file_format
# https://www.geeksforgeeks.org/check-whether-k-th-bit-set-not
#
# Przydatne metody / operatory:
# https://docs.python.org/3.8/library/stdtypes.html#int.from_bytes
# https://docs.python.org/3.8/library/stdtypes.html#int.to_bytes
# https://docs.python.org/3.8/library/stdtypes.html#bytes
# https://wiki.python.org/moin/BitwiseOperators
#
# Podpowiedź: W pliku `white-small.bmp` zaszyta jest wiadomość `TESTEOF`.
#from os import getcwd
import array
import os
import numpy as np
from skimage import io
import struct
import matplotlib.pyplot as plt

# class ImageInfo:
#     def __init__(self, filename):
#         self.filename = filename
#         self.getInfo()
#
#     def __call__(self, x):
#         self.wyliczWynik(x)
#         return self.result
#     def _getInfo(self):

class Steganography:
    def __init__(self, filename: str):
        self.filename = filename
        self.hidden_text = ''
        self.file_analyze()

    def __call__(self):
        return self.hidden_text

    def file_analyze(self):
        full_path_to_file = os.getcwd() + "\\" + self.filename
        print('1) open:',full_path_to_file)
        count = 0
        # with open(str(self.filename),"rb") as f:
        #     for line in f:
        #         count += 1
        #         print("line {}: {}".format(count,line.strip()))

        pic = np.array(io.imread(full_path_to_file))
        print('len(pic)', len(pic))
        print (pic.size)

        # for bt in pic:
        #     count += 1
        #     print(bt)
        #     if count>12:
        #         break

        # lst = pic.tolist()

        lst = []
        for bt in pic:
            lst.append(bt)

        for bt in lst:
            count += 1
            print(bt)

        print('count', count)

        # plt.imshow(pic)
        # plt.show()

        # with open(str(self.filename),"rb") as f:
        #     #print(imghdr.what(self.filename))
        #     lst_bit = f.read()
        #     print('type(lst_bit)', type(lst_bit))
        #     print('len(lst_bit)', len(lst_bit))
        # if len(lst_bit)>0:
        #     for b in lst_bit:
        #         count += 1
        #         #print("Lp({}): {} => {} =ASCII=> {}".format(count, b, bin(b), chr(b)))
        #         if self.check_bit_state(b):
        #             print("Lp({}): {} => {} =ASCII=> {}".format(count, b, bin(b), chr(b)))
        # self.hidden_text = 'steganography class test =>' + str(self.hidden_text)

    # default chek last bit (8th)

    def check_bit_state(self, check_int: int,bit_position_to_check: int = 1) -> bool:
        #print(" - check {} bit in int {} (binary: {})".format(bit_position_to_check, check_int, bin(check_int)))
        bit_state  = False
        if check_int & (1 << (bit_position_to_check - 1)):
            bit_state = True
        return bit_state

def extract_message(filename: str) -> str:
    print_info = True
    st = Steganography(filename)
    secret_information = st()
    if print_info:
        print(30 * '-', 'steganography (Pyloop)', 30 * '-')
        print('file path: ', os.getcwd())
        print('test file: ', filename)
        print('secret information: ', secret_information)
        print(80 * '-')
    return secret_information



print(extract_message('white-small.bmp'))
#print(extract_message('garden.bmp'))