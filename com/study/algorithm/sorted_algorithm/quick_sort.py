def quickSort(nums, left, right):
    if left < right:
        partition_index = partition(nums, left, right)

        quickSort(nums, left, partition_index -1)
        quickSort(nums, partition_index + 1, right)
    return nums

def partition(nums, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if nums[i] < nums[pivot]:
            swab(nums, i, index)
            index += 1
        i += 1

    swab(nums, pivot, index - 1)
    return index - 1


def swab(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]



if __name__ == '__main__':
    nums = [4,1]
    quickSort(nums, 0, len(nums) - 1)
    print(nums)