"""Find all prime numbers up to n using the Sieve of Eratosthenes.

Difference from C++:
Unlike C++ where std::vector<bool> requires manual dynamic allocation or 
fixed-size array indexing, Python creates the list using list multiplication 
`[True] * (n + 1)` and list comprehension for a more expressive syntax.
"""
def primes_up_to(n : int) -> list[int]:
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    i = 2
    while i * i < n:
        if is_prime[i]:
            for k in range(i * i, n + 1, i):
                is_prime[k] = False
        i += 1
    
    return [num for num in range(2, n + 1) if is_prime[num]]