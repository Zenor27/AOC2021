from itertools import islice, zip_longest


class LibIterable:
    @staticmethod
    def grouper(iterable, n, fillvalue=None):
        args = [iter(iterable)] * n
        return list(zip_longest(*args, fillvalue=fillvalue))

    @staticmethod
    def sliding_grouper(iterable, n):
        res = []
        for i in range(len(iterable) - n + 1):
            res.append(tuple(iterable[i: i + n]))
        return res
