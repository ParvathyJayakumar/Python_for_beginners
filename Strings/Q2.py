#Reverse a sequence of comma-separated words and print the result.
sequence = input("Enter comma-separated words: ").split(',')
print(','.join(sequence[::-1]))