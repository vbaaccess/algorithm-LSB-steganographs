class Stenography:
    def __init__(self, filename: str):
        self.filename = filename
        self.hidden_text = ''
        self.search_message()

    def search_message(self):
        # pic = np.array(io.imread(self.filename))
        # print('len(pic)', len(pic))
        # print('pic.size', pic.size)

        with open(self.filename, "rb") as f:
            a = f.read()

        #print(type(a))
        #print(len(a))

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


        # image_height = len(pic.size[0])
        # image_width = len(pic.size[0][0])
        #
        # print('image_height', image_height)
        # print('image_width', image_width)

        # z_max = pic.size[2]
        #
        # for x in range(x_max):
        #     for y in range(y_max):
        #         for z in range(z_max):
        #             print("<x,y,z> = <{},{},{}>: TO DO ".format(x,y,z))

        #print("<x,y,z> = <{},{},{}>: {} ".format(1, 2, 3, 'TEST'))
        #print("<x,y> <r,g,b,alfa> = <{},{}> <{},{},{},{}>: {} ".format(0, 0, pic[0][0][0],pic[0][0][1], pic[0][0][2], pic[0][0][3], 'TO DO'))

        # count = 0
        # lsb_chr = ''
        # lsb = ''
        # stop = False
        # for row in pic:
        #     if stop:
        #         break
        #     for pixel in row:
        #         if stop:
        #             break
        #         #print('pixel =>', pixel)
        #         for bit_field in pixel:
        #             if stop:
        #                 break
        #             #print('bit_field = >', bit_field, bin(bit_field))
        #             #lsb_chr += (str(bin(bit_field))[-1::])
        #             lsb_chr += (str(bin(bit_field))[-1::])
        #             if len(lsb_chr)>7:
        #                 #print('lsb',lsb)
        #                 int_lsb_chr = int(lsb_chr, 2)
        #                 #if int_lsb_chr != 255:
        #                 #if (int_lsb_chr >= 32) and (int_lsb_chr <= 126):
        #                 if (int_lsb_chr >= 65) and (int_lsb_chr <= 90):
        #                     print('lsb -> int, ascii', int_lsb_chr, chr(int_lsb_chr))
        #                     lsb += chr(int_lsb_chr)
        #                     if lsb[-3::] == 'EOF':
        #                         stop = True
        #                 lsb_chr = ''
        # self.hidden_text = lsb

        # count = 0
        # secret_bit = ''
        # for row in pic:
        #     for col in row:
        #         for pix in col:
        #             count += 1
        #             print(count, pix, bin(pix))
        #             secret_bit += str()

        #     count += 1
        #     print(bit)
        #     if count > 0:
        #         break

    def __call__(self):
        return self.hidden_text


def extract_message(filename: str) -> str:
    st = Stenography(filename)
    secret_information = st()
    return secret_information


# tests
print(extract_message('white-small.bmp'))
#print(extract_message('white.bmp'))
#print(extract_message('lenna.bmp'))
print(extract_message('garden.bmp'))