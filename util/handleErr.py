import util.getRoutes
import json

errorFuncs = util.getRoutes.import_files_from_folder("err")

errKeys = list(errorFuncs.keys())

def handleErr(errId, compErr):
    for err in errKeys:
        if errorFuncs[err] == errId:
            out = err.compErr()
            out[2] = out[2].encode("utf-8")
            return out
    return [
        errId, 500,
        json.dumps({"err":"Unknown Problem has occured, please try again later. if you are the developer please also check that this error is handeled by you code"})
    ]
