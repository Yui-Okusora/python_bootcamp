def count_frequency(vector):
    freq = {}
    for element in vector:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
    return freq