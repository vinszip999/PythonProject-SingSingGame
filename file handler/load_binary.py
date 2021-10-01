with open('binary.bin', 'rb') as f:
    data = f.read()  #b'\xff\x00\x7f': 111111110000000001111111
print(data)
