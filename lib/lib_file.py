class LibFile:
    @staticmethod
    def read_file(filename) -> str:
        with open(filename, 'r') as file:
            return file.read()

    @staticmethod
    def read_lines(filename) -> str:
        with open(filename, 'r') as file:
            return file.readlines()