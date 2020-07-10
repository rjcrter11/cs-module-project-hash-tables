# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
# import with open
# Make dictionary for that frequencies table
# Make another dictionary to store letter counts
# Another one to store their frequencies
# Store total number of letters
# get letter frequencies by dividing letter count by total letters
# Sort both the frequencies table, and the letter frequencies
# Get the keys of both, then stringify them
# Replace letters in letter frequencies in encrypted text w/ letters from the frequencies table
# Note: maketrans/translate is for characters -- replace is for substrings


with open('ciphertext.txt') as f:
    encrypted_text = f.read()


def decrypt(text):
    frequencies = {
        "E": 11.53,
        "T": 9.75,
        "A": 8.46,
        "O": 8.08,
        "H": 7.71,
        "N": 6.73,
        "R": 6.29,
        "I": 5.84,
        "S": 5.56,
        "D": 4.74,
        "L": 3.92,
        "W": 3.08,
        "U": 2.59,
        "G": 2.48,
        "F": 2.42,
        "B": 2.19,
        "M": 2.18,
        "Y": 2.02,
        "C": 1.58,
        "P": 1.08,
        "K": 0.84,
        "V": 0.59,
        "Q": 0.17,
        "J": 0.07,
        "X": 0.07,
        "Z": 0.03
    }

    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_counts = {}
    letter_frequency = {}

    total = 0

    for char in encrypted_text:
        if char in ALPHABET:
            total += 1
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    for letter in ALPHABET:
        letter_frequency[letter] = letter_counts[letter] / total

    letter_frequency = list(letter_frequency.items())
    frequencies = list(frequencies.items())

    letter_frequency.sort(key=lambda x: x[1])
    frequencies.sort(key=lambda x: x[1])

    encrypted_list = []
    for letter in letter_frequency:
        encrypted_list.append(letter[0])
    encrypted_string = ''.join(encrypted_list)

    cache_frequencies_list = []
    for letter in frequencies:
        cache_frequencies_list.append(letter[0])
    cache_string = ''.join(cache_frequencies_list)

    translation = encrypted_text.maketrans(
        encrypted_string, cache_string)
    decrypted_text = encrypted_text.translate(translation)

    print(decrypted_text)


decrypt(encrypted_text)
