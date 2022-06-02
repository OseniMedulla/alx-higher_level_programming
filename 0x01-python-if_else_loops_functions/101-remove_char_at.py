def remove_char_at(str, n):
    """Deletes the character at the n position of the str
    This function creates a copy of the string, deletes
    a position of the passed string and returns a string
    without the deleted position
    Parameters
    ----------
    str : str
        The string from which the position needs to be removed
    n : int
        The position of the string to be deleted
    Returns
    -------
    str
        The copy of the string without the deleted position
    """
if n < 0:
    return (str)
return (str[:n] + str [n+1:])
