class Solution(object):
    def mergeAlternately(self, word1, word2):
        i, j = 0, 0
        n1, n2 = len(word1), len(word2)
        merged_chars = []

        # Alternate characters while both strings have characters left
        while i < n1 and j < n2:
            merged_chars.append(word1[i])
            merged_chars.append(word2[j])
            i += 1
            j += 1

        # Append the remaining tail (if any)
        if i < n1:
            merged_chars.append(word1[i:])
        if j < n2:
            merged_chars.append(word2[j:])

        return ''.join(merged_chars)


# --- quick tests ---
if __name__ == "__main__":
    s = Solution()
    print(s.mergeAlternately("abc", "pqr"))   # apbqcr
    print(s.mergeAlternately("ab", "pqrs"))   # apbqrs
    print(s.mergeAlternately("abcd", "pq"))   # apbqcd
