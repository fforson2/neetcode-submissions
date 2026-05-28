class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countMap = {}
        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)


        freq = [[] for i in range(len(nums) + 1)]


        for key, val in countMap.items():
            freq[val].append(key)

        result = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result

