def remove_Dupp(vector):
    seen = set()
    result = []
    for item in vector:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage
original_vector = ["apple", "banana", "apple", "orange"]
unique_vector = remove_Dupp(original_vector)
print(unique_vector)  
