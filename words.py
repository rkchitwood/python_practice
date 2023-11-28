def print_upper_words(words):
    """prints each provided word on a seperate line, in uppercase"""
    for word in words:
        print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "excelsior!"])

def print_upper_words2(words):
    """prints each provided word on a seperate line in uppercase, only if they begin with the letter 'e'"""
    for word in words:
        if word[0] == 'e':
            print(word.upper())

print_upper_words2(["hello", "hey", "goodbye", "yo", "yes", "excelsior!"])

def print_upper_words3(words, must_start_with):
    """prints each provided word on a seperate line in uppercase, only if they begin with the passed in set of letters"""
    for word in words:
        if word[0] in must_start_with:
            print(word.upper())

print_upper_words3(["hello", "hey", "goodbye", "yo", "yes", "excelsior!"], ["h","y"])