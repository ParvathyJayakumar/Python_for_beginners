#Count and print vowels in alphabetical order from a string. If no vowels, print "none".
s = input("Enter a string: ").lower()
vowels = sorted(set(filter(lambda x: x in 'aeiou', s)))
print(''.join(vowels) if vowels else "none")