# src/count_vowels.py

def count_vowels(text):
    """Returns the count of vowels (a, e, i, o, u) in the input string, case insensitive."""
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)
