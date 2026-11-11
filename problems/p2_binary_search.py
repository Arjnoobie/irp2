def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    target = int(input())
    print(binary_search(numbers[:n], target))


if __name__ == "__main__":
    main()
