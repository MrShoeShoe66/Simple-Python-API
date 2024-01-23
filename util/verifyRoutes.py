import classes.route
import exeptions.routeErr

def checkRoutes(modules):
    keys = list(modules.keys())
    for mod in keys:
        try:
            modules[mod].route
        except Exception:
            raise exeptions.routeErr.RouteError(f"./{mod}","This module does not have a route or is not formated correctly.")
        if not isinstance(modules[mod].route, classes.route.RouteClass):
            raise exeptions.routeErr.RouteError(mod, f"Module {mod} is not initated to route class but {type(modules[mod].route)} class")
        

            