from classes.route import RouteClass

def executeAPICall(type, prams, apiState, externalSelf):
    return {"success": "test2"}

route = RouteClass(executeAPICall)