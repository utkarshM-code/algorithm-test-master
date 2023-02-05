from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        assert len(c) == 1
        return max(1, self.table.get(c, len(self.pattern)-1))

    def search(self) -> int:
        lenOfPattern = len(self.pattern)
        lenOfText = len(self.text)
        maxIndex = lenOfText - lenOfPattern
        currIndex = 0
        while currIndex <= maxIndex:
            pattern_index = lenOfPattern - 1
            while pattern_index >= 0 and self.pattern[pattern_index] == self.text[currIndex + pattern_index]:
                pattern_index -= 1
            if pattern_index < 0:
                return currIndex
            currIndex = currIndex + self.decide_slide_width(self.text[currIndex + pattern_index])

        return -1
