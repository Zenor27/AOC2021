import time


class LibBench:
    @staticmethod
    def bench(func):
        def _bench(*args, **kwargs):
            start = time.time()
            ret = func(*args, **kwargs)
            end = time.time()
            # Miliseconds to seconds
            print(f"Time: {end - start}s")
            return ret
        return _bench
