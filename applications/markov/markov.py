import random

# Day 2 fix
# import text and split
# make a dictionary for words
# make a dictionary for start words
# loop the txt file, stopping at the last word in it
# while looping- if a word is in the dict, append the next word
# if it isn't, insert the next word at that index
# check for start word - add it to dictionary if it is
# Make sentences
# random.choice out of start words
# Loop, adding random words from the word dictionary
# Check for end punctuation
# If yes - end loop

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    split = words.split()


sentence_dict = {}
start_words = {}


def random_sentence():
    for word in split:
        if word[0].isupper() or word[0] == '"':
            start_words[word] = word

    stringed_start = list(start_words.keys())

    for i in range(len(split)):
        if i == len(split) - 1:
            break
        if split[i] in sentence_dict:
            sentence_dict[split[i]].append(split[i + 1])
        else:
            sentence_dict[split[i]] = [split[i + 1]]

    stop_punctuation = ['.', '?', '!', '"']
    next_word = random.choice(stringed_start)
    sentence = ''
    end = False

    while not end:
        sentence += next_word + ' '
        next_word = random.choice(sentence_dict[next_word])
        last = next_word[len(next_word)-1]
        if last in stop_punctuation:
            next_to_last = next_word[len(next_word)-2]
            if last == '"' and next_to_last not in stop_punctuation:
                continue
            sentence += next_word
            print(sentence)
            end = True


# TODO: construct 5 random sentences
# Your code here


random_sentence()
random_sentence()
random_sentence()
random_sentence()
random_sentence()
