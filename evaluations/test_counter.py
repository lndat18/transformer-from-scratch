from collections import Counter


cand_ngrams = [('He', 'eats'), ('eats', 'apple'), ('He', 'eats')] # Giả sử 'He eats' lặp 2 lần
ref_ngrams = [('He', 'eats'), ('eats', 'an'), ('an', 'apple')]

c1 = Counter(cand_ngrams)
c2 = Counter(ref_ngrams)

overlap = c1 & c2
union = c1 | c2

print(overlap)
print(union)