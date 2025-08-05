# Given a string, find the first character that does not repeat anywhere in the string. Return None if all characters repeat.



# Input: "Hello"

# Output: "H"
# Input: "Swiss"
# Output: "w"



def first_non_repeating_char(s):
    # Create a frequency dictionary (case-insensitive)
    freq = {}

    for char in s:
        key = char.lower()  # make it case-insensitive
        freq[key] = freq.get(key, 0) + 1

    # Find first non-repeating character
    for char in s:
        if freq[char.lower()] == 1:
            return char

    return None

# Examples
print(first_non_repeating_char("Hello"))   # Output: H
print(first_non_repeating_char("Swiss"))   # Output: w
print(first_non_repeating_char("aabbcc"))  # Output: None
