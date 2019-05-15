"""Contains categories for tokens and tokenize function"""
import string

NUMERIC = string.digits + '.'
PUNCTUATION = '!"#$%&\'*+,-/:;<=>?@\\^_`|~'
BRACKETS = '(){}[]'


def tokenize(expression):
    """Returns list of tokens from input string"""
    categories = [
        string.ascii_lowercase,
        NUMERIC,
        string.whitespace,
        PUNCTUATION,
        BRACKETS
    ]
    token = ''
    tokens = []
    category = None
    expression = prepare_string(expression)
    for char in expression:
        if token:
            if category and char in category:
                token += char
            else:
                tokens = append_token(tokens, token)
                token = char
                category = None
                for cat in categories:
                    if char in cat:
                        category = cat
                        break
        else:
            category = None
            if not category:
                for cat in categories:
                    if char in cat:
                        category = cat
                        break
            token += char
    if token:
        tokens = append_token(tokens, token)
    return tokens


def prepare_string(expression):
    return expression.replace('log10(', 'lg(')


def append_token(tokens, token):
    """append token to tokens"""
    if '+' in token or '-' in token or ')' in token or '(' in token:
        for char in token:  # if token contains multy +, - or () characters, split it
            tokens.append(char)
    else:
        tokens.append(token)
    return tokens
