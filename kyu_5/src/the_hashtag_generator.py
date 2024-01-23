def generate_hashtag(s):
    """

    :param str s:
    :rtype: str or False
    """
    _s = "".join((_word.capitalize() for _word in s.split(" "))) #title not capitalize
    if 0<len(_s)<140:
        return "#{}".format(_s)
    return False

