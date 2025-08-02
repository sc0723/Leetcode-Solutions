from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for val, occ in freq.items():
            heap.append((-occ, val))
        
        heapq.heapify(heap)
        res = []
        for i in range(k):
            occ, val = heapq.heappop(heap)
            res.append(val)
        
        return res
