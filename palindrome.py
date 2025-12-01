"""
Palindrome Checker Module

This module provides a function to check if a word or phrase is a palindrome.
A palindrome reads the same forwards and backwards, ignoring case, spaces, and punctuation.
"""


def is_palindrome(text):
    """
    Check if a word or phrase is a palindrome.
    
    A palindrome reads the same forwards and backwards. This function:
    - Ignores case differences
    - Ignores spaces
    - Ignores punctuation marks
    - Handles numbers and special characters
    
    Args:
        text (str): The text to check for palindrome property.
                   Can be a string, number (will be converted to string), or None.
    
    Returns:
        bool: True if the text is a palindrome, False otherwise.
    
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("12321")
        True
    """
    # Handle None and non-string inputs
    if text is None:
        return False
    
    # Convert to string to handle numbers and other types
    text = str(text)
    
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if cleaned string is empty (only punctuation/spaces)
    if not cleaned:
        return False
    
    # Check if the cleaned string equals its reverse
    return cleaned == cleaned[::-1]

