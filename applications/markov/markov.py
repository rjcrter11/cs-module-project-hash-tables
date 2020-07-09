import random

# import text -- with open
# split words by whitespace
# start words = capitals, or " followed by a capital
# stop words = words ending in .?!, or that follow by "
# dictionary to hold  start words and endwords -
# conditional for use with random.choice
# iterate through split words until endword variable is hit, random.choice for non start words

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    split = words.split()
    # print(split)


# TODO: analyze which words can follow other words
# Your code here

start_words = {}
end_words = {}

for word in split:
    stop_punctuation = ['.', '?', '!', '"', '."', '?"', '!"']
    if word[0].isupper() == True or word[0] == '\"':
        start_words[word] = word
    elif word[-1] in stop_punctuation or word[-2:] in stop_punctuation:
        end_words[word] = word

start_list = list(start_words.keys())
end_list = list(end_words.keys())


def random_sentence():
    print(random.choice(start_list), end=" ")
    for word in split:
        if word in end_list:
            break
        if word not in start_list:
            print(random.choice(split), end=" ")
    print(random.choice(end_list))


# TODO: construct 5 random sentences
# Your code here
random_sentence()
random_sentence()
random_sentence()
random_sentence()
random_sentence()
