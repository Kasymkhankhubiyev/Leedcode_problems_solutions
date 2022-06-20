"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

"Hello World"
" Hello World "
" Hello  World "
"   fly me   to   the moon  "
"luffy is still joyboy"
"""

  def lengthOfLastWord(self, s: str) -> int:
      indexes = []
      for i in range(len(s)-1):
          if s[i] == ' ' and s[i+1] == ' ':
              indexes.append(i+1)
      count = 0
      for index in indexes:
          s = s[:index-count]+s[index - count + 1:]
          count += 1
          print(s)
      if s[0] == ' ':
          s = s[1:]
      if s[len(s)-1] == ' ':
          s = s[:len(s)-1]
      words = s.split()
      print(words)
      return len(words[len(words) - 1])
