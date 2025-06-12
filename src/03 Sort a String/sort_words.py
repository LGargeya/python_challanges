'''
def sort_words(words):
    return ' '.join(sorted(words.split(), key=str.casefold)) # key = str.casefold tells to ignore the case while sorting
'''
def sort_words(input):
    words = input.split()
    words = [w.lower()+w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)

# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE

