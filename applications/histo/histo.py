# Your code here
# import the file with open
# Init counter dictionary
# LowerCase everything
# Split on the whitespaces
# Iterate through and remove uneeded characters
# Iterate again, counting up each word's use
# Order by number of words descending
# Then by word alphabetically
# Format strings


with open('robin.txt') as f:
    words = f.read()
    # print(words)


def histogram(s):
    bad_chars = ['"', ':', ';', ',', '.', '-', '+', '=', '/',
                 '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', '!', '?']
    counter = {}
    s = s.lower()
    for i in bad_chars:
        s = s.replace(i, "")
    res = s.split()
    for word in res:
        if word not in counter:
            counter[word] = '#'
        else:
            counter[word] += "#"
    count_list = list(counter.items())
    sorted_list = sorted(
        sorted(count_list, key=lambda x: x[0]), key=lambda x: x[1], reverse=True)

    for pair in sorted_list:

        print('{:20s} {:4s} '.format(pair[0], pair[1]))


histogram(words)
