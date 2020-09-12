def not_keyword_only_func(a, b, c=1):
    return a*b*c


def keyword_only_func(a, b, *, c=1):
    """
    '*' is the end of positional arguments
    """    
    return a*b*c


if __name__ == "__main__":
    not_keyword_only_func(1, 2, 3)

    # keyword_only_func() takes 2 positional arguments but 3 were given
    keyword_only_func(1, 2, 3)

    keyword_only_func(1, 2, c=3)
