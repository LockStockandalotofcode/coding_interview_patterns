from typing import Tuple

def longest_palindrome_in_a_string(s: str) -> str:
    n = len(s)
    # base case
    if n == 0:
        return ""
    # if strng is 1-character long, then its a palindrome
    longest_len = 1
    start_idx = 0

    def expand_palindrome(left: int, right: int) -> Tuple[int, int]:
        # we can do check for previous if we start with 2 center length in case of even
        # strings, palindrome
        # this algo first checks if next expansion leads to a palindrome or not, then only updates the palindrome length, expanding its indices
        while left > 0 and right < n - 1 and s[left - 1] == s[right + 1]:
            left -= 1
            right += 1
        
        return left, right - left + 1

    # optimised approach: expanding from center to get length of palindrome, traversing through entire string for odd-length and even-length palindromes
    for center in range(n):
        # starting with base case of len 1, 2
        # odd length palindromes
        odd_start, odd_len = expand_palindrome(center, center)
        if odd_len > longest_len:
            start_idx = odd_start
            longest_len = odd_len

        # even length palindromes
        if center < n-1 and s[center] == s[center + 1]:
            even_start, even_len = expand_palindrome(center, center + 1)
            if even_len > longest_len:
                start_idx = even_start
                longest_len = even_len
    
    return s[start_idx : start_idx + longest_len]