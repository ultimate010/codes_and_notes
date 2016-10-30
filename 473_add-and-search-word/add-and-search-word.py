# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/add-and-search-word
@Language: Python
@Datetime: 16-06-30 13:56
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        # Write your code here
        self.root = TrieNode()
        


    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        # Write your code here
        p = self.root
        for ch in word:
            if ch not in p.children:
                p.children[ch] = TrieNode()
            p = p.children[ch]
        p.isEnd = True


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        # Write your code here
        def _search(root, word):
            p = root
            for i in range(len(word)):
                if word[i] == '.':
                    for t in p.children.values():
                        if _search(t, word[i + 1:]):
                            return True
                    return False
                else:
                    if word[i] in p.children:
                        p = p.children[word[i]]
                    else:
                        return False
            return p.isEnd
        return _search(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")