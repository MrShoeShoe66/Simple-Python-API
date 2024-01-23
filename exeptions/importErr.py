class ImmportError(Exception):
    def __init__(self, file, message):
        self.message = f"Import Error\nFailed to import: {file}\n Because: {message}"
        super().__init__(self.message)
