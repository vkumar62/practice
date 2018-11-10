
# WRONG WRONG
#Return the count of longest increasing subsequence in array A
# Time - O(len(A))
# Space - O(1)
def lis(A):
    count_till_here = 1
    max_count = 0
    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            count_till_here += 1
        else:
            count_till_here = 1
        max_count = max(max_count, count_till_here)
    return max_count

print(lis([10,9,2,5,3,7,101,18]))
