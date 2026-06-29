def substring_anagrams(s: str, t: str) -> int:
    len_s, len_t = len(s), len(t)
    if len_t > len_s:
        return 0

    # FIXED WINDOW
    count = 0
    exp_freq, window_freq = [0] * 26, [0] * 26

    # populate exp_freq hash map with that of t
    # ord() in python helps get ASCII code of alphabets
    for c in t:
        exp_freq[ord(c) - ord('a')] += 1
    
    left = right = 0
    while right < len_s:
        # expand window until full size reached
        # add new character to window_hashmap
        window_freq[ord(s[right]) - ord('a')] += 1
        # if window of full size, only slide
        if right - left + 1 == len(t):
            if window_freq == exp_freq:
                count += 1
            # remove leftmost character when sliding, before sliding
            window_freq[ord(s[left]) - ord('a')] -= 1
            # only then slide the winodw
            left += 1
        right += 1
    
    return count