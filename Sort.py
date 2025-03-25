# 冒泡排序
# 通过重复地走访要排序的数列，一次比较两个数据元素，如果顺序不对则进行交换，并一直重复这样的走访操作，直到没有要交换的数据元素为止。
# 特点：算法简单，空间复杂度低，但时间复杂度较高，为O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 插入排序
# 对于未排序数据，它会在已排序序列中从后向前扫描，找到相应位置并插入，就像打扑克牌时整理手中牌的过程。
# 特点：在数据基本有序时，时间复杂度接近O(n)，空间复杂度为O(1)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# 选择排序
# 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置；
# 然后再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
# 特点：无论数据初始状态如何，时间复杂度都是O(n^2)，空间复杂度为O(1)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# 快速排序
# 通过选择一个基准值，将数组分为两部分，小于基准值和大于基准值，然后递归地对这两部分进行排序。
# 特点：平均时间复杂度为O(nlog n)，但在最坏情况下可能退化为O(n^2)，空间复杂度为O(log n)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    return quick_sort(left) + middle + quick_sort(right)

# 归并排序
# 将数组分成两个子数组，对每个子数组进行排序，然后将排序好的子数组合并成一个排序好的数组，采用分治的思想。
# 特点：时间复杂度稳定为O(nlog n)，空间复杂度为O(n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged