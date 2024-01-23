class RouteClass:
    def __init__(self, returnFunction):
        self.returnFunction = returnFunction

    def execute(self, prams, type, apiState, externalSelf):
        return self.returnFunction(type, prams, apiState, externalSelf) 