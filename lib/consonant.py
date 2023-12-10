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


     # Find consonant substrings 
    consonant_substrings = []
    substring_start = 0
    for i in range(len(word_without_vowels) + 1):
        if i == len(word_without_vowels) or word_without_vowels[i] in vowels:
            if substring_start < i:
                consonant_substrings.append(word_without_vowels[substring_start:i])
            substring_start = i + 1

    # Calculate values of substrings and return the maximum value
    max_value = 0
    for sub in consonant_substrings:
        sub_value = substring_value(sub)
        if sub_value > max_value:
            max_value = sub_value