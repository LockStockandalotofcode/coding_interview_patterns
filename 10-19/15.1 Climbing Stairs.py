memo = {}

def climbing_stairs(n: int) -> int:
    if n <= 2:
        return n
    
    if n in memo:
        return memo[n]

    memo[n] = (
        climbing_stairs(n-1)+
        climbing_stairs(n-2)
    )

    return memo[n]