from data import DICTIONARY, LETTER_SCORES

TEST_WORDS = ('bob', 'julian', 'pybites', 'quit', 'barbeque')

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as file:
        return tuple(word.rstrip('\n') for word in file)

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for letter in word:
        if letter.upper() in LETTER_SCORES:
            value = value + LETTER_SCORES[letter.upper()]
    return value

def max_word_value(word_list = list()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not len(word_list):
        word_list = load_words()
    
    word_list_values = {word:calc_word_value(word) for word in word_list}
    ordered_by_value = sorted(word_list_values.items(), key=lambda x: x[1])
    return ordered_by_value[-1][0]

if __name__ == "__main__":
    pass
