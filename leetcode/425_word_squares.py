import pdb

import collections

class Solution:
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        
        def form_word_square(word_square):
            len_ws = len(word_square)
            if len_ws == M:
                result.append(word_square)
                return
            
            s = (word_square[x][len_ws] for x in range(len_ws))
            for candidate_word in worddict[''.join(s)]:
                form_word_square(word_square + [candidate_word])
        
        #pdb.set_trace()
        if not words:
            []
            
        M = len(words[0])
        
        #worddict = set(words)
        #preprocess the words by keeping list of prefixes
        worddict = collections.defaultdict(list)
        for word in words:
            for i in range(1, len(word)):
                worddict[word[:i]].append(word)


        result = []
        
        for word in words:
            form_word_square([word])
            
        return result

#words = ["area","lead","wall","lady","ball"]
words = ["abat","baba","atan","atal"]
print(Solution().wordSquares(words))
