from check_number import is_number


def clean(string):
    word = string.replace('\n', ' ')
    symbols = list("&÷×|/()[]{}=<>*\"':;?,.")
    for symbol in symbols:
        word = word.replace(symbol, '')
    return word


def extract(string):
    numbers = []
    words = string.replace('\n', ' ').split()
    for word in words:
        word = clean(word)
        if is_number(word):
            numbers.append(word)
    return numbers
