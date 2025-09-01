def count_words(text):
    """
    Counts the number of words in a text string.
    
    Args:
        text (str): The text string to count words in
        
    Returns:
        int: The number of words found in the text
    """
    return len(text.split())
def count_letters(text):
    """
    Counts the number of times each character appears in the text.
    Converts all characters to lowercase to avoid duplicates.
    
    Args:
        text (str): The text string to analyze
        
    Returns:
        dict: Dictionary with characters as keys and their counts as values
              Format: {'p': 6121, 'r': 20818, 'o': 25225, ...}
    """
    # Convert text to lowercase to avoid duplicates
    text_lower = text.lower()
    
    # Create dictionary to store character counts
    char_count = {}
    
    # Count each character in the text
    for char in text_lower:
        if char in char_count:
            char_count[char] += 1  # Increment count if character already exists
        else:
            char_count[char] = 1   # Initialize count if character is new
    
    return char_count
def sort_on(char_dict):
    """
    Helper function that returns the value of the "num" key.
    This is how the .sort() method knows how to sort the list of dictionaries.
    
    Args:
        char_dict (dict): Dictionary with 'char' and 'num' keys
        
    Returns:
        int: The count value for sorting comparison
    """
    return char_dict["num"]

def sort_character_counts(char_counts_dict):
    """
    Converts a character count dictionary to a sorted list of dictionaries.
    Each dictionary contains 'char' and 'num' keys, sorted by count (greatest to least).
    
    Args:
        char_counts_dict (dict): Dictionary with characters as keys and counts as values
        
    Returns:
        list: Sorted list of dictionaries in format [{"char": "b", "num": 4868}, ...]
    """
    # Convert dictionary to list of dictionaries with 'char' and 'num' keys
    char_list = []
    for char, count in char_counts_dict.items():
        char_list.append({"char": char, "num": count})
    
    # Sort the list using the helper function, from greatest to least
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list