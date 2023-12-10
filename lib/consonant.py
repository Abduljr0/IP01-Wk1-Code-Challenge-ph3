def solve(word):
    # Function to calculate the value of a substring
    def substring_value(sub):
        value = 0
        for char in sub:
            value += ord(char) - ord('a') + 1
        return value

    # Remove vowels from the string
    vowels = 'aeiou'
    word_without_vowels = ''.join([char for char in word if char not in vowels])