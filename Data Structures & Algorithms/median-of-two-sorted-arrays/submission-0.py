class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #Brute force
        #Merge the two arrays
        #sort and find median

        res = nums1 + nums2
        res.sort()
        n = len(res)

        #check for even or odd
        if n % 2 == 0:
            mid = n // 2
            return (res[mid] + res[mid - 1]) / 2


        else:
            mid = n // 2
            return res[mid]



    