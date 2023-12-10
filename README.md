# IP01-Wk1-Code-Challenge-ph3 

   TOY PROBLEM 

 The function convert_to_24_hour() takes in three arguments: hour (ranging from 1 to 12), minute (ranging from 0 to 59), and period ("am" or "pm"). It converts the time into a 24-hour format and returns a four-digit string representing the time in that format.

For "am" times, it converts 12 am to 0 hours and leaves other hours unchanged.
For "pm" times, it adds 12 to the hour unless the hour is already 12 (as 12 pm remains 12 in the 24-hour format).
The function then formats the hour and minute to ensure they each have two digits e.g., '08' instead of '8', and finally combines them to create the four-digit string representing the time in 24-hour format.


 The two_positive_numbers function takes three integer arguments (a, b, and c) and counts the number of positive integers among them. It returns True if exactly two of the integers are positive and False otherwise.

It counts positive integers by checking each integer using three separate if statements and increments the positive_count variable accordingly.
Finally, it returns True if the positive_count is equal to 2 (indicating exactly two positive integers) and  returns False otherwise.
 
 The solve() function takes a lowercase string as input, removes vowels from the string, finds consonant substrings, calculates their values based on the given mapping of letters to values, and returns the highest value among these consonant substrings.

It defines a nested function substring_value() to calculate the value of a substring based on the given mapping.
Removes vowels from the input string using a list comprehension.
Finds consonant substrings by iterating through the string and separating substrings based on vowel occurrences.
Calculates the value of each consonant substring and keeps track of the maximum value found.
Returns the maximum value among all the consonant substrings.
 









  
