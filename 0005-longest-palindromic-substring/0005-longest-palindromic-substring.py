class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, max_len = 0, 1

        def expand(left: int, right: int) -> None:
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left+1, right-1 is the actual palindrome bounds
            curr_len = right - left - 1
            if curr_len > max_len:
                max_len = curr_len
                start = left + 1

        for i in range(len(s)):
            expand(i, i)       # odd-length palindrome centered at i
            expand(i, i + 1)   # even-length palindrome centered between i, i+1

        return s[start:start + max_len]