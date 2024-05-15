class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z가-힣0-9]", "", s.lower())
        return s == ''.join(reversed(s))