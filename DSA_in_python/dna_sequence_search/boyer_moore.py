def build_bad_character_table(pattern):
    table = {}
    m = len(pattern)
    for i in range(m - 1):
        table[pattern[i]] = m - 1 - i
    return table

def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0

    bad_character_table = build_bad_character_table(pattern)

    i = m - 1
    while i < n:
        j = m - 1
        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1
        if j == -1:
            return i + 1
        else:
            if text[i] in bad_character_table:
                i += bad_character_table[text[i]]
            else:
                i += m
    return -1

def search_dna_sequence(filename, pattern):
    with open(filename, 'r') as file:
        text = file.read().replace('\n', '')

    index = boyer_moore_search(text, pattern)

    if index != -1:
        print("Pattern found at index:", index)
    else:
        print("Pattern not found.")

filename = "dog.txt"
pattern = "ATGCC"

search_dna_sequence(filename, pattern)
