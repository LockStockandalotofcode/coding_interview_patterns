import heapq

class MedianOfAnIntegerStream:
    def __init__(self):
        self.left_half = []
        self.right_half = []

    def add(self, num: int) -> None:
        # using negative numbers to imitate max_heap, with default min_heap
        if not self.left_half or num <= -self.left_half[0]:
            heapq.heappush(self.left_half, -num)
            if len(self.left_half) > len(self.right_half) + 1:
                number = -heapq.heappop(self.left_half)
                heapq.heappush(self.right_half, number)
        else:
            heapq.heappush(self.right_half, num)
            if len(self.left_half) < len(self.right_half):
                number = -heapq.heappop(self.right_half)
                heapq.heappush(self.left_half, number)

    def get_median(self) -> float:
        if len(self.left_half) == len(self.right_half):
            return (-self.left_half[0] + self.right_half[0]) / 2.0
        return -self.left_half[0]