def longest_substring_with_unique_chars(s: str) -> int:
    # DYNAMIC SLIDING
    # MAINTAIN A HASHMAP (OPTIMIZED) OF ALL UNIQUE CHARACTERS, ONCE DUPICATE CHARACTER FOUND, JUMP LEFT INDEX TO NEXT TO PREV DUPLICATE'S INDEX
    # IF NEW CHARACTER IS UNIQUE, EXPAND, OTHERWISE SHRINK AS PER ABOVE

    left = right = 0

    max_len = 0
    hashmap = {} # CHARACTER -> INDEX

    while right < len(s):
        if s[right] in hashmap and hashmap[s[right]] >= left:
            left = hashmap[s[right]] + 1
        new_window_len = right - left + 1
        max_len = max(max_len, new_window_len)
        hashmap[s[right]] = right
        right += 1
    
    return max_len