W plikach *.bmp zaszyte zostały wiadomości tekstowe (w każdym pliku inna).
Uzupełnij funkcję `extract_message` tak, aby przujmując nazwę pliku zwracała
wiadomość w nim zakodowaną.

* Wiadomość znajduje się w bajtach odpowiadających pixelom obrazka.
* Wiadomość składa się ze znaków z tabeli ASCII.
* Do ukrycia wiadomości wykorzystano LSB powyższych bajtów.
* Każdy pixel składa się z 4 bajtów.
* Każdy znak ukrytej wiadomości reprezentowany jest jako 1 bajt (8 bitów).
* Każdy znak ukrytej wiadomości zajmuje 2 pixele, 2 * 4 bajty = 8 bajtów (1 bajt na 1 bit znaku).
* LSB pierwszego bajtu pierwszego z pary pixeli staje sie MSB ukrytego znaku.
* Wiadomość kończy się ciągiem 'EOF'.
* Pomimo iż znaki z tabeli ASCII zajmują 7 bitów, do zakodowania znaków wykorzystano 8 bitów.
  Można więc założyć, że MSB znaku jest zawsze równy 0.

Przykład:

Dla dwóch kolejnych pixeli odczytanych z pliku:
pixel 1 - 254 255 254 255
pixel 2 - 254 255 254 254

Otrzymujemy ciąg 8 bajtów:
254 255 254 255 254 255 254 254

W reprezentacji bitowej wygląda to następująco:
0b11111110 0b11111111 0b11111110 0b11111111 0b11111110 0b11111111 0b11111110 0b11111110

Po wyodrębnieniu LSB ze wszystkich bajtów i połączeniu w 1 bajt otrzymujemy:
0b01010100
Co odpowiada znakowi `T` w tabeli ASCII

Przydatne linki:
https://en.wikipedia.org/wiki/Steganography
https://en.wikipedia.org/wiki/BMP_file_format
https://www.geeksforgeeks.org/check-whether-k-th-bit-set-not

Przydatne metody / operatory:
https://docs.python.org/3.8/library/stdtypes.html#int.from_bytes
https://docs.python.org/3.8/library/stdtypes.html#int.to_bytes
https://docs.python.org/3.8/library/stdtypes.html#bytes
https://wiki.python.org/moin/BitwiseOperators

Podpowiedź: W pliku `white-small.bmp` zaszyta jest wiadomość `TESTEOF`.