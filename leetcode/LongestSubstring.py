def longestSubstring(s):

    l = 0
    longest = 0
    data = set()
    n = len(s)

    for r in range(n):
        while s[r] in data:
            data.remove(s[l])
            l += 1

        window = r - l + 1
        longest = max(longest, window)
        data.add(s[r])

    return longest
