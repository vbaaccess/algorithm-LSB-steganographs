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

def extract_message(filename: str) -> str:
    return ""