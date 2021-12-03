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
            if i > 1:
                lsb_chr += bin(a[i])[-1::]
                if len(lsb_chr)>7:
                    int_chr = int(lsb_chr, 2)
                    if (int_chr >= 32) and (int_chr <= 126):
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
#print(extract_message('white-small.bmp'))
#print(extract_message('white.bmp'))
print(extract_message('lenna.bmp'))
#print(extract_message('garden.bmp'))