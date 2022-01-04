class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combArr = nums1 + nums2
        sortArr = sorted(combArr)
        print(sortArr)

        sizeArr = len(sortArr)

        if(sizeArr%2 == 1):
            return float(sortArr[sizeArr//2])

        else:
            return float(((sortArr[sizeArr//2]) + sortArr[(sizeArr//2) - 1]) / 2)

        