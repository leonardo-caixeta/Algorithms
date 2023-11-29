def is_anagram(first_string: str, second_string: str):
    sorted_second_str = ''.join(merge_sort(second_string.lower()))
    sorted_first_str = ''.join(merge_sort(first_string.lower()))
    if not first_string or not second_string:
        return (sorted_first_str, sorted_second_str, False)

    if sorted_first_str == sorted_second_str:
        return (sorted_first_str, sorted_second_str, True)

    return (sorted_first_str, sorted_second_str, False)


def merge_sort(s):
    if len(s) <= 1:
        return s
    mid = len(s) // 2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])
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
