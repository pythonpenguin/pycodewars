def find(s):
    """

    :param str s:
    :rtype: int
    """
    _res = ""

    for lc in range(1, len(s)):
        _res = s[0:lc]
        _ires = int(_res)
        _nres = _ires + 1
        _to_find = "{}{}".format(_ires, _nres)
        matches = [_res]
        while _to_find in s:
            matches.append(str(_nres))
            _ires = int(_nres)
            _nres = _ires + 1
            _to_find = "{}{}".format(_ires, _nres)
        if "".join(matches) == s:
            return int(_res)
    return int(s)
