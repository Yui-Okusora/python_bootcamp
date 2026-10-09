def count_frequency(vector):
    frequency = {}

    for element in vector:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1

    return frequency