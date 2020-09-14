from collections import defaultdict


class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        """
        Instance becomes callable
        """
        self.added += 1
        return 0


if __name__ == "__main__":
    counter = BetterCountMissing()
    assert callable(counter)

    current = {'green': 12, 'blue': 3}
    increments = [
        ('red', 5),
        ('blue', 17),
        ('orange', 9),
    ]
    result = defaultdict(counter, current)

    for key, amount in increments:
        result[key] += amount

    assert counter.added == 2

    print(result)
