def happy_number(n: int) -> bool:
    slow = fast = n
    while True:
        slow = next_number(slow)
        fast = next_number(next_number(fast))
        if fast == 1:
            return True
        elif fast == slow:
            return False

def next_number(x: int) -> int:
    next_num = 0
    while x > 0:
        digit = x % 10
        x //= 10
        next_num += digit ** 2
    return next_num