def solve(word):
    # Function to calculate the value of a substring
    def substring_value(sub):
        value = 0
        for char in sub:
            value += ord(char) - ord('a') + 1
        return value

   