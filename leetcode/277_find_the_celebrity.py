# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
import pdb
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        celebs = set(range(n))
       
        pdb.set_trace()
        while len(celebs) > 1:
            a = celebs.pop()
            b = celebs.pop()
            if knows(a, b):
                # a cannot be a celeb since a knows someone
                celebs.add(b)
            else:
                # b cannot be a celeb since b is not known by someone
                celebs.add(a)
        
        if len(celebs) == 1:
            celeb = celebs.pop()
            for num in range(n):
                if num != celeb and (knows(num, celeb) == False or knows(celeb, num) == True):
                    return -1
            return celeb
        return -1
        

def knows(a, b):
    if a == 0 and b == 1:
        return True
    return False

print(Solution().findCelebrity(2))
