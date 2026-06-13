class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]
            mod = total % 26
            mapped_char = chr(ord('z') - mod)

            result.append(mapped_char)
        return "".join(result)
        
        
        