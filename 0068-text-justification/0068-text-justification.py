class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_words = []
            line_len = 0

            while i < n:
                if line_len + len(words[i]) + len(line_words) > maxWidth:
                    break
                line_words.append(words[i])
                line_len += len(words[i])
                i += 1

            if i == n or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                res.append(line)
                continue

            total_spaces = maxWidth - line_len
            gaps = len(line_words) - 1

            space_each = total_spaces // gaps
            extra = total_spaces % gaps

            line = ""
            for j in range(gaps):
                line += line_words[j]
                line += " " * (space_each + (1 if j < extra else 0))
            line += line_words[-1]

            res.append(line)

        return res
        