# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import namedtuple

LongestPath = namedtuple("LongestPath", ["with_root", "without_root"])

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def longestUnivaluePath_helper(node):
            if not node:
                return LongestPath(0, 0)
            
            with_root = 1
            without_root = 0
            left = right = None
            
            if node.left:
                left = longestUnivaluePath_helper(node.left)                   
            
            if node.right:
                right = longestUnivaluePath_helper(node.right)
                    
            if node.left and node.left.val == node.val and node.right and node.right.val == node.val:
                without_root = max(left.without_root, right.without_root, left.with_root + right.with_root + 1)
                with_root = 1 + max(left.with_root, right.with_root)
            
            if node.left and node.left.val == node.val:
                with_root = max(with_root, 1+left.with_root)
            if node.right and node.right.val == node.val:
                with_root = max(with_root, 1+right.with_root)
            if node.left:
                without_root = max(without_root, left.without_root, left.with_root)
            if node.right:
                without_root = max(without_root, right.without_root, right.with_root)
            
            return LongestPath(with_root, without_root)
        if not root:
            return 0
        
        import pdb
        pdb.set_trace()
        result = longestUnivaluePath_helper(root)
        return max(result)-1

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);
            
            ret = Solution().longestUnivaluePath(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
