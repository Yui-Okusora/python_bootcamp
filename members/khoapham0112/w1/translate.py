def binary_search(a, key):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (high + low)//2
        if a[mid] == key: 
            return mid
        elif a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
"""
Điểm khác biệt so with C++:
 - Python không lo bị tràn số nguyên (integer overflow) khi tính `mid = (low + high) // 2` vì số nguyên trong Python có độ dài gần như vô hạn.
 - Trong C++, việc tính mid dễ gây tràn số `int`, nên C++ dùng công thức an toàn: `low + (high - low) / 2`.
"""