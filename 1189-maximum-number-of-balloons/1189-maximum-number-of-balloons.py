class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        # "balloon" -> b:1, a:1, l:2, o:2, n:1
        needed = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}

        return min(count[char] // req for char, req in needed.items())