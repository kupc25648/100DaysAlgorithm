'''
Anytime data is transferred or stored, there are errors occurring which leads to data corruption. Computer memory, disk, ethernet, wi-fi, … it happens everywhere. Hamming code was an impressive discovery of how to deal with the problem efficiently.

To identify errors, we may double each bit. Instead of 1010 we can store 11001100. If a pair of consecutive bits doesn’t match, data is corrupted. That is called parity.

But doubling is not enough. We can identify there’s an error but we can’t recover. Hence we have to triple the data. Having 111000111000 we can identify corrupted triplets and let the triplet vote for majority to reconstruct the original.

However, for each bit of data this approach requires additional 2 bits. If we expect an error to occur not more than once out of 255 bits, that’s just wasting.

Hamming’s idea is the following. For 255 bits we need 8 bits as address space. We can store 247 bits of data and only use 8 bits for parity checks.

Each parity bit covers positions that have certain bit set to 1 in its address. For example parity bit P1 checks only addresses with mask xxx1, P2 checks only addresses xx1x, P4 checks only addresses x1xx, etc.

If an error occurs, only parities targeting the corrupted bit are set to 1 and form an address to exact location.
'''
import numpy as np
# Algorithm
def encode(parity_bits, data):
    n = len(data) + parity_bits
    assert 2 ** parity_bits == n + 1
    # copy data to code
    code = np.zeros(n, dtype=int)
    code[np.arange(n) & np.arange(n) + 1 > 0] = data
    # parity mask
    mask = np.zeros(n, dtype=int)
    mask[::2] = 1
    # compute parity
    i = 0
    while i < n:
        code[i] = code[i:][mask == 1].sum() & 1
        i += i + 1
        mask = np.repeat(mask, 2)[:n - i]
    # result
    return code
def decode(code):
    n = len(code)
    # parity mask
    mask = np.zeros(n, dtype=int)
    mask[::2] = 1
    # compute parity
    error, i = -1, 0
    while i < n:
        error += (i + 1) * (code[i:][mask == 1].sum() & 1)
        i += i + 1
        mask = np.repeat(mask, 2)[:n - i]
    # fix error
    if error >= 0:
        code[error] ^= 1
    # get data from code
    data = code[np.arange(n) & np.arange(n) + 1 > 0]
    # result
    return error, data
# Run
parity_bits = 3
data = np.random.randint(0, 2, 4)

# generate code
code = encode(parity_bits, data)
print('hamming code', data, '->', code)

# make error
code[3] ^= 1
print('with error', code)

# reconstruct
error, recon = decode(code)
print('error @', error, '->', recon)
