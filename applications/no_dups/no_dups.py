# split strings by whitespace
# iterate through list
# remove any duplicates
# remove whitespace at end

def no_dups(s):
    s = s.split()
    res = list(dict.fromkeys(s))
    string = " "
    result = string.join(res).strip()

    return result


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
