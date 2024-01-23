class authErr(Exception):
    def __init__(self, message):
        self.message = f"Auth Error\Message: {message}"
        super().__init__(self.message)
