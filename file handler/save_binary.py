with open('binary.bin', 'wb') as f:
    byte_list = bytes([255, 0, 127])
    f.write(byte_list)
