class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
           totalsize = len(digits)
           i = -1
           neg = -totalsize
           resultdigits = digits[:]
           while i >= neg :
             sum = resultdigits[i] +1
             if sum == 10:
               resultdigits[i] = 0
               if i == neg :
                 resultdigits.insert(0,1)
                 return resultdigits
               i = i- 1
             else:
               resultdigits[i] = sum
               return resultdigits