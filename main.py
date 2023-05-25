def timer(func):
    import timeit

    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = timeit.default_timer() - start_time
        print(
            f"Function {func.__name__} took {elapsed:.6f} seconds to execute."
        )
        return result

    return wrapper


@timer
def word_frequency_v1(paragraph: list[str]) -> dict[str, int]:
    word_freq = {}

    words = []
    for sentence in paragraph:
        words += sentence.lower().split()

    for word in words:
        word = word.strip(".,!?")

        if word:
            word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq


@timer
def word_frequency_v2(paragraph: list[str]) -> dict[str, int]:
    word_freq = {}

    for sentence in paragraph:
        word = ""
        for char in sentence:
            if char.isalnum():
                word += char.lower()
            elif word:
                word_freq[word] = word_freq.get(word, 0) + 1
                word = ""

        if word:
            word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq


if __name__ == "__main__":
    paragraph = [
        "The quick brown fox",
        "jumps over the lazy dog.",
        "The dog barks,",
        "and the fox runs away."
    ]

    print(word_frequency_v1(paragraph))
    print(word_frequency_v2(paragraph))
