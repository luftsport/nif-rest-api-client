import inflection


def _convert_keys(d, convert_function):
    """
    Converts keys recursively by function given
    :param d:
    :param convert_function:
    :return:
    """

    if isinstance(d, dict):
        new = {}
        for k, v in d.items():
            new_v = v
            if isinstance(v, dict):
                new_v = _convert_keys(v, convert_function)
            elif isinstance(v, list):
                new_v = list()
                for x in v:
                    new_v.append(_convert_keys(x, convert_function))

            new[convert_function(k)] = new_v

        return new

    else:
        return d


def snake_case(d):
    """
    Snake case with inflection.underscore
    :param d:
    :return:
    """
    return _convert_keys(d, inflection.underscore)


def del_keys(d, keys, del_none=False):
    """
    Deltes keys given in list
    :param d:
    :param keys:
    :param del_none:
    :return:
    """
    if isinstance(d, dict):
        for k in keys:
            d.pop(k, None)

        return d
    return d

def rename_keys(d, keys):
    """
    Takes a list of tuples
    @todo see if all(isinstance(item, tuple) for item in keys) makes sense
    :param d:
    :param keys:
    :return:
    """
    if isinstance(d, dict):

        for k in keys:
            try:
                d[k[0]] = d.pop(k[1])
            except:
                pass

        return d
    return d


def del_whitelist(d, whitelist):
    """
    Deletes all keys not in whitelist, not recursive
    :param d:
    :param whitelist:
    :return:
    """
    if isinstance(d, dict):
        keys = d.copy().keys()
        for k in keys:
            if k not in whitelist:
                d.pop(k, None)
        return d
    return d


def del_by_value(d, value=None):
    """
    Delete key-value pair by value
    :param d:
    :param value:
    :return:
    """
    if isinstance(d, dict):
        new_d = {}
        for k, v in d.items():
            if v is not value:
                new_d.update({k: v})

        return new_d
    return d


def rename_key(d, keys):
    """
    Maps keys to values in dict
    :param d:
    :param keys:
    :return:
    """
    if isinstance(d, dict):
        for k, v in keys.items():
            if k in d:
                d[v] = d[k]
                d.pop(k, None)

    return d
