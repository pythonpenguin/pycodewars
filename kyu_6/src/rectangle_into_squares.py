import collections


def _extract_sq(positions: set, lng: list, wdth: list, sq_dim: int) -> list:
    sq = sq_dim * sq_dim
    _ac = {(x,y) for x in lng[0:sq_dim] for y in wdth[0:sq_dim]}
    if len(_ac) == sq:
        positions.difference_update(_ac)
        return [sq_dim]
    return []


def _row_column_available(positions: set, ) -> tuple:
    _row = collections.defaultdict(lambda: 0)
    _column = collections.defaultdict(lambda: 0)
    for x, y in positions:
        _row[x] += 1
        _column[y] += 1
    act_dim = min([max(_row.values()), max(_column.values())])
    return (sorted((r for r, c in _row.items() if c >= act_dim)),
            sorted((_c for _c, _r in _column.items() if _r >= act_dim)), act_dim)


def sq_in_rect(lng, wdth):
    """

    def sqInRect(lng, wdth, recur = 0):
    if lng == wdth:
        return (None, [lng])[recur]            # If this is original function call, return None for equal sides (per kata requirement);
                                               # if this is recursion call, we reached the smallest square, so get out of recursion.
    lesser = min(lng, wdth)
    return [lesser] + sqInRect(lesser, abs(lng - wdth), recur = 1)


    :param lng:
    :param wdth:
    :return:
    """
    # your code
    if lng == wdth:
        return None
    positions = {(x, y) for x in range(lng) for y in range(wdth)}
    sq_dims = []
    while positions:
        _lng, _wdth, sq_dim = _row_column_available(positions)
        sq_dims.extend(_extract_sq(positions, _lng, _wdth, sq_dim))
    return sorted(sq_dims, reverse=True)
