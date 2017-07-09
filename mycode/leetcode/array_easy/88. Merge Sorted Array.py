class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        i = m - 1
        j = n - 1
        k = len(nums1)-1
        if k < i + j:
            return False

        while i > -1 and j > -1:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
        if j != -1:
            while j > -1:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1



if __name__ == "__main__":
    nums1 = [1,0]
    m = 1
    nums2 = [2]
    n = 1
    s = Solution()
    print s.merge(nums1, m, nums2, n)