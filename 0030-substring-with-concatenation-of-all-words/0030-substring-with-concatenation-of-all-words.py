from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        
        word_count = Counter(words)
        res = []

        for i in range(word_len):  # different offsets
            left = i
            curr_count = {}
            count = 0

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_count:
                    curr_count[word] = curr_count.get(word, 0) + 1
                    count += 1

                    # if excess word, shrink window
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    # valid window
                    if count == total_words:
                        res.append(left)

                else:
                    # reset window
                    curr_count.clear()
                    count = 0
                    left = j + word_len

        return res