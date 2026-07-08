from typing import List

def candies(ratings: List[int]) -> int:
    n = len(ratings)
    if n == 0:
        return 0

    candies = [1] * n # initialising for condition 1

    # left to right pass : increasing, child > left_neighbor, starting at index 1, since 0 has no left neighbor
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i-1] + 1
    # right to left pass : decreasing, child > right_neighbor, starting at index n-1, since index n-1 has no right neighbor
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)