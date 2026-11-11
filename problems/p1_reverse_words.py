def reverse_word_order(line):
    words = line.split()
    ending = ""

    # Move sentence-ending punctuation to the end of the reversed sentence.
    if words and words[-1] and words[-1][-1] in ".!?":
        ending = words[-1][-1]
        words[-1] = words[-1][:-1]

    return " ".join(reversed(words)) + ending


def main():
    line = input()
    print(reverse_word_order(line))


if __name__ == "__main__":
    main()
