import string


def is_pangram(s):
    """

    :param str s:
    :rtype: bool
    """
    return len({_c for _c in s.lower() if _c.isalpha()}) == len(string.ascii_lowercase)
