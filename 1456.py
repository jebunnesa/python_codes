class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if len(s) == k:
            return k
        vowels = ['a', 'e', 'i', 'o', 'u']
        max_frqency = 0
        top_max_f = 0
        for i in range(len(s)):
            if i < k:
                if s[i] in vowels:
                    max_frqency += 1
            else:
                top_max_f = max(top_max_f,max_frqency)
                if s[i-k] in vowels:
                    max_frqency -= 1
                if s[i] in vowels:
                    max_frqency += 1
        top_max_f = max(top_max_f, max_frqency)
        return top_max_f


obj = Solution()
print(obj.maxVowels("abciiidef", 3))
print(obj.maxVowels("leetcode", 3))
print(obj.maxVowels("ae", 2))
print(obj.maxVowels("weallloveyou", 7))