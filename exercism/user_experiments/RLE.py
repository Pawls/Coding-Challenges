"""
Perform Run Length Encoding compression on a string.
"""


def compress(raw: str) -> bytes:
    """
    Compress the raw string to bytes using RLE.
    """
    if len(raw) == 0: return b''
    if len(raw) == 1: return bytes([1]) + bytes(raw[0], 'utf-8')
    res = b''
    i = 0
    raw = raw.encode('utf-8')
    while i < len(raw):
        count = 1
        if i < len(raw)-1:
            j = i+1
            while raw[j] == raw[i]:
                count += 1
                j += 1
                if j == len(raw):
                    break
            i = j - 1   
        res += bytes([count]) + bytes([raw[i]])
        i += 1
    return res

print(compress("\N{GRINNING FACE} \N{SHAMROCK}"))
print(compress("abb"))

# Example test case: "\N{GRINNING FACE} \N{SHAMROCK}"
# Output: b'\x01\xf0\x01\x9f\x01\x98\x01\x80\x01 \x01\xe2\x02\x98'
