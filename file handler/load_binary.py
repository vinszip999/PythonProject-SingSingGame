with open('text.bin', 'wb') as f:
    f.write(b'\xea\xb0\x80')  # 11101010_10110000_10000000

input()

with open('text.bin', 'r', encoding='utf-8') as f:
    data = f.read()  # b'\xff\x00\x7f': 111111110000000001111111
print(data)
