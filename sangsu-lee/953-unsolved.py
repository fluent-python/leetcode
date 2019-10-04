from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = '!' + order
        words = self.fill_gap(words)
        for i in range(len(words[0])):
            if len(words) <= 1:
                print("TRUE")
                return True
            cur_order_ix = order.index(words[0][i])
            words_to_be_removed = []
            for j, word in enumerate(words):
                ix = order.index(word[i])
                if ix >= cur_order_ix:
                    print("ix: {}".format(ix))
                    print("change, cur_order_ix: {}".format(cur_order_ix))
                    if cur_order_ix != order.index(words[0][i]):
                        print("append {} to words_to_be_removed".format(word))
                        words_to_be_removed.append(word)
                    cur_order_ix = ix
                else:
                    print("ix: {}".format(ix))
                    print("abort: cur_order_ix: {}".format(cur_order_ix))
                    print("FALSE")
                    return False
            print("words_to_be_removed: {}".format(words_to_be_removed))
            for word in words_to_be_removed:
                words.remove(word)

    def fill_gap(self, words):
        max_length = max([len(word) for word in words])
        new_words = []
        for word in words:
            gap_to_fill = '!'*(max_length - len(word))
            new_words.append(word + gap_to_fill)
        return new_words



s = Solution()
s.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")
s.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz")
s.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz")
