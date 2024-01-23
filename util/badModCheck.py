import exeptions.importErr as impErr

def checkForBadModuleNames(modules):
    keys = list(modules.keys())
    for mod in keys:
        if len(mod) >= 1:
            if mod[-1] == "/":
                if mod[:-1] in keys:
                    raise impErr.ImmportError(
                        f"./{mod} & ./{mod[:-1]}", 
                        f"Folder {mod} name is the same as a module name for the {mod[:-1]} module\nThis is not needed as the program autoroutes one to the other if either is avalible. If you want to use the same name for both, use a different name for the folder."
                    )
            else:
                if f"{mod}/" in keys:
                    raise impErr.ImmportError(
                        f"./{mod} & ./{mod}/",
                        f"Folder {mod}/ name is the same as a module name for the {mod} module\nThis is not needed as the program autoroutes one to the other if either is avalible. If you want to use the same name for both, use a different name for the folder."
                    )