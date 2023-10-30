class Solution:
    def isPalindrome(self, x: int) -> bool:
        copia = [i for i in str(x)]
        return copia == copia[::-1]