class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        digits = []
        letters = []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        digits.sort(key=lambda x: (x.split()[1:].join()))

        return letters + digits
