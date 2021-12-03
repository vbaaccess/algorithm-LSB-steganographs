import os
#from PIL import Image

class Stenography:
    def __init__(self, filename: str):
        self.filename = filename
        self.hidden_text = ''
        self.search_hidden_message()

    def search_hidden_message(self):
        count =0
        img = Image.open(self.filename)
        imgWidth, imgHeight = img.size
        imgdata = img.getdata()

        x_pos = 0
        y_pos = 1

        pixel_value = []
        x = []
        y = []

        for item in imgdata:
            if (x_pos) == imgWidth:
                x_pos = 1
                y_pos += 1
            else:
                x_pos += 1

            if item[3] != 0:
                pixel_value.append(item[2])
                x.append(x_pos)
                y.append(y_pos)

        lsb_chr = ''
        lsb_str = ''
        for pixel in pixel_value:
            lsb_chr += (str(bin(pixel))[-1::])
            if len(lsb_chr) > 7:
                int_chr = int(lsb_chr, 2)
                if (int_chr >= 32) and (int_chr <= 90):
                    lsb_str += chr(int_chr)
                    if lsb_str[-3::] == 'EOF':
                        break
                lsb_chr = ''

        self.hidden_text = lsb_str[1::]
        #print('pixel_value',pixel_value)
            # for line in f:
            #     count+=1
            #     stripped_lien = line.strip()
            #     print(count, stripped_lien)

    def __call__(self):
        return self.hidden_text


def extract_message(filename: str) -> str:
    st = Stenography(filename)
    secret_information = st()
    secret_information = secret_information[3::]
    return secret_information


# tests
print(extract_message('white-small.bmp'))
#print(extract_message('white.bmp'))
#print(extract_message('lenna.bmp'))
#print(extract_message('garden.bmp'))