from classes.route import RouteClass

def executeAPICall(type, prams, apiState, externalSelf):
    print(type, prams, apiState)
    return {"success": "final test"}


route = RouteClass(executeAPICall)
