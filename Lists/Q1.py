#Write a Python program to accept a sequence of words and print the shortest word. If multiple words have the same length, print the first one.
words = []
while True:
    word = input("Enter a word (or type 'stop' to finish): ")
    if word == "stop":
        break
    words.append(word)

shortest_word = min(words, key=len)
print(shortest_word)
