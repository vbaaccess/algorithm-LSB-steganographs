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


class Steganography:
    def __init__(self, filename: str):
        self.filename = filename
        self.hidden_text = ''
        self.search_message()

    def search_message(self):
        with open(self.filename, "rb") as f:
            a = f.read()

        lsb_chr = ''
        lsb_str = ''
        for i in range(len(a)):
            if i > 129:
                lsb_chr += bin(a[i])[-1::]
                if len(lsb_chr)>7:
                    int_chr = int(lsb_chr, 2)
                    lsb_str += chr(int_chr)
                    if lsb_str[-3::] == 'EOF':
                        break
                    lsb_chr = ''
        self.hidden_text = lsb_str[1::]

    def __call__(self):
        return self.hidden_text


def extract_message(filename: str) -> str:
    st = Steganography(filename)
    secret_information = st()
    return secret_information


# tests
print(extract_message('white-small.bmp'))
print(extract_message('white.bmp'))
print(extract_message('lenna.bmp'))
print(extract_message('garden.bmp'))