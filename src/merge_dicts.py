# src/merge_dicts.py

def merge_dicts(dict1, dict2):
    """Merges two dictionaries, summing values of common keys."""
    merged_dict = dict1.copy()  # Start with dict1's keys and values
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Sum values for common keys
        else:
            merged_dict[key] = value  # Add new key-value pair
    return merged_dict
