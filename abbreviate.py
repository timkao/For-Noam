# re-organize the string to remove anything which is not number or alphabet

def abbreviate2(s):
    import re
    words = re.split("\W+", s)
    for word in words:
        if len(word) > 3:
            w = word[0] + str(len(word)-2) + word[-1]
            s = s.replace(word, w)
    return words
