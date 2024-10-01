# 8. String Algorithms

# KMP Algorithm (Knuth-Morris-Pratt)
"""Application: The KMP algorithm is used for searching substrings in text, which is a fundamental operation in many text processing applications.
Example: It is used in word processors to find and replace text efficiently. It is also employed in DNA sequence analysis, pattern matching in bioinformatics, and search engines for keyword searching."""

def kmp_search(pattern, text):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1  # Pattern not found

# Test KMP Algorithm
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
index_kmp = kmp_search(pattern, text)
print("KMP Search:", index_kmp)  # Expected: 10 (starting index of "ABABCABAB" in the text)