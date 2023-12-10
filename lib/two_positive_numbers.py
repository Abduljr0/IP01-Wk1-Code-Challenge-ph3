def two_positive_numbers (a, b, c):

    positive_count =0 # counts number of positive int

    # condition checks each int and adds positive count

    if a > 0 :
        positive_count += 1
    if b > 0 :
        positive_count += 1
    if c > 0 :
        positive_count += 1
    
    #returns true if only 2 integers are positive 
    return positive_count == 2
    
    
print (two_positive_numbers (12, 40, -3))
print (two_positive_numbers (12, -40, -3))