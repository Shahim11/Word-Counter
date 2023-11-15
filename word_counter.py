print("\n")  # For new line
print("****** Welcome to the Word Counter App! ******")
print("\n")  # For new line


# Define function to read the file and return a list of words
def read_file(file_name):
    words = []
    with open(file_name, "r") as f:
        for line in f:
            words.append(line.strip().lower())  # Convert the words to lowercase for case-insensitive comparison
    return words


# Define function to count the number of occurrences of a word in the list
def count_occurrences(word, words_list):
    count = 0
    for a in words_list:
        if a == word.lower():   # Convert the search word to lowercase for case-insensitive comparison
            count += 1
    return count


# Read the file and get the list of words
file_name = "input.txt"
words_list = read_file(file_name)


# search_words list
search_words = ["Python", "C", "OOP", "Hello", "Java"]


# Count the number of occurrences of each word in the search_words
word_counts = {}
for word in search_words:
    word_counts[word] = count_occurrences(word, words_list)


# find the word with the highest length in the list
max_length_word = max(search_words, key=len)
# print(max_length_word)
max_length = len(max_length_word)
# print(type(max_length))


# Print the word counts to the console
# print(word_counts)
# print(word_counts.items())
for word, count in word_counts.items():
    # print(word, "->", count)
    print("{0:{1}} ->{2:4}".format(word, max_length, count))
    
