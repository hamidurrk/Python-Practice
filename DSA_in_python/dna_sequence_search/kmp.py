def build_failure_table(pattern):
    m = len(pattern)
    failure = [0] * m
    i, j = 1, 0

    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            failure[i] = j
            i += 1
        elif j > 0:
            j = failure[j-1]
        else:
            failure[i] = 0
            i += 1

    return failure

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    failure = build_failure_table(pattern)
    i, j = 0, 0

    while i < n:
        if text[i] == pattern[j]:
            if j == m - 1:
                return i - j
            i += 1
            j += 1
        elif j > 0:
            j = failure[j-1]
        else:
            i += 1

    return -1

def search_dna_sequence(filename, pattern):
    with open(filename, 'r') as file:
        text = file.read().replace('\n', '')

    index = kmp_search(text, pattern)

    if index != -1:
        print("Pattern found at index:", index)
    else:
        print("Pattern not found.")

# Example usage
filename = "dog.txt"
pattern = "AGTACG"

search_dna_sequence(filename, pattern)
