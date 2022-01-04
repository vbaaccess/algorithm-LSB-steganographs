# algorithm-LSB-steganographs
Steganografi - Least Significant Bit algorithm

The example contains a solution to the problem of reading data embedded in other stakes (e.g. in graphic or musical files).

In the attached * .bmp files there are test messages hidden (different in each file).

 * The message is in bytes corresponding to the pixels of both pictures.
 * The message consists of characters from the ASCII table.
 * The LSB of the above bytes was used to hide the message.
 * Each pixel consists of 4 bytes.
 * Each character of the hidden message is represented as 1 byte (8 bits).
 * Each character of the hidden message takes 2 pixels, 2 * 4 bytes = 8 bytes (1 byte for 1 bit of character).
 * The LSB of the first byte of the first pixel pair becomes the MSB of the hidden character.
 * The message ends with 'EOF'.
 * Although the characters in the ASCII table are 7 bits long, 8 bits were used to encode the characters.
 Thus, it can be assumed that the MSB of the sign is always 0.

Example:
- for two consecutive pixels read from the file, we get a sequence of 8 bits:
  |    Pixel 1     |    Pixel 2     |
  |254 255 254 255 | 254 255 254 254|
  
  his representation bitwise and LSB:
     |    254        255        254        255        254        255        254       254    |
     |0b11111110 0b11111111 0b11111110 0b11111111 0b11111110 0b11111111 0b11111110 0b11111110|
  LSB|  .......0   .......1   .......0   .......1   .......0   .......1   .......0   .......0| => 0b01010100
  
  We transform the received string into an ASCII character
  
       bits   ==> decimal ==> ASCII
  | 0b01010100 |    84     |    T
  
  Useful links:
https://en.wikipedia.org/wiki/Steganography
https://en.wikipedia.org/wiki/BMP_file_format
https://www.geeksforgeeks.org/check-whether-k-th-bit-set-not
  
  Useful methods / operators:
https://docs.python.org/3.8/library/stdtypes.html#int.from_bytes
https://docs.python.org/3.8/library/stdtypes.html#int.to_bytes
https://docs.python.org/3.8/library/stdtypes.html#bytes
https://wiki.python.org/moin/BitwiseOperators
  
