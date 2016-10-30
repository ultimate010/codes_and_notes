# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/implement-trie
@Language: Python
@Datetime: 16-06-30 13:40
'''

"""
Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("lintcode")
trie.search("lint") will return false
trie.startsWith("lint") will return true
"""
class TrieNode:
  def __init__(self):
    # Initialize your data structure here.
    self.children = {}
    self.isEnd = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  # @param {string} word
  # @return {void}
  # Inserts a word into the trie.
  def insert(self, word):
      p = self.root
      for ch in word:
          if ch not in p.children:
              p.children[ch] = TrieNode()
          p = p.children[ch]
      p.isEnd = True
              

  # @param {string} word
  # @return {boolean}
  # Returns if the word is in the trie.
  def search(self, word):
      p = self.root
      for ch in word:
          if ch in p.children:
              p = p.children[ch]
          else:
              return False
      return p.isEnd
        

  # @param {string} prefix
  # @return {boolean}
  # Returns if there is any word in the trie
  # that starts with the given prefix.
  def startsWith(self, prefix):
      p = self.root
      for ch in prefix:
          if ch in p.children:
              p = p.children[ch]
          else:
              return False
      return True