from sortedcontainers import SortedList

class Solution(object):
    def kEmptySlots(self, flowers, k):
        active = SortedList()
        for day, flower in enumerate(flowers, 1):
            i = active.bisect_left(flower)
            for neighbor in active[i-(i>0):i+1]:
                if abs(neighbor - flower) - 1 == k:
                    return day
            active.add(flower)
        return -1

flowers, k = [1,3,2], 1
print(Solution().kEmptySlots(flowers,k))
