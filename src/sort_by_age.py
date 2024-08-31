# src/sort_by_age.py

def sort_by_age(people):
    """Sorts a list of tuples (name, age) by age in ascending order."""
    return sorted(people, key=lambda person: person[1])
