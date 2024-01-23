"""
s = "<prod><name>drill</name><prx>99</prx><qty>5</qty></prod>

<prod><name>hammer</name><prx>10</prx><qty>50</qty></prod>

(prx stands for price, qty for quantity) and an article i.e "saw".

The function catalog(s, "saw") returns the line(s) corresponding to the article with $ before the prices:

"table saw > prx: $1099.99 qty: 5\nsaw > prx: $9 qty: 10\n..."

If the article is not in the catalog return "Nothing".

"""
import re


def _extract_from_field(line, tag):
    """

    :param str line:
    :param str tag:
    :rtype: str
    """
    return re.search("<{tag}>(.*?)</{tag}>".format(tag=tag), line).groups()[0]


def _preprocess_test(s, article):
    """

    :param str s:
    :param str article:
    :rtype: typing.Iterator
    """
    return (_l.replace('\r', '').strip() for _l in s.split('\n') if article in _l)


def _rewrite_line(line):
    """

    :param str line:
    :param str article:
    :rtype: str
    """
    return "{article} > prx: ${price} qty: {qty}".format(article=_extract_from_field(line, "name"),
                                                         price=_extract_from_field(line, "prx"),
                                                         qty=_extract_from_field(line, "qty"))


def catalog(s, article):
    """

    :param str s:
    :param str article:
    :rtype: str
    """
    return "\r\n".join(map(_rewrite_line,_preprocess_test(s, article))) or "Nothing"
