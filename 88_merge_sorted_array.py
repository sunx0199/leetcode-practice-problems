def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    if m == 0:
        return nums2
        
    if n == 0:
        return nums1
        
    sorted = [0] * (m+n)
    i = 0
    j = 0 
    while i < m and j < n:
        idx = i + j
        if nums1[i] <= nums2[j]:
            sorted[idx] = nums1[i]
            i += 1
        else:
            sorted[idx] = nums2[j]
            j += 1
        
    if i < m:
        sorted[(idx+1):] = nums1[i:]
    if j < n:
        sorted[(idx+1):] = nums2[j:]

    return sorted
