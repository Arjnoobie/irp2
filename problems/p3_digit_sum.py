def digit_sum(number):
    number = abs(number)

    if number < 10:
        return number

    return number % 10 + digit_sum(number // 10)


def main():
    number = int(input())
    print(digit_sum(number))


if __name__ == "__main__":
    main()
