"""
Simple Letter Code - Substitution Cipher
A basic letter code that shifts each letter by a fixed amount
"""

class LetterCode:
    def __init__(self, shift=3):
        """
        Initialize the letter code with a shift value.
        Default shift is 3 (Caesar cipher)
        """
        self.shift = shift
    
    def encode(self, text):
        """
        Encode text using the letter code
        """
        result = []
        for char in text:
            if char.isalpha():
                if char.isupper():
                    # Shift uppercase letters
                    shifted = chr((ord(char) - ord('A') + self.shift) % 26 + ord('A'))
                    result.append(shifted)
                else:
                    # Shift lowercase letters
                    shifted = chr((ord(char) - ord('a') + self.shift) % 26 + ord('a'))
                    result.append(shifted)
            else:
                # Keep non-letter characters as-is
                result.append(char)
        return ''.join(result)
    
    def decode(self, text):
        """
        Decode text using the letter code
        """
        # Decoding is just encoding with negative shift
        original_shift = self.shift
        self.shift = -self.shift
        decoded = self.encode(text)
        self.shift = original_shift
        return decoded


# Example usage
if __name__ == "__main__":
    # Create a code with shift of 3
    code = LetterCode(shift=3)
    
    # Test encoding
    original = "Hello World"
    encoded = code.encode(original)
    decoded = code.decode(encoded)
    
    print(f"Original:  {original}")
    print(f"Encoded:   {encoded}")
    print(f"Decoded:   {decoded}")
