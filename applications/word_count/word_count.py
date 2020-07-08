# lowercase all letters
# split on whitespace
# iterate through string to remove unwanted characters
# iterate through that to add to counter
# return dictionary with count of how many times a word occurs

def word_count(s):
    bad_chars = ['"', ':', ';', ',', '.', '-', '+', '=', '/',
                 '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    counter = {}
    s = s.lower()
    for i in bad_chars:
        s = s.replace(i, '')
    res = s.split()

    for word in res:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1

    return counter


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
