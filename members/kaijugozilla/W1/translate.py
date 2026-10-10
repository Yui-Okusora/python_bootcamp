def binary_search(a: list[int], key: int) -> int:
    """
    Tìm kiếm một phần tử trong danh sách đã được sắp xếp bằng thuật toán tìm kiếm nhị phân (Binary Search).
    Điểm khác biệt so với C++:
    Trong Python, hàm len(a) được sử dụng để lấy số lượng phần tử của danh sách, thay vì a.size() như trong C++.
    Ngoài ra, Python sử dụng toán tử // để thực hiện phép chia lấy phần nguyên, giúp biến mid luôn là số nguyên và có thể dùng làm chỉ số truy cập danh sách.
    Python cũng sử dụng thụt lề để xác định khối lệnh thay vì dấu ngoặc nhọn {} như trong C++.
    """
    lo = 0
    hi = len(a) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if a[mid] == key:
            return mid

        if a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1
