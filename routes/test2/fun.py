from classes.route import RouteClass

def executeAPICall(type, prams, apiState, externalSelf):
    return {"success": "test3"}

route = RouteClass(executeAPICall)