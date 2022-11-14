class Solution:
    """
    the pattern takes the first half and adds a bit flipped version to the sequence, this is how the whole set is built.
    so this keeps halving and adds a flipping at every halving (when even) or add one and halve until the value to be returned is at idx 1.
    once this is done, the number of flips applied determines what the resultant is.
    """
    def kthGrammar(self, n: int, k: int) -> int:
        n_flip = 0
        while k > 1:
            if k % 2:   # Odd
                k = (k+1) / 2
            else:
                k = k / 2
                n_flip += 1
        return n_flip % 2


dummy = Solution()
# print(dummy.kthGrammar(2,2))
# print(dummy.kthGrammar(6,12))
print(dummy.kthGrammar(6,5))

