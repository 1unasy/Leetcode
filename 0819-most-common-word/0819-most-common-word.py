class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        filtered_words = [word for word in re.sub('[^a-z0-9]', ' ', paragraph.lower()).split() if word not in banned]
        from collections import defaultdict
        dict = defaultdict(int)
        for word in filtered_words:
            dict[word] += 1    
        return sorted(dict.items(),key=lambda x: -x[1])[0][0]   
        