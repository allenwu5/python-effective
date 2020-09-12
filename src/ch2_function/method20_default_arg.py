def decode(data, default={}):
    if data:
        return data
    else:
        return default


def decode2(data, default=None):
    if data:
        return data
    else:
        return {} if default is None else default


if __name__ == "__main__":
    print(decode("a"))
    print(decode(None))
    d = decode(None)
    d["key"] = "value"
    print(decode(None))

    d = decode2(None)
    d["key"] = "value"
    print(decode2(None))
