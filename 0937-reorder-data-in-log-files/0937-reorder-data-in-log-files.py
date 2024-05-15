class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        character, nums = [], []
        for log in logs:
            if log.split()[1].isdigit():
                nums.append(log)
            else:
                character.append(log)

        character.sort(key=lambda x : (x.split()[1:], x.split()[0]))
        return character + nums