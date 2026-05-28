class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        freq = [[] for i in range(len(nums)+1)]
        result = []

        for num in nums:
            countMap[num] = 1 + countMap.get(num,0)

        for key,val in countMap.items():
            freq[val].append(key)

        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result


                                                        

        