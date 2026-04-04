class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ""
        
        cols = len(encodedText) // rows
        
        matrix = []
        idx = 0
        for i in range(rows):
            matrix.append(encodedText[idx:idx+cols])
            idx += cols
        
        result = []
        for j in range(cols):
            i, k = 0, j
            while i < rows and k < cols:
                result.append(matrix[i][k])
                i += 1
                k += 1
        
        return ''.join(result).rstrip()
        