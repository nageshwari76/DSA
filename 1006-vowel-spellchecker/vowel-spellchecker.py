class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(w):
            return ''.join('*' if c in 'aeiou' else c for c in w.lower())
        exact = set(wordlist)
        lower = {}
        vowel = {}
        for w in wordlist:
            lw = w.lower()
            dv = devowel(w)
            lower.setdefault(lw, w)
            vowel.setdefault(dv, w)
            
        res = []
        for q in queries:
            if q in exact:
                res.append(q)
            else:
                lq = q.lower()
                dq = devowel(q)
                res.append(lower.get(lq,vowel.get(dq, "")))
        return res
        