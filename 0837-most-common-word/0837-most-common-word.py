class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        filtered_words = [word for word in re.sub('[^a-z0-9]', ' ', paragraph.lower()).split() if word not in banned]
  
        counts = collections.Counter(filtered_words)
        return counts.most_common(1)[0][0]