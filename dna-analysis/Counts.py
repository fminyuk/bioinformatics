import numpy as np

number_2_symbol = 'ACGT'
symbol_2_number = {l: i for i, l in enumerate(number_2_symbol)}


def pattern_to_number(pattern: str) -> int:
    number = 0
    for c in pattern:
        number *= 4
        number += symbol_2_number[c]
    return number


def number_to_pattern(number: int, k: int) -> str:
    letters = []
    for i in range(k):
        letters.append(number_2_symbol[number % 4])
        number //= 4
    return ''.join(letters[::-1])


def compute_frequencies(text: str, k: int):
    frequency_array = np.zeros(4 ** k, np.int)
    for i in range(len(text) - k + 1):
        j = pattern_to_number(text[i:i + k])
        frequency_array[j] += 1
    return frequency_array


def faster_frequent_words(text: str, k: int):
    frequent_patterns = set()
    frequency_array = compute_frequencies(text, k)
    max_count = np.max(frequency_array)
    for j in range(len(frequency_array)):
        if frequency_array[j] == max_count:
            frequent_patterns.add(number_to_pattern(j, k))
    frequent_patterns = list(frequent_patterns)
    frequent_patterns.sort()
    return frequent_patterns


def finding_frequent_words_by_sorting(text: str, k: int):
    frequent_patterns = []
    index = np.zeros(len(text) - k + 1, np.int)
    count = np.zeros(len(text) - k + 1, np.int)
    for i in range(len(text) - k + 1):
        pattern = text[i: i + k]
        index[i] = pattern_to_number(pattern)
        count[i] = 1
    sorted_index = np.sort(index)
    for i in range(1, len(text) - k + 1):
        if sorted_index[i] == sorted_index[i - 1]:
            count[i] = count[i - 1] + 1
    max_count = np.max(count)
    for i in range(len(text) - k + 1):
        if count[i] == max_count:
            pattern = number_to_pattern(sorted_index[i], k)
            frequent_patterns.append(pattern)
    return frequent_patterns


# def clump_finding(dna: str, k: int, L: int, t: int):
#     frequent_patterns = set()
#     clump = np.zeros(4 ** k, np.int)
#     for i in range(1, len(dna) - L + 1):
#         text = dna[i: i + L]
#
#     pass
