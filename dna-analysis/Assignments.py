import Counts


def read_dna_k(filename: str):
    with open(filename, 'r') as f:
        dna = f.readline()
        k = f.readline()
        return dna.strip(), int(k.strip())


def read_dna(filename: str):
    with open(filename, 'r') as f:
        dna = f.readline()
        return dna.strip()


def read_number_k(filename: str):
    with open(filename, 'r') as f:
        number = f.readline()
        k = f.readline()
        return int(number.strip()), int(k.strip())


def print_answer(assignment: str, answer):
    print(assignment)
    print(answer)
    print()


print_answer('1.5.5', ' '.join(map(str, Counts.compute_frequencies(*read_dna_k('dataset_2994_5.txt')))))

print_answer('1.6.2', Counts.pattern_to_number(read_dna('dataset_3010_2.txt')))

print_answer('1.6.5', Counts.number_to_pattern(*read_number_k('dataset_3010_5.txt')))

# print_answer('1.6.5', Counts.finding_frequent_words_by_sorting())
