def longest_common_subsequence(s1: str, s2: str) -> int:
    # 2D dp table 
    # base case get coded into dp table
    l1 = len(s1)
    l2 = len(s2)
    prev_row = [0 for _ in range(l2 + 1)]

    for s1_char_idx in range(l1 - 1, -1, -1):
        curr_row = [0 for _ in range(l1 + 1)]
        for s2_char_idx in range(l2 - 1, -1, -1):
            # chars same 
            if s1[s1_char_idx] == s2[s2_char_idx]:
                curr_row[s2_char_idx] = 1 + prev_row[s2_char_idx + 1]
            # chars different
            else:
                curr_row[s2_char_idx] = max(curr_row[s2_char_idx + 1], prev_row[s2_char_idx])
        prev_row = curr_row
    
    return prev_row[0]