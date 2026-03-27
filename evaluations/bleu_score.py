import math as m
from collections import Counter


def n_gram(text: str, n: int) -> list:
    n_gram_list = []
    words = text.split()

    for i in range(len(words) - n + 1):
        n_gram_list.append(words[i: i + n])
    
    return n_gram_list


def cal_n_gram_match(n_gram_candidate, n_gram_reference) -> int:
    n_gram_candidate = Counter(tuple(n_gram_candidate))
    n_gram_reference = Counter(tuple(n_gram_reference))

    print(n_gram_candidate)
    print(n_gram_reference)
    pass


def n_gram_precision_score(candidate: str, reference: str, n: int) -> list:
    n_gram_candidate = n_gram(candidate, n)
    n_gram_reference = n_gram(reference, n)

    n_gram_match = cal_n_gram_match(n_gram_candidate, n_gram_reference)
    total_n_gram_in_prediction = len(n_gram(candidate, n))

    return n_grams_match / total_n_gram_in_prediction


def n_gram_precision_list(candidate, reference):
    pre_list = []
    
    pass


def brevity_penalty_score(length_prediction, length_reference) -> float:
    if length_prediction > length_reference:
        return 1

    return m.exp((1-length_reference) / length_prediction)


def geometric_average_precision(n_gram_precision_list: list):
    res = 1
    for p_i in n_gram_precision_list:
        res *= p_i**(1/4) 

    return res


def bleu_score(candidate, reference):
    n_gram_pre_list = n_gram_precision_list(candidate, reference)

    BP = brevity_penalty_score(len(candidate), len(reference))
    geometric_mean = geometric_average_precision(n_gram_pre_list)

    return BP * geometric_mean


