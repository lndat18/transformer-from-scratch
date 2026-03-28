import math as m

from collections import Counter


def n_gram(text: str, n: int) -> list:
    n_gram_list = []
    words = text.split()

    for i in range(len(words) - n + 1):
        n_gram_list.append(tuple(words[i: i + n]))
    
    return n_gram_list


def cal_n_gram_match(n_gram_candidate, n_gram_reference) -> int:
    n_gram_candidate_counter = Counter(n_gram_candidate)
    n_gram_reference_counter = Counter(n_gram_reference)

    return sum((n_gram_reference_counter & n_gram_candidate_counter).values())
    

def n_gram_precision_score(candidate: str, reference: str, n: int) -> list:
    n_gram_candidate = n_gram(candidate, n)
    n_gram_reference = n_gram(reference, n)

    n_gram_match = cal_n_gram_match(n_gram_candidate, n_gram_reference)
    total_n_gram_in_prediction = len(n_gram(candidate, n))

    if total_n_gram_in_prediction == 0:
        return 0

    return n_gram_match / total_n_gram_in_prediction


def geometric_average_precision(candidate, reference):
    
    return m.prod([n_gram_precision_score(candidate, reference, i)**(1/4) for i in range(1,5)])
    

def brevity_penalty_score(length_prediction, length_reference) -> float:
    if length_prediction > length_reference:
        return 1

    return m.exp(1 - (length_reference / length_prediction))


def bleu_score(candidate, reference):
    BP = brevity_penalty_score(len(candidate), len(reference))
    geometric_mean = geometric_average_precision(candidate, reference)

    return BP * geometric_mean

