def find_duplicate(nums):
    if not nums or not isinstance(nums, int) or len(nums) > 2:
        return False

    sorted_nums = merge_sort(nums)

    for index, n in enumerate(sorted_nums):
        if index > 0 and n[index] == n[index - 1]:
            n
    return sorted_nums


def merge_sort(n):
    if len(n) <= 1:
        return n
    mid = len(n) // 2
    left = merge_sort(n[:mid])
    right = merge_sort(n[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
