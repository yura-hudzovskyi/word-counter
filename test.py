import pytest

from main import word_frequency_v1, word_frequency_v2

data_to_test = [
    (
        ["This is a sentence.", "This is another sentence."],
        {"this": 2, "is": 2, "a": 1, "sentence": 2, "another": 1},
    ),
    (
        ["Lorem ipsum dolor sit amet, consectetur adipiscing elit."],
        {
            "lorem": 1,
            "ipsum": 1,
            "dolor": 1,
            "sit": 1,
            "amet": 1,
            "consectetur": 1,
            "adipiscing": 1,
            "elit": 1,
        },
    ),
    (
        ["The quick brown fox", "jumps over the lazy dog."],
        {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1},
    ),
    (
        ["The dog barks,", "and the fox runs away."],
        {"the": 2, "dog": 1, "barks": 1, "and": 1, "fox": 1, "runs": 1, "away": 1},
    ),
    (
        ["The quick brown fox",
         "jumps over the lazy dog.",
         "The dog barks,",
         "and the fox runs away."],
        {"the": 4, "quick": 1, "brown": 1, "fox": 2, "jumps": 1, "over": 1, "lazy": 1, "dog": 2, "barks": 1, "and": 1,
         "runs": 1, "away": 1},
    ),
    (
        [],
        {},
    ),
]


@pytest.mark.parametrize("paragraph, expected", data_to_test)
def test_word_frequency_v1(paragraph, expected):
    assert word_frequency_v1(paragraph) == expected


@pytest.mark.parametrize("paragraph, expected", data_to_test)
def test_word_frequency_v2(paragraph, expected):
    assert word_frequency_v2(paragraph) == expected

