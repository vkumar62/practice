class TrieNode:
    def __init__(self):
        self.children = dict()
        self.index = -1

class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        
        def create_trie():
            root = TrieNode()
            # Create trie of the words
            for i, word in enumerate(words):
                cur = root
                for c in word:
                    if c not in cur.children:
                        cur.children[c] = TrieNode()
                    cur = cur.children[c]
                cur.index = i
                
            return root
        
        def is_palindrome(s):
            left = 0
            right = len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        import pdb
        pdb.set_trace()

        root = create_trie()
        results = []
        
        for i, word in enumerate(words):
            # Check if the reverse of the word exists in the trie
            cur = root
            # Special case for ''
            if root.index != -1 and is_palindrome(word):
                results.append([root.index, i])
            remaining_word = ''
            for k in reversed(range(len(word))):
                c = word[k]
                if c not in cur.children:
                    remaining_word = word[:k+1]
                    break
                cur = cur.children[c]
            if cur.index != -1 and cur.index != i and is_palindrome(remaining_word):
                # Now check if the start of the word until c forms a palindrome
                results.append([cur.index, i])
            
        return results
       
#words = ["abcd","dcba","lls","s","sssll"] 
words = ["a",""]
print(Solution().palindromePairs(words))
