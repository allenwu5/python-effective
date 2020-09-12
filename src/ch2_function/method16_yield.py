
def index_token(lines):
    offset = 0
    for line in lines:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


if __name__ == "__main__":
    lines = ["it's a good article.", "you must read it."]

    # <generator object index_token at 0x7ff361269510>
    print(index_token(lines))

    # [0, 5, 7, 12, 20, 24, 29, 34]
    print(list(index_token(lines)))
