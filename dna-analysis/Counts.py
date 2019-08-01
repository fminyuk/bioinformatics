import numpy as np

num_2_dna = dict(enumerate('ACGT'))
dna_2_num = {l: i for i, l in num_2_dna.items()}


def pattern_to_number(pattern: str) -> int:
    number = 0
    for c in pattern:
        number *= 4
        number += dna_2_num[c]
    return number


def number_to_pattern(number: int, len: int) -> str:
    letters = []
    for i in range(len):
        letters.append(num_2_dna[number % 4])
        number //= 4
    return ''.join(letters[::-1])


def compute_frequencies(dna: str, k: int):
    frequency_array = np.zeros(4 ** k, np.int)
    for i in range(len(dna) - k + 1):
        j = pattern_to_number(dna[i:i + k])
        frequency_array[j] += 1
    return frequency_array


def faster_frequent_words(dna: str, k: int):
    frequent_patterns = set()
    frequency_array = compute_frequencies(dna, k)
    max_count = np.max(frequency_array)
    for j in range(len(frequency_array)):
        if frequency_array[j] == max_count:
            frequent_patterns.add(number_to_pattern(j, k))
    frequent_patterns = list(frequent_patterns)
    frequent_patterns.sort()
    return frequent_patterns


def read_dna_k(filename: str):
    with open(filename, 'r') as f:
        dna = f.readline()
        k = f.readline()
        return dna.strip(), int(k.strip())

# print(' '.join(map(str, compute_frequencies(*read_dna_k('dataset_2994_5.txt')))))


# # print(pattern_to_number('ATGCAA'))
# print(number_to_pattern(5437, 8))
#
#
# print(compute_frequencies())
