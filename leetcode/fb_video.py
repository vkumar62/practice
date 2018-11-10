"""Facebook's How to Crush Your Coding Interview. Problem: Write a function that given a string, returns all nearby words. You are given the following helper functions: Set<String> getNearbyChars(char c); isWord(String word);
"""

def get_nearby_words(word):
    def get_nearby_words_helper(index, partial):
        if index == len(word):
            if is_word(partial):
                results.append(partial)
            return

        for c in get_nearby_chars(word[index]):
            partial = partial[:index] + c + partial[index+1:]
            get_nearby_words_helper(index+1, partial)

    results = []
    partial = word
    get_nearby_words_helper(0, partial)
    return results



def get_nearby_chars(c):
    nearby_chars = { 'g':'ghf', 'i':'iok' }
    return nearby_chars[c]

def is_word(word):
    words = set(['go', 'hi'])
    return word in words

print(get_nearby_words('gi'))
