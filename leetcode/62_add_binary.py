import pdb
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        pdb.set_trace()
        
        result = ''
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        
        while i >= 0 or j >= 0 or carry != 0:
            ai = aj = 0
            if i >= 0:
                ai = ord(a[i]) - ord('0')
            if j >= 0:
                bj = ord(b[j]) - ord('0')
            s = ai + bj + carry
            carry = s >> 1
            result = chr(ord('0')+(s&1)) + result
            i -= 1
            j -= 1
            
        return result
            
a = "1"
b = "111"
print(Solution().addBinary(a, b))
