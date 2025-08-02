import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heap.append(-n)
        heapq.heapify(heap)
        res = []
        for i in range(k):
            res.append(-(heapq.heappop(heap)))
        
        return res[-1]