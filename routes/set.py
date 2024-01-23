from classes.route import RouteClass

def executeAPICall(type, prams, apiState, externalSelf):
    apiState[prams["s"]] = prams["d"]
    print(apiState)
    return {"success": True}

route = RouteClass(executeAPICall)