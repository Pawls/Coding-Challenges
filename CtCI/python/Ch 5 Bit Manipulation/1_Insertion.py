# Lambda experimentation
# returns a summation of powers of two in sequence
# twos = lambda a: 2**a + twos(a-1) if a > 0 else 2**a

def clear_bit_range(num, length, offset):
    # Generates a binary sequence of 1's, padded by 0's
    mask = ((1 << length + offset) - 1) ^ ((1 << offset) - 1)

    # Invert all bits in mask
    mask ^= ~0
    
    return num & mask

def insert_binary(big_bin, small_bin, i, j):
    clear_bin = clear_bit_range(big_bin, j - i, i)
    print('Big  ',bin(big_bin))
    print('Small',bin(small_bin))
    print('Insert small into big, offset by',i,'from the LSB')
    return bin(clear_bin | (small_bin << i))


# 0b111111111111111 is 2047
# 0b01010 is 10
print(insert_binary(2047,10, 2, 5))
print()

print(insert_binary(0b10000000000,0b10011, 3, 8))
print()

print(insert_binary(0b1111111111,0b1000, 3, 7))
