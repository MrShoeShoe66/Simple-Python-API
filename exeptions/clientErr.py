class clientErr(Exception):
    def __init__(self, message):
        self.message = f"Client Error\Message: {message}"
        super().__init__(self.message)
