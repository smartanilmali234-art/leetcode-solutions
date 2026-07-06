class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        total_len = len(nums1) + len(nums2)
        
        def get_kth(a_start, b_start, k):
            if a_start >= len(nums1): return nums2[b_start + k - 1]
            if b_start >= len(nums2): return nums1[a_start + k - 1]
            if k == 1: return min(nums1[a_start], nums2[b_start])
            
            half = k // 2
            mid_a = nums1[a_start + half - 1] if a_start + half <= len(nums1) else float('inf')
            mid_b = nums2[b_start + half - 1] if b_start + half <= len(nums2) else float('inf')
            
            if mid_a < mid_b:
                return get_kth(a_start + half, b_start, k - half)
            else:
                return get_kth(a_start, b_start + half, k - half)

        if total_len % 2 == 1:
            return float(get_kth(0, 0, total_len // 2 + 1))
        else:
            left_mid = get_kth(0, 0, total_len // 2)
            right_mid = get_kth(0, 0, total_len // 2 + 1)
            return (left_mid + right_mid) / 2.0      