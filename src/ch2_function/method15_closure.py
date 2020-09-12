
def sort_priority(numbers, group):
    found = False

    def helper(x):
        if x in group:
            # Avoid "Unused variable 'found'"
            nonlocal found
            found = True
            return 0, x
        return 1, x
    numbers.sort(key=helper)
    return found


if __name__ == "__main__":
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = [2, 3, 5, 7]
    found = sort_priority(numbers, group)
    print(found)
    print(numbers)
