"""
Comprehensive test suite for the palindrome checker function.

Tests cover:
- Basic palindromes
- Mixed case
- Spaces
- Punctuation
- Numbers
- Edge cases (empty strings, None, single characters, etc.)
- Special characters
- Unicode characters
"""

import pytest
from palindrome import is_palindrome


class TestBasicPalindromes:
    """Test basic palindrome cases."""
    
    def test_simple_palindrome(self):
        """Test simple lowercase palindrome."""
        assert is_palindrome("racecar") is True
    
    def test_simple_non_palindrome(self):
        """Test simple non-palindrome."""
        assert is_palindrome("hello") is False
    
    def test_single_character(self):
        """Test single character (always a palindrome)."""
        assert is_palindrome("a") is True
        assert is_palindrome("A") is True
        assert is_palindrome("5") is True
    
    def test_two_characters_palindrome(self):
        """Test two character palindrome."""
        assert is_palindrome("aa") is True
        assert is_palindrome("ab") is False


class TestMixedCase:
    """Test palindromes with mixed case."""
    
    def test_mixed_case_palindrome(self):
        """Test palindrome with mixed case."""
        assert is_palindrome("Racecar") is True
        assert is_palindrome("RACECAR") is True
        assert is_palindrome("RaCeCaR") is True
    
    def test_mixed_case_non_palindrome(self):
        """Test non-palindrome with mixed case."""
        assert is_palindrome("Hello") is False
        assert is_palindrome("WORLD") is False


class TestSpaces:
    """Test palindromes with spaces."""
    
    def test_palindrome_with_spaces(self):
        """Test palindrome phrase with spaces."""
        assert is_palindrome("a man a plan a canal panama") is True
        assert is_palindrome("A man a plan a canal Panama") is True
        assert is_palindrome("race a car") is False
    
    def test_multiple_spaces(self):
        """Test palindrome with multiple spaces."""
        assert is_palindrome("a  b  a") is True
        assert is_palindrome("never odd or even") is True
    
    def test_only_spaces(self):
        """Test string with only spaces."""
        assert is_palindrome("   ") is False
        assert is_palindrome(" ") is False


class TestPunctuation:
    """Test palindromes with punctuation."""
    
    def test_palindrome_with_punctuation(self):
        """Test palindrome with punctuation marks."""
        assert is_palindrome("A man, a plan, a canal: Panama!") is True
        assert is_palindrome("race, a car!") is False
        assert is_palindrome("Was it a car or a cat I saw?") is True
    
    def test_various_punctuation(self):
        """Test with various punctuation marks."""
        assert is_palindrome("Madam, I'm Adam.") is True
        assert is_palindrome("Eve, mad Adam, Eve!") is True
        assert is_palindrome("Hello, world!") is False
    
    def test_only_punctuation(self):
        """Test string with only punctuation."""
        assert is_palindrome("!!!") is False
        assert is_palindrome(".,!?") is False


class TestNumbers:
    """Test palindromes with numbers."""
    
    def test_numeric_palindrome(self):
        """Test numeric palindromes."""
        assert is_palindrome("12321") is True
        assert is_palindrome("12345") is False
        assert is_palindrome("1221") is True
    
    def test_number_as_integer(self):
        """Test passing integer directly."""
        assert is_palindrome(12321) is True
        assert is_palindrome(12345) is False
        assert is_palindrome(1) is True
    
    def test_mixed_letters_and_numbers(self):
        """Test palindromes with letters and numbers."""
        assert is_palindrome("a1a") is True
        assert is_palindrome("1a1") is True
        assert is_palindrome("a1b") is False
        assert is_palindrome("race2car") is False


class TestEdgeCases:
    """Test edge cases and special scenarios."""
    
    def test_empty_string(self):
        """Test empty string."""
        assert is_palindrome("") is False
    
    def test_none_input(self):
        """Test None input."""
        assert is_palindrome(None) is False
    
    def test_very_long_palindrome(self):
        """Test very long palindrome."""
        long_palindrome = "a" * 1000
        assert is_palindrome(long_palindrome) is True
    
    def test_very_long_non_palindrome(self):
        """Test very long non-palindrome."""
        long_non_palindrome = "a" * 999 + "b"
        assert is_palindrome(long_non_palindrome) is False
    
    def test_special_characters_only(self):
        """Test strings with only special characters."""
        assert is_palindrome("@#$%") is False
        assert is_palindrome("@@@") is False


class TestComplexCases:
    """Test complex real-world palindrome cases."""
    
    def test_complex_phrases(self):
        """Test complex palindrome phrases."""
        assert is_palindrome("A Santa at NASA") is True
        assert is_palindrome("Mr. Owl ate my metal worm") is True
        assert is_palindrome("Do geese see God?") is True
    
    def test_palindrome_with_all_features(self):
        """Test palindrome with case, spaces, punctuation, and numbers."""
        assert is_palindrome("A1b2c3c2b1a") is True
        assert is_palindrome("Race 2 car!") is False


class TestUnicodeAndSpecial:
    """Test Unicode and special character handling."""
    
    def test_unicode_characters(self):
        """Test with Unicode characters (if applicable)."""
        # Standard ASCII should work
        assert is_palindrome("civic") is True
        # Note: Full Unicode support would require additional handling
        # "été" when cleaned becomes "t" (single char), which is a palindrome
        assert is_palindrome("été") is True  # Single char after cleaning
        # Test that Unicode alphanumeric characters are handled
        # "a1b2b1a" with mixed case should work
        assert is_palindrome("A1B2B1A") is True


class TestBooleanAndTypeHandling:
    """Test type handling for various input types."""
    
    def test_boolean_input(self):
        """Test boolean input (converted to string)."""
        assert is_palindrome(True) is False  # "True" -> "true" -> not palindrome
        assert is_palindrome(False) is False  # "False" -> "false" -> not palindrome
    
    def test_float_input(self):
        """Test float input."""
        # "121.0" -> "1210" -> "0121" reversed, so NOT a palindrome
        assert is_palindrome(121.0) is False
        # "123.45" -> "12345" -> "54321" reversed, so NOT a palindrome
        assert is_palindrome(123.45) is False
        # Test a float that would be a palindrome
        # "12.21" -> "1221" -> palindrome
        assert is_palindrome(12.21) is True

