class Solution:
  def mostWordsFound(self, sentences: List[str]) -> int:
    maxcnt = 0
    for i in range(len(sentences)):
      cnt = 0
      for j in range(len(sentences[i])):
        if sentences[i][j] == '':
          cnt = cnt + 1
      if cnt > maxcnt:
        maxcnt = cnt
    return maxcnt
