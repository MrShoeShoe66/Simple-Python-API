class compError(Exception):
    def __init__(self, file, message):
        self.message = f"Computing Error\nFailed to compute: {file}\n Because: {message}"
        super().__init__(self.message)
