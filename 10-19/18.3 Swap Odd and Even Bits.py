def swap_odd_and_even_bits(n: int) -> int:
    # 0 based indexing, where there is LSB at index 0

    # BIT MASKING
    # to isolate even or odd bits

    # These two hexadecimal values, 0x55555555 and 0xAAAAAAAA, are famous in computer science because they form alternating bit patterns. When converted to binary, they create a perfect chessboard-like sequence of 1s and 0s.

    even_mask = 0x55555555
    odd_mask = 0xAAAAAAAA

    even_bits = even_mask & n
    odd_bits = odd_mask & n

    res = (even_bits << 1) | (odd_bits >> 1)

    return res