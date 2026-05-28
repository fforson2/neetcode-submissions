class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums)+ 1)]
        countMap = {}
        res = []


        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)

        for key,val in countMap.items():
            freq[val].append(key)

        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res


        