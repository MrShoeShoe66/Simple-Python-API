class RouteError(Exception):
    def __init__(self, file, message):
        self.message = f"Route Error\nBad Route File: {file}\n Because: {message}"
        super().__init__(self.message)
