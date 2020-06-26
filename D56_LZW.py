'''
Lempel-Ziv-Welch, or LZW, is a dictionary-based compression algorithm from LZ family of algorithms.
The idea behind is cute. And even though its performance was heavily outperformed by other algorithms, I still consider it as one of the most clever techniques.

LZW iteratively builds a (code, word) dictionary as it reads input data. At the beginning, the whole alphabet is inserted and hence needs not to be stored to output.
Input is then matched to the longest known word in dictionary and its code is sent to output. The word extended by the next input character is stored as a new entry.
This technique is fast as it needs no extra search inside large blocks. And unlike my implementation with dict, it just needs an array with pointers.
However, major flaw of the algorithm are the dictionary codes. To store the code, we have to periodically enlarge number of bits from 9 up to 12 or 16. At this point, dictionary is usually erased and algorithm starts over.
That empowers its weakness — the dictionary is built very slowly. Once it contains enough information to compress efficiently, it is erased. But allowing larger size is tricky due to long codes and decrease in performance.
I’ve inserted only encoding portion of code in here, check the notebook for decoder.

'''

# Algorithm
def lzw_encode(data):
    code, code_bits = {bytes([i]): i for i in range(256)}, 8
    buffer, buffer_bits = 0,0
    index, aux = 0, []

    while index < len(data):
        # find word
        for j in range(index +1, len(data)+1):
            word = data[index:j]

            # store word
            if word not in code:
                code[word] = len(code)
                word = word[:-1]
                break

        # write buffer
        buffer <<= code_bits
        buffer |= code[word]
        buffer_bits += code_bits

        # code length
        if len(code) > 2**code_bits:
            code_bits +=1

        # shift
        index += len(word)

        # buffer alignment
        if index >= len(data) and buffer_bits%8:
            r = 8 -(buffer_bits%8)
            buffer <<= r
            buffer_bits += r

        # emit output
        if not buffer_bits%8:
            aux += int.to_bytes(buffer, buffer_bits >> 3, 'big')
            buffer, buffer_bits = 0,0

    return bytes(aux)

def lzw_decode(data):
    code, code_bits = {i: bytes([i]) for i in range(256)}, 8
    buffer, buffer_bits = 0, 0
    index, aux = 0, []
    prefix = b''

    while index < len(data) or buffer_bits >= code_bits:
        # read buffer
        while index < len(data) and buffer_bits < code_bits:
            buffer <<= 8
            buffer |= data[index]
            buffer_bits += 8
            index += 1

        # find word
        buffer_bits -= code_bits
        key = buffer >> buffer_bits
        buffer &= (1 << buffer_bits) - 1
        word = code.get(key, prefix + prefix[:1])

        # store word
        if prefix:
            code[len(code)] = prefix + word[:1]
        prefix = word

        # code length
        if len(code) >= 2 ** code_bits:
            code_bits += 1

        # emit output
        aux += word

    return bytes(aux)

# Run
def compress(data):
    encoded = lzw_encode(data.encode('ASCII'))
    decoded = lzw_decode(encoded).decode('ASCII')
    assert data == decoded

    print('compression', len(data), '->', len(encoded), 'bytes')

compress('ATGATCATGAG')
