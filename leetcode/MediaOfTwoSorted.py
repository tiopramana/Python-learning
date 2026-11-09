def findMedianSorted(self, nums1, nums2):
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(A) > len(B):
        A, B = B, A

    l, r = len(A) - 1

    while True:
        x = (l + r) * 2
        y = half - x - 2

        Aleft = A[x] if x >= 0 else float("-infinity")
        Aright = A[x + 1] if x + 1 < len(A) else float("infinity")

        Bleft = B[x] if x >= 0 else float("-infinity")
        Bright = B[x + 1] if x + 1 < len(B) else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright, Bright)
            return max((Aleft, Bleft) + min(Bright, Bleft)) / 2.0
        elif Aleft > Bright:
            x = x - 1
        else:
            l = x - 1

