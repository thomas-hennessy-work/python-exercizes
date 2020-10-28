from intermidiate import num_to_word
import pytest

def test_123():
    assert num_to_word.final_word(123) == "one hundred and twenty three"

def test_5011():
    assert num_to_word.final_word(5011) == "five thousand and eleven"

def test_923341573943234():
    assert num_to_word.final_word(923341573943234) == "nine hundred and twenty three trillion, three hundred and forty one billion, five hundred and seventy three million, nine hundred and forty three thousand two hundred and thirty four"