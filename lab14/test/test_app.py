from app import hello
from app import extract_sentiment
from app import text_contain_word
from app import bubble_sort
import pytest


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want

testdata1 = ["I think today will be a great day"]

@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0

testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output


# Zadanie do samodzielnego wykonania
unsorted = [[6, 8, 14, 15, 125, 9, 1, 0, 3, 3, 2, 1, 3, 5, 7, 123, 4, 1, 4],
             [1, 2, -1, 2, 3, 4, 1, 2, 3, 4, 3]]
sorted_lists = [sorted([6, 8, 14, 15, 125, 9, 1, 0, 3, 3, 2, 1, 3, 5, 7, 123, 4, 1, 4]),
            sorted([1, 2, -1, 2, 3, 4, 1, 2, 3, 4, 3])]

testdata3 = [(unsorted[0], sorted_lists[0]), (unsorted[1], sorted_lists[1])]
@pytest.mark.parametrize('sample, expected_output', testdata3)
def test_bubble_sort(sample, expected_output):
    got = bubble_sort(sample)
    assert got == expected_output
