#!/usr/local/bin/python3

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
def book_title(title_name):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'

    >>> book_title('')
    ' '
    
    """
    if not title_name:
        return ' '
    lst_of_words = title_name.lower().split()
    new_title = [lst_of_words.pop(0).title()]
    for word in lst_of_words:
        if word in small_words:
            new_title.append(word)
            continue
        new_title.append(word.title())
    new_title = ' '.join(new_title)
    return new_title

def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()