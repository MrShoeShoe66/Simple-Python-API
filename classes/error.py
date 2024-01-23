class errorClass:
    def __init__(self, errid, returnFunc):
        self.id = errid
        self.func = returnFunc
        if 400<=self.id<=499:
            self.type = "client"
        elif 500<=self.id<=599:
            self.type = "server"
        else:
            self.type = "unknown"
    def compErr(self,errData):
        return [self.id, self.type, self.func(errData)]