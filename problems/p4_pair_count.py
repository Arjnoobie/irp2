def count_pairs(numbers, target_sum):
    seen = {}
    pair_count = 0

    for value in numbers:
        complement = target_sum - value
        pair_count += seen.get(complement, 0)
        seen[value] = seen.get(value, 0) + 1

    return pair_count


def main():
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(count_pairs(numbers[:n], k))


if __name__ == "__main__":
    main()
