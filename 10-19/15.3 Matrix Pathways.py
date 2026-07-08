def matrix_pathways(m: int, n: int) -> int:
    dp = [[1]*n for _ in range(m)]
    # setting base case row 0, column 0 to 1, in initialisation only
    
    # bottom up
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]