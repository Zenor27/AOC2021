class LibCheck:
    @staticmethod
    def check(input_files_and_results: list[tuple[str, int]], input_parse_func: callable):
        def decorator(func):
            def wrapper():
                for input_file, result in input_files_and_results:
                    func_result = func(input_parse_func(input_file))
                    if result is None:
                        print(f"❓ Got {func_result}")
                    elif result != func_result:
                        print(
                            f"⛔️ Sanity check error expected {result} got {func_result}")
                    else:
                        print(f"✅ Sanity check ok, got {result}")
            return wrapper
        return decorator
