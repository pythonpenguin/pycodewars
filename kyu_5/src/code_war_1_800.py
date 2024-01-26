MAPS = {}
for _index, seq in enumerate(
        [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'H', 'I'), ('J', 'K', 'L'), ('M', 'N', 'O'), ('P', 'Q', 'R', 'S'),
         ('T', 'U', 'V'), ('W', 'X', 'Y', 'Z')], 2):
    for char in seq:
        MAPS[char] = str(_index)


def _estrai_parole_simili(av_words,mn):
    """

    :param list av_words:
    :param list mn:
    :rtype: list of tuple
    """
    _ret = []
    for word in av_words:
        _nw = [MAPS[c] for c in word]
        if mn == _nw:
            _ret.append((_nw,word))
    return _ret


def parole_valide(av_words, first, second):
    """

    :param list av_words:
    :param str first:
    :param str second:
    :rtype: list of tuple
    """
    _fn = [MAPS[c] for c in first]
    _ln = [MAPS[c] for c in second]
    _fwords = _estrai_parole_simili(av_words, _fn)
    _lwords = _estrai_parole_simili(av_words, _ln)
    _rn = _fn + _ln
    res = []
    for _nfw,_fw in _fwords:
        for _nlw,_lw in _lwords:
            number = _nfw + _nlw
            if number == _rn:
                res.append((_fw,_lw))
    return res


def check1800(s):
    """

    :param str s:
    :rtype: set
    """
    base, _c, ext = s.rsplit("-", 2)
    n2f = _c + ext
    allword = parole_valide(WORDS, n2f[0:4], n2f[4:]) + parole_valide(WORDS, n2f[0:3], n2f[3:])
    print(WORDS)
    return {"{base}-{cent}-{ext}".format(base=base, cent=cent, ext=ext) for cent, ext in allword}
