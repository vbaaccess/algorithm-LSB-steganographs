import struct

class Steganography:
    def __init__(self, filename: str):
        self.filename = filename
        self.hidden_text = ''
        self.search_message()

    def search_message(self):
        with open(self.filename, "rb") as f:
            bmp_array = f.read()

        offset_bits = [bmp_array[10], bmp_array[11], bmp_array[12], bmp_array[13]]
        file_offset = struct.unpack("I", bytearray(offset_bits))
        pixel_array_begin = file_offset[0]-8

        lsb_chr = ''
        lsb_str = ''
        for i in range(len(bmp_array)):
            if i >= pixel_array_begin:
                lsb_chr += bin(bmp_array[i])[-1::]
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
