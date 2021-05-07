
def encrypt(file_hash):
    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '(', ')']

    binary = bin(int(file_hash, 16))[2:]
    # print(len(binary), 6-len(binary)%6)
    if 6-(len(binary)%6)!=6:
        binary = "0"*(6-(len(binary)%6)) + binary
    # print(len(binary))
    data = ""

    for i in range(0, len(binary), 6):
        segment = binary[i:i+6]
        # print(int(segment, 2), end= " ")
        # print(segment, end= " ")
        data += arr[int(segment, 2)]
    
    return data

def decrypt(data):
    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '(', ')']

    file_hash = ""
    
    for i in data:
        index = arr.index(i)
        segment = "{0:06b}".format(index)
        # print(index, end=" ")
        # print(segment, end= " ")
        file_hash += segment.strip()
    # print(len(file_hash))
    file_hash = hex(int(file_hash, 2))[2:]

    return file_hash

# x = encrypt("1aceb2f20a220dcc7fa934084c948ee45df89eb9a502cba62d0fca730c887fb4")
# print(x)
# print(decrypt(x))