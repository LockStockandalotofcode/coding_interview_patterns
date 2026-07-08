def longest_palindrome_in_a_string(s: str) -> str:
    n = len(s)
    # base case
    if n == 0:
        return ""
    # base case of dp adjacency matrix, with cell [i][j] representing if substr from index: i to j, palindorme or not
    # if strng is 1-character long, then its a palindrome
    longest_len = 1
    start_idx = 0
    dp = [[False]*n for _ in range(n)]
    # for len = 1, all substrings are palindromes
    for i in range(n):
        dp[i][i] = True
    # for len = 2, all substrings are palindromes that have both characters same
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True 
            longest_len = 2
            start_idx = i
    
    # traversal: like a sliding window, with window length increasing from 3, 4, 5, ...
    for substring_len in range(3, n+1):
        # sliding the window of length i : start to end, i to j window of len = substring_len
        for i in range(n - substring_len + 1):
            # j - i + 1 = substring_len
            j = i - 1 + substring_len

            # check if palindrome through recursive relation, and above memoization through adj matrix
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                longest_len = substring_len
                start_idx = i
    
    return s[start_idx : start_idx + longest_len] # but stop slice is not included, so s[start_idx : start_idx + longest_len], instead of s[start_idx : start_idx - 1 + longest_len]