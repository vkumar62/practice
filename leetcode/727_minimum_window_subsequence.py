import pdb
class Solution:
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
       
        pdb.set_trace()
        minlen = float('inf')
        minrange = (-1, -1)
        
        for k in range(len(S)):
            if S[k] == T[0]:
                i = k
                j = 0
                while i < len(S) and j < len(T):
                    if S[i] == T[j]:
                        #i += 1
                        j += 1
                    i += 1
                if j == len(T) and minlen > i-k:
                    minlen = i - k
                    minrange = (k, i)
        if minlen != float('inf'):
            return S[minrange[0]:minrange[1]]
        return ""
        

S, T = "abcdebdde", "bde"
print(Solution().minWindow(S, T))
