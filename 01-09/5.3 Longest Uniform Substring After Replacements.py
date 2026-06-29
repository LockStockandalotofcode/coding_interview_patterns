def longest_uniform_substring_after_replacements(s: str, k: int) -> int:
    # DYNAMIC SLIDING
    # 2 SCENARIOS
    # SLIDE - WHEN REPLACEABLE_CHARS > K
    # EXPAND - WHEN REPLACEABLE_CHARS <= K

    # REPLACEABLE_CHARS = LENGTH OF WINDOW - UNIQUE CHARACTERS

    freqs = {}
    highest_freq = max_len = 0
    left = right = 0

    while right < len(s):
        # update freq of right pointer
        # highest freq
        freqs[s[right]] = freqs.get(s[right],0)  + 1
        highest_freq = max(highest_freq, freqs[s[right]])

        # calculate no. of replacements
        len_substr = right - left + 1
        replacements = len_substr - highest_freq

        # if condition valid : expand
        # else : slide
        if replacements > k:
            freqs[s[left]] -= 1
            left += 1
        max_len = right - left + 1
        right += 1

    return max_len